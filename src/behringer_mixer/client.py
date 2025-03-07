"""
Client module for the connection between the wrapper objects and the actual mixing desks.
"""
import asyncio
import logging
import time

from typing import final, Optional, Callable, Dict, Any, List
from abc import ABC, abstractmethod

from netaddr import IPv4Address
from jsonschema import validate, ValidationError
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_message_builder import OscMessageBuilder
from pythonosc.osc_server import AsyncIOOSCUDPServer

from .exceptions import NoResponseException
from . import utils


class Client(ABC):
    """

    """
    _mixer_host: str | IPv4Address
    _mixer_port: int

    _logger: logging.Logger


    def __init__(self, mixer_host: str | IPv4Address, mixer_port: int):
        """

        :param mixer_host:
        :param mixer_port:
        """
        self._mixer_host = mixer_host
        self._mixer_port = mixer_port
        self._logger = logging.getLogger("behringer-mixer :: Client")

    @final
    async def initialize(self, validation_endpoint: Endpoint) -> bool:
        """

        :param validation_endpoint:
        :return:
        """
        self._initialize_communication()
        self.validate(validation_endpoint=validation_endpoint)

    @abstractmethod
    async def validate(self, validation_endpoint: Endpoint):
        """

        :param validation_endpoint:
        :return:
        """

    @abstractmethod
    async def _initialize_communication(self):
        """

        :return:
        """


class OSCClient(Client):
    """
    Handles the communication with the mixer via the OSC protocol
    """
    __osc_client_server: AsyncIOOSCUDPServer | None
    __query_response_wait_time: float
    __query_response_timeout: float

    __query_response = None
    __last_received_timestamp: float

    def __init__(
            self, mixer_host: str | IPv4Address, mixer_port: int,
            query_response_wait_time: float = 0.002, query_response_timeout: float = 0.5
    ):
        """

        :param mixer_host:
        :param mixer_port:
        :param query_response_wait_time:
        :param query_response_timeout:
        """
        super().__init__(mixer_host=mixer_host, mixer_port=mixer_port)
        self.__query_response_wait_time = query_response_wait_time
        self.__query_response_timeout = query_response_timeout

        self.__osc_client_server = None
        self.__transport = None
        self.__protocol = None

        self.__query_response = None
        self.__last_received_timestamp = 0


        self._logger = logging.getLogger("behringer-mixer :: OSCClient")

    async def _initialize_communication(self):
        """

        :return:
        """
        if not self._osc_client_server:
            dispatcher = Dispatcher()
            dispatcher.set_default_handler(self.__msg_handler)
            self.__osc_client_server = AsyncIOOSCUDPServer(
                ("0.0.0.0", 0), dispatcher, asyncio.get_event_loop()
            )
            self.__transport, self.__protocol = self.__osc_client_server.create_serve_endpoint()
            self.__osc_client_server.register_transport(self.__transport, self.__protocol)


    async def start(self):
        """Startup the server"""
        if not self.server:
            self.server = OSCClientServer(
                (self.ip, self.port), self.msg_handler, asyncio.get_event_loop()
            )
            transport, protocol = await self.server.create_serve_endpoint()
            self.server.register_transport(transport, protocol)
        return await self.validate_connection()

    async def validate_connection(self):
        """Validate connection to the mixer"""
        await self.send("/xinfo")
        await asyncio.sleep(self._CONNECT_TIMEOUT)
        if not self.info_response:
            self.logger.debug(
                "Failed to setup OSC connection to mixer. Please check for correct ip address."
            )
            return False

        self.logger.debug(
            "Successfully connected to %s at %s.",
            {self.info_response[2]},
            {self.info_response[0]},
        )
        return True

    @property
    def query_response(self):
        """Return any OSC responses"""
        if self.__query_response is not None:
            return self.__query_response
        raise NoResponseException

    def __msg_handler(self, addr, *data):
        """Handle callback response"""

        self.logger.debug(f"received: {addr} {data if data else ''}")
        self._last_received = time.time()
        updates = self._update_state(addr, data)
        if addr == "/xinfo":
            self.handle_xinfo(data)
            updates = []
        if self._callback_function:
            for row in updates:
                self._callback_function(row)
        else:
            self._info_response = data[:]

    async def send(self, addr: str, param: Optional[str] = None):
        """Send an OSC message"""
        self.logger.debug(f"sending: {addr} {param if param is not None else ''}")
        self.server.send_message(addr, param)
        self._info_response = None
        await asyncio.sleep(self._delay)

    async def query(self, address):
        """Send an receive the value of an OSC message"""
        await self.send(address)
        return self.info_response

    async def stop(self):
        """Stop the OSC server"""
        self.server.shutdown()
        return True

    def state(self, key=None):
        """Return current mixer state"""
        if key:
            return self._state.get(key)
        return self._state

    async def load_scene(self, scene_number):
        """Load a new scene on the mixer"""
        await self.send(self.cmd_scene_load, scene_number)
        # Because of potential UDP buffer overruns (lots of messages are sent on
        # a scene change), data may be lost
        # therefore we need to wait for the scene change to finish
        # and then update the state to make sure we have everything
        await asyncio.sleep(1)
        await self._load_initial()

    async def reload(self):
        """Reload state"""
        self._state = {}
        await self._load_initial()

    async def _load_initial(self):
        """Load initial state"""
        for address in self._mappings.keys():
            await self.send(address)

    def _update_state(self, address: str, values: List[Any]) -> List[Dict[str, Any]]:
        """Update internal state representation, called when a message is received
        Args:
            address (str): The address to update.
            values (List[Any]): The values to update.

        Returns:
            List[Dict[str, Any]]: A list of updates.
        """
        if address not in self._mappings:
            return []
        address_data = self._mappings.get(address, {})
        state_key = address_data.get("output")
        value = values[0] if len(values) == 1 else values
        updates = []
        if state_key:
            if address_data.get("mapping"):
                value = address_data["mapping"].get(value)
            if address_data.get("data_type", "") == "boolean":
                value = bool(value)
            self._state[state_key] = value
            updates.append({"property": state_key, "value": value})
            for suffix, secondary_data in address_data.get(
                "secondary_output", {}
            ).items():
                secondary_key = state_key + suffix
                new_value = getattr(utils, secondary_data["forward_function"])(
                    value, address_data
                )
                self._state[secondary_key] = new_value
                updates.append({"property": secondary_key, "value": new_value})
        return updates

    async def set_value(self, address: str, value: Any) -> None:
        """Set the value in the mixer

        Args:
            address (str): The address to process.
            value (Any): The value to process.
        """
        address_data = None
        if address in self._secondary_mappings:
            address_data = self._mappings.get(self._secondary_mappings[address])
            for suffix, secondary_data in address_data.get(
                "secondary_output", {}
            ).items():
                if address.endswith(suffix):
                    value = getattr(utils, secondary_data["reverse_function"])(
                        value, address_data
                    )
                    address = address_data.get("output")
                    break
        if not address_data:
            address_data = self._mappings_reverse.get(address) or {}
        if value is False:
            value = 0
        if value is True:
            value = 1
        if address_data.get("mapping"):
            reverse_map = {v: k for k, v in address_data["mapping"].items()}
            value = reverse_map[value]
        if address_data:
            await self.send(address_data["input"], value)
            await self.query(address_data["input"])

    def last_received(self) -> float:
        """Return the timestamp of the last time the module received a message from the mixer.

        Returns:
            float: The timestamp of the last received message.
        """
        return self._last_received

    def subscription_connected(self) -> bool:
        """Return true if the module has received a message from the mixer in the last 15 seconds.

        Returns:
            bool: True if connected, False otherwise.
        """
        return (time.time() - self._last_received) <= 15

    async def subscription_status_register(
        self, callback_function: Callable[[bool], None]
    ) -> bool:
        """Register a callback function that is called each time the status of the subscription changes.

        Args:
            callback_function (Callable[[bool], None]): The callback function to register.

        Returns:
            bool: True if registration is successful.
        """
        self._subscription_status_callback = callback_function
        return True

    def name(self) -> Optional[str]:
        """Return the name of the mixer.

        Returns:
            Optional[str]: The name of the mixer.
        """
        return self._mixer_status.get("name")

    def firmware(self) -> Optional[str]:
        """Return the firmware version of the mixer.

        Returns:
            Optional[str]: The firmware version of the mixer.
        """
        return self._mixer_status.get("firmware")

    def handle_xinfo(self, data: List[Any]) -> None:
        """Handle the return data from xinfo requests.

        Args:
            data (List[Any]): The data received from the xinfo request.
        """
        self._mixer_status = {
            "ip_address": data[0],
            "name": data[1],
            "type": data[2],
            "firmware": data[3],
        }

    def dump_mapping(self) -> List[Dict[str, str]]:
        """Dump the mapping table.

        Returns:
            List[Dict[str, str]]: The dumped mapping table.
        """
        output = []
        for original_path in sorted(self._mappings.keys()):
            output.append(
                {
                    "input": original_path,
                    "output": self._mappings[original_path]["output"],
                }
            )
        return output


class Endpoint(ABC):
    """

    """
    _path: str

    def __init__(self, path: str):
        """

        :param path:
        """
        self._path = path

    @property
    def path(self):
        """

        :return:
        """
        return self._path

    @abstractmethod
    def validate_response(self, response) -> bool:
        """

        :param response:
        :return:
        """


class OSCEndpoint(Endpoint):
    """

    """
    __expected_response_schema: dict

    def validate_response(self, response) -> bool:
        """

        :param response:
        :return:
        """
        try:
            validate(response, self.__expected_response_schema)
            return True
        except ValidationError:
            return False
