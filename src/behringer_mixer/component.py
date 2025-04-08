"""

"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Dict, Type, final
from copy import deepcopy
from string import ascii_uppercase

from netaddr import IPAddress

from .client import Client
from .exceptions import (
    EndpointException, QueryException, ComponentOutOfBoundsException, BehringerMixerException
)


class EndpointBase(ABC):
    """

    """
    _path: str
    _index: str | int | None
    _index_format_string: str

    def __init__(
            self, path: str, index: str | int | None = None, index_format_string: str = "/{index}"
    ):
        """

        :param path:
        """
        self._path = path
        self._index = index
        self._index_format_string = index_format_string

    @property
    def indexed_path(self) -> str:
        """

        :return:
        """
        if self._index is not None and self._index_format_string != "":
            return f"{self._path}{self._index_format_string.format(index=self._index)}"
        return self._path


class ComponentBase(EndpointBase):
    """

    """
    _client: Client
    _variant: str | None
    _component_objects: dict
    _endpoint_objects: dict

    @property
    @abstractmethod
    def _components(self) -> dict:
        """

        :return:
        """
        return {}

    @property
    @abstractmethod
    def _endpoints(self) -> dict:
        """

        :return:
        """
        return {}



    def __init__(
            self, client: Client, path: str, variant: str | None = None,
            index: str | int | None = None, index_format_string: str = "/{index}"
    ):
        """

        :param client:
        :param path:
        :param variant:
        :param index:
        :param index_format_string:
        """
        super().__init__(path=path, index=index, index_format_string=index_format_string)
        self._variant = variant
        self._client = client
        self._component_objects = {}
        self._endpoint_objects = {}

    def __str__(self):
        """

        :return:
        """
        return self.indexed_path

    def __repr__(self):
        """

        :return:
        """
        components_str = ""
        if self._components:
            components_str = f"; Components: {', '.join(self._components.keys())}"
        endpoints_str = ""
        if self._endpoints:
            endpoints_str = f"; Endpoints: {', '.join(self._endpoints.keys())}"
        return f"{self.__str__()} ({self.__class__.__name__}{components_str}{endpoints_str})"

    def __getattr__(self, item: str):
        """

        :param item:
        :return:
        """
        match item:
            case item if item in self._component_objects:
                return self._component_objects[item]
            case item if item in self._endpoint_objects:
                return self._endpoint_objects[item]
            case item if item in self._components:
                self._populate_component(name=item)
                return self._component_objects[item]
            case item if item in self._endpoints:
                self._populate_endpoint(name=item)
                return self._endpoint_objects[item]
            case _:
                raise AttributeError(
                    f"No Component or Endpoint named '{item}' for component {self.indexed_path}"
                )

    def _component_setup(self):
        """

        :return:
        """
        self._resolve_aliases()
        self._filter_variants()
        self._check_duplicates()

    def _resolve_aliases(self):
        """

        :param configs:
        :return:
        """
        for configs in [self._components, self._endpoints]:
            new_fields = {}
            for name, config in configs.items():
                if "aliases" in config:
                    for alias in config["aliases"]:
                        if alias in new_fields:
                            raise QueryException(
                                f"Duplicate Alias name: '{alias}'", path=self._path
                            )
                        new_fields.update({ alias: config })
                    del config["aliases"]
            for name, config in new_fields.items():
                if name in configs:
                    raise QueryException(
                        f"Duplicate Component/Endpoint name: '{name}'", path=self._path
                    )
                configs.update({ name: config })

    def _filter_variants(self):
        """

        :param configs:
        :return:
        """
        for configs in [self._components, self._endpoints]:
            for name, config in configs.items():
                if "variants" in config:
                    if self._variant is None:
                        continue
                    for variant, variant_config in config["variants"].items():
                        if self._variant == variant:
                            configs[name] = variant_config

    def _check_duplicates(self):
        """

        :return:
        """
        all_names = []
        for configs in [self._components, self._endpoints]:
            for name in configs:
                if name in all_names:
                    raise QueryException(
                        f"Name Conflict! Both Component and Endpoint defined for name '{name}'!",
                        path=self._path
                    )

    def _populate_component(self, name: str):
        """

        :param path_base:
        :param name:
        :param config:
        :return:
        """
        if name not in self._components:
            raise QueryException(f"Unknown component: '{name}'!", path=self.indexed_path)
        config = self._components[name]
        if "path" not in config or "class" not in config:
            raise QueryException(f"Invalid config for component: '{name}'!", path=self.indexed_path)
        kwargs = {
            "client": self._client,
            "path": f"{self.indexed_path}{config['path']}",
            "variant": self._variant
        }
        for arg, value in config.items():
            if arg not in ["class", "path", "count", "alphabet_indexed"]:
                kwargs.update({ arg: value })
        if 'count' in config:
            component_dict = {} # dict not list as this is 1-indexed for better mapping
            for index in range(0, config['count']):
                if "alphabet_indexed" in config and config["alphabet_indexed"]:
                    letter = ascii_uppercase[index]
                    component_dict.update(
                        { letter: config["class"](index=letter, **kwargs) }
                    )
                else:
                    component_dict.update(
                        { index + 1: config["class"](index=index + 1, **kwargs) }
                    )
            self._component_objects.update({ name: component_dict })
        else:
            self._component_objects.update({
                name: config["class"](**kwargs)
            })

    def _populate_endpoint(self, name: str):
        """

        :param name:
        :return:
        """
        config = self._get_endpoint_config(name=name)
        kwargs = self._parse_endpoint_kwargs(
            name=name, config=config, path_base=self._get_path_base()
        )
        if 'count' in config:
            endpoint_dict = {} # dict not list as this is 1-indexed for better mapping
            for index in range(0,config["count"]):
                if "alphabet_indexed" in config and config["alphabet_indexed"]:
                    endpoint_index = ascii_uppercase[index]
                else:
                    endpoint_index = index + 1
                endpoint_dict.update({
                    endpoint_index: config["class"](index=endpoint_index, **kwargs)}
                )
            self._endpoint_objects.update({ name: endpoint_dict })
        else:
            self._endpoint_objects.update({ name: config["class"](**kwargs) })

    def _parse_endpoint_kwargs(self, name: str, config: dict, path_base: str) -> dict:
        """

        :param name:
        :param config:
        :param path_base:
        :return:
        """
        if "path" not in config or "class" not in config:
            raise QueryException(f"Invalid config for endpoint '{name}'!", path=path_base)
        kwargs = {
            "client": self._client,
            "path": f"{path_base}{config['path']}",
            "read_only": config["read_only"] if "read_only" in config else False
        }
        if "read_path" in config:
            kwargs.update({ "read_path": f"{path_base}{config['path']}" })
        for arg, value in config.items():
            if arg not in ["class", "path", "read_path", "read_only", "count", "alphabet_indexed"]:
                kwargs.update({ arg: value })
        return kwargs

    def _get_endpoint_config(self, name: str) -> dict:
        """

        :param name:
        :param config:
        :return:
        """
        if name not in self._endpoints:
            raise QueryException(f"Unknown endpoint: '{name}'!", path=self.indexed_path)
        return self._endpoints[name]

    def _get_path_base(self) -> str:
        """

        :return:
        """
        return self.indexed_path

    @final
    @staticmethod
    def _get_component_by_index(
            components: List[Component], name: str, index: int, max: int
    ) -> Component:
        """

        :param components:
        :param index:
        :param max:
        :return:
        """
        if 0 < index <= max:
            return components[index - 1]
        raise ComponentOutOfBoundsException(
            f"Index '{index}' out of bounds for {name}. Available endpoints: 1-{max}"
        )


class Component(ComponentBase):
    """

    """
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
        self._component_setup()


class MixingConsole(ComponentBase):
    """

    """

    def __init__(self, client: Client, variant: str | None = None):
        """

        :param client:
        :param path:
        :param variant:
        """
        super().__init__(client=client, path="", variant=variant, index=None)


    async def initialize(self):
        """

        :return:
        """
        await self._client.initialize()
        self._component_setup()

    @classmethod
    @abstractmethod
    def _get_client(cls, host: str | IPAddress, port: int | None = None, **kwargs) -> Client:
        """

        :param host:
        :param port:
        :return:
        """
        if port is None:
            port = cls._default_port
        return _client_class(mixer_host=host, mixer_port=port, **kwargs)

    @classmethod
    def create(
            cls, host: str | IPAddress, port: int | None = None, variant: str | None = None,
            **kwargs
    ) -> MixingConsole:
        """

        :param host:
        :param port:
        :param variant:
        :return:
        """
        client = cls._get_client(host=host, port=port, **kwargs)
        return cls(client=client, variant=variant)
