"""

"""
from abc import ABC, abstractmethod
from typing import Dict, final

from .client import Client, OSCClient
from .component import EndpointBase
from .exceptions import IllegalQueryException, QueryException


class Endpoint(EndpointBase):
    """

    """
    allow_bulk_queries: bool = True

    _client: Client
    _read_only: bool

    _read_path: str | None

    def __init__(
            self, client: Client, path: str, read_path: str | None = None, read_only: bool = False,
            index: str | int | None = None, index_format_string: str = "/{index}", **kwargs
    ):
        """

        :param path:
        """
        super().__init__(path=path, index=index, index_format_string=index_format_string)
        self._client = client
        self._read_only = read_only
        self._read_path = read_path
        try:
            self._init(**kwargs)
        except TypeError as e:
            raise QueryException(str(e), path=self._path) from e

    @property
    def path(self):
        """

        :return:
        """
        return self.indexed_path

    @property
    def read_path(self) -> str:
        """

        :return:
        """
        if self._read_path is None:
            return self.path
        if self._index is not None:
            return f"{self._read_path}{self._index_format_string.format(index=self._index)}"
        return self._read_path

    @property
    def read_only(self) -> bool:
        return self._read_only

    @property
    def allow_bulk_queries(self) -> bool:
        return True

    async def get(self):
        """

        :return:
        """
        response = await self._client.query(path=self.read_path)
        return self._parse_response(response=response)

    async def set(self, parameter):
        """

        :return:
        """
        if self.read_only:
            raise IllegalQueryException(
                f"Trying to send set request for read-only endpoint! Parameter: '{parameter}'",
                path=self.path
            )
        parameter = self._parse_parameter(parameter)
        await self._client.send(path=self.path, parameter=parameter)

    def _init(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def _parse_response(self, response):
        """

        :param response:
        :return:
        """

    async def _parse_parameter(self, parameter) -> str:
        """

        :param value:
        :return:
        """
        return str(parameter)


class ComplexEndpoint(EndpointBase):
    """

    """
    _endpoints: Dict[str, Endpoint]
    _read_only: bool

    def __init__(
            self, client: Client, path: str, endpoints: dict, index: str | int | None = None,
            index_format_string: str = "/{index}", read_only: bool = True
    ):
        """

        :param endpoints:
        """
        super().__init__(path=path, index=index, index_format_string=index_format_string)
        self._read_only = read_only
        self._endpoints = {}
        for name, config in endpoints.items():
            kwargs = {
                "client": client,
                "path": f"{path}{config['path']}",
                "read_only": config["read_only"] if "read_only" in config else False
            }
            for arg, value in config.items():
                if arg not in ["class", "path", "read_only", "count"]:
                    kwargs.update({ arg: value })
            self._endpoints.update({ name: config["class"](**kwargs) })

    @final
    @property
    def read_only(self) -> bool:
        return self._read_only

    @final
    async def get(self):
        """

        :return:
        """
        responses = {}
        for name, endpoint in self._endpoints.items():
            responses.update({ name: await endpoint.get() })
        return self._parse_responses(responses=responses)

    @final
    async def set(self, parameter):
        """

        :return:
        """
        if self._read_only:
            raise IllegalQueryException(
                f"Trying to send set request for read-only endpoint! Parameter: '{parameter}'",
                path=self.path
            )
        parameters = self._unpack_parameter(parameter=parameter)
        for name, parameter in parameters.items():
            if name not in self._endpoints:
                raise IllegalQueryException(
                    f"Trying to set parameter for non-existing endpoint '{name}'!"
                )
            await self._endpoints[name].set(parameter)

    @abstractmethod
    def _parse_responses(self, responses: dict):
        """

        :param responses:
        :return:
        """

    def _unpack_parameter(self, parameter) -> dict:
        """

        :param parameter:
        :return:
        """
        return {}
