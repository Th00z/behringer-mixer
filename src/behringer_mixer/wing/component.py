"""

"""
import re
from typing import Dict, Type
from abc import ABC, abstractmethod
from copy import deepcopy

from behringer_mixer.component import ComponentBase, Component
from behringer_mixer.client import Client
from behringer_mixer.endpoint import Endpoint
from behringer_mixer.exceptions import QueryException

from .endpoint import BoolEndpoint, FloatEndpoint, StringEnumEndpoint, StringMappingEndpoint


class EQBand(Component):
    """

    """
    _components = {}

    _endpoints = {
        "gain": {
            "path": "g",
            "class": FloatEndpoint,
            "min": -15.0,
            "max": 15.0,
            "aliases": [ "g" ]
        },
        "frequency": {
            "path": "f",
            "class": FloatEndpoint,
            "min": 20.0,
            "max": 20000.0,
            "aliases": [ "f" ]
        },
        "q": {
            "path": "q",
            "class": FloatEndpoint,
            "min": 0.44,
            "max": 10.0
        },
    }


class EQShelf(Component):
    """

    """
    _frequency_min: float = 20.0
    _frequency_max: float = 20000.0

    _components = {}

    _endpoints = {
        "gain": {
            "path": "sg",
            "class": FloatEndpoint,
            "min": -15.0,
            "max": 15.0
        },
        "frequency": {
            "path": "sf",
            "class": FloatEndpoint,
            "min": _frequency_min,
            "max": _frequency_max
        }
    }


class ConcretePlugin(Component):
    """

    """
    @staticmethod
    @abstractmethod
    def model_key() -> str:
        """

        :return:
        """

    @staticmethod
    @abstractmethod
    def model_name() -> str:
        """

        :return:
        """


class PluginComponent(Component):
    """

    """
    _model_endpoint_path = "/mdl"

    _components = {}
    _endpoints = {}

    _model_identifier: str | None
    _model_class_map: dict
    _model_components: Dict[str, Type[ConcretePlugin]]
    _model_endpoint: StringMappingEndpoint

    def __init__(
            self, client: Client, path: str = "", variant: str | None = None,
            index: str | int | None = None, index_format_string: str = "/{index}"
    ):
        """

        :param client:
        :param path:
        :param index:
        :param variant:
        """
        super().__init__(
            client=client, path=path, variant=variant, index=index,
            index_format_string=index_format_string
        )
        self._model_components = {}
        self._populate_models()
        self._populate_model_endpoint()
        self._model_identifier = None

    @property
    @abstractmethod
    def _models(self) -> list:
        """

        :return:
        """
        return []

    @property
    def model(self) -> Component:
        """

        :return:
        """
        return self._model_endpoint

    async def plugin(self) -> ComponentBase:
        """

        :return:
        """
        required_model = await self._model_endpoint.get()
        if required_model not in self._model_components:
            if required_model not in self._model_class_map:
                raise QueryException(
                    f"Invalid plugin model: '{required_model}'!", self.indexed_path
                )
            self._model_components.update({
                required_model: self._model_class_map[required_model](
                    client=self._client, path=self.indexed_path, variant=self._variant
                )
            })
        return self._model_components[await self._model_endpoint.get()]

    def _populate_model_endpoint(self):
        """

        :param client:
        :param path_base:
        :return:
        """
        string_mapping = {}
        for name, model in self._model_class_map.items():
            string_mapping.update({ model.model_key(): name })

        self._model_endpoint = StringMappingEndpoint(
            client=self._client, path=f"{self.indexed_path}{self._model_endpoint_path}",
            string_mapping=string_mapping
        )

    def _populate_models(self):
        """

        :return:
        """
        self._model_class_map = {}
        for cls in self._models:
            self._model_class_map.update({ cls.model_name(): cls })


class LeftRightComponent(Component, ABC):
    """

    """
    _side_regex = re.compile(r"\/(?P<side>[lr])$")

    def _parse_endpoint_kwargs(self, name: str, config: dict, path_base: str) -> dict:
        """

        :param name:
        :param config:
        :param path_base:
        :return:
        """
        config = deepcopy(config)
        if "path" not in config:
            raise QueryException(f"Invalid config for endpoint '{name}'!", path=path_base)
        side_match = self._side_regex.search(path_base)
        if side_match is None:
            raise QueryException(
                f"LeftRightComponent path must be just '/l' or '/r'!", path=path_base
            )
        config["path"] = config["path"].format(side=side_match["side"])
        stripped_path_base = re.sub(self._side_regex, "/", path_base)
        return super()._parse_endpoint_kwargs(
            name=name, config=config, path_base=stripped_path_base
        )


class PostIndexedComponent(Component, ABC):
    """

    """
    def __init__(
            self, client: Client, path: str = "", variant: str | None = None,
            index: str | int | None = None
    ):
        """

        :param client:
        :param path:
        :param variant:
        :param index:
        :param index_format_string:
        """
        super().__init__(
            client=client, path=path, variant=variant, index=index, index_format_string=""
        )

    def _parse_endpoint_kwargs(self, name: str, config: dict, path_base: str) -> dict:
        """

        :param name:
        :param config:
        :param path_base:
        :return:
        """
        config = deepcopy(config)
        if "path" not in config:
            raise QueryException(f"Invalid config for endpoint '{name}'!", path=path_base)
        config["path"] = config["path"].format(index=self._index)
        return super()._parse_endpoint_kwargs(name=name, config=config, path_base=path_base)
