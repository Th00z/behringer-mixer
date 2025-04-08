"""
Client module for the connection between the wrapper objects and the actual mixing desks.
"""
import asyncio
import logging
import time

from typing import final, Optional, Callable, Dict, Any, List, Tuple
from abc import ABC, abstractmethod
from copy import deepcopy

from netaddr import IPAddress
from jsonschema import validate, ValidationError
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_message_builder import OscMessageBuilder
from pythonosc.osc_server import AsyncIOOSCUDPServer

from .exceptions import NoResponseException


class Client(ABC):
    """

    """
    _mixer_host: str | IPAddress
    _mixer_port: int

    _logger: logging.Logger


    def __init__(self, mixer_host: str | IPAddress, mixer_port: int):
        """

        :param mixer_host:
        :param mixer_port:
        """
        self._mixer_host = mixer_host
        self._mixer_port = mixer_port
        self._logger = logging.getLogger("behringer-mixer :: Client")

    @abstractmethod
    async def initialize(self):
        """
        :return:
        """


    @abstractmethod
    async def send(self, path: str, parameter: str | None = None):
        """

        :param path:
        :param parameter:
        :return:
        """

    @abstractmethod
    async def raw_send(self, message: bytes):
        """

        :param message:
        :return:
        """

    @abstractmethod
    async def query(self, path: str, parameter: str | None = None):
        """

        :param path:
        :param parameter:
        :return:
        """

    @abstractmethod
    async def raw_query(self, message: bytes):
        """

        :param message:
        :return:
        """


class OSCClient(Client):
    """
    Handles the communication with the mixer via the OSC protocol
    """
    __osc_client_server: AsyncIOOSCUDPServer | None
    __inter_message_delay: float
    __query_response_timeout: float

    __query_response = None
    __new_query_response: bool

    def __init__(
            self, mixer_host: str | IPAddress, mixer_port: int,
            inter_message_delay: float = 0.002, query_response_timeout: float = 0.1
    ):
        """

        :param mixer_host:
        :param mixer_port:
        :param query_response_wait_time:
        :param query_response_timeout:
        """
        super().__init__(mixer_host=mixer_host, mixer_port=mixer_port)
        self.__inter_message_delay = inter_message_delay
        self.__query_response_timeout = query_response_timeout

        self.__osc_client_server = None
        self.__transport = None
        self.__protocol = None

        self.__query_response = None
        self.__new_query_response = False
        self.__last_received_timestamp = 0


        self._logger = logging.getLogger("behringer-mixer :: OSCClient")

    def __del__(self):
        """

        :return:
        """
        self.close()

    def close(self):
        """
        Stop the OSC server
        """
        if self.__transport is not None:
            try:
                self.__transport.close()
            except RuntimeError:
                pass
            self.__transport = None
        del self.__osc_client_server
        self.__osc_client_server = None

    async def initialize(self):
        """

        :return:
        """
        if not self.__osc_client_server:
            dispatcher = Dispatcher()
            dispatcher.set_default_handler(self.__msg_handler)
            self.__osc_client_server = AsyncIOOSCUDPServer(
                ("0.0.0.0", 0), dispatcher, asyncio.get_event_loop()
            )
            self.__transport, self.__protocol = await self.__osc_client_server.create_serve_endpoint()
            self.__osc_client_server.transport = self.__transport
            self.__osc_client_server.protocol = self.__protocol

    async def send(self, path: str, parameter: str | None = None):
        """

        :param path:
        :param parameter:
        :return:
        """
        self._logger.debug(f"Sending: {path} {parameter if parameter is not None else ''}")
        message_builder = OscMessageBuilder(address=path)
        if parameter is not None:
            message_builder.add_arg(parameter)
        message = message_builder.build()
        self.__transport.sendto(message.dgram, self.__mixer_address())
        await asyncio.sleep(self.__inter_message_delay)

    async def raw_send(self, message: bytes):
        """

        :param message:
        :return:
        """
        self.__transport.sendto(message, self.__mixer_address())
        await asyncio.sleep(self.__inter_message_delay)

    async def query(self, path: str, parameter: str | None = None):
        """

        :param path:
        :param parameter:
        :return:
        """
        self.__query_response = None
        self.__new_query_response = False
        await self.send(path=path, parameter=parameter)
        return await self.__wait_for_query_response(path=path)

    async def raw_query(self, message: bytes):
        """

        :param message:
        :return:
        """
        self.__query_response = None
        self.__new_query_response = False
        await self.raw_send(message)
        return await self.__wait_for_query_response(path="")

    async def __wait_for_query_response(self, path: str):
        """

        :return:
        """
        if self.__new_query_response is False:
            await asyncio.sleep(self.__query_response_timeout)
        if self.__new_query_response is False:
            raise NoResponseException(
                "Request timed out without receiving response.", path=path
            )

        response = deepcopy(self.__query_response)
        self.__query_response = None
        self.__new_query_response = False

        return response

    def __mixer_address(self) -> Tuple[str, int]:
        """

        :return:
        """
        if isinstance(self._mixer_host, IPAddress):
            return str(self._mixer_host), self._mixer_port
        if isinstance(self._mixer_host, str):
            return self._mixer_host, self._mixer_port
        raise ValueError(f"Invalid type for mixer_host: {type(self._mixer_host)}")

    def __msg_handler(self, addr, *data):
        """
        Handle callback response
        """

        self._logger.debug(f"received: {addr} {data if data else ''}")
        self.__query_response = data[:]
        self.__new_query_response = True
