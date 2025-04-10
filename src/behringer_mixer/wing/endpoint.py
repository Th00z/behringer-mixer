"""

"""
import re

from typing import List, Dict, Type
from datetime import datetime
from enum import Enum
from copy import deepcopy

from netaddr import IPAddress

from behringer_mixer.client import Client
from behringer_mixer.endpoint import Endpoint, ComplexEndpoint
from behringer_mixer.exceptions import InvalidResponseException, IllegalQueryException
from behringer_mixer.types import dB, DelayUnit, Meters, Feet, Milliseconds, Samples

from .utils import Color, Icon


class StringEndpoint(Endpoint):
    """

    """
    _max_chars: int | None

    def _init(self, max_chars: int | None = None):
        """

        :param max_chars:
        :return:
        """
        self._max_chars = max_chars

    def _parse_response(self, response) -> str:
        """

        :param response:
        :return:
        """
        if not isinstance(response, tuple):
            raise InvalidResponseException("OSC-Client returned a non-tuple!", path=self.path)
        if not isinstance(response[0], str):
            raise InvalidResponseException("OSC-Client did not return a string!", path=self.path)
        if self._max_chars is not None:
            if len(response[0]) > self._max_chars:
                raise InvalidResponseException(
                    f"String too long: '{response[0]}' ({len(response[0])} chars)!", path=self.path
                )
        return response[0]

    def _parse_parameter(self, parameter: str) -> str:
        """

        :param parameter:
        :return:
        """
        if not isinstance(parameter, str):
            parameter = str(parameter)
        if len(parameter) > self._max_chars:
            raise IllegalQueryException(
                f"String length too long! Allowed: {self._max_chars} chars; "
                f"Received: {len(parameter)} chars.", path=self.path
            )
        return parameter


class StringEnumEndpoint(StringEndpoint):
    """

    """
    _valid_strings: List[str]
    _valid_read_strings: List[str]

    def _init(
            self, valid_strings: List[str], valid_read_strings: List[str] | None = None
    ):
        """

        :param valid_strings:
        :param valid_read_strings:
        :return:
        """
        self._valid_strings = valid_strings
        if valid_read_strings is not None:
            self._valid_read_strings = valid_read_strings
        else:
            self._valid_read_strings = valid_strings
        max_chars = 0
        for valid_string in self._valid_strings + self._valid_read_strings:
            if len(valid_string) > max_chars:
                max_chars = len(valid_string)
        super()._init(max_chars=128)

    def _parse_response(self, response) -> str:
        """

        :param response:
        :return:
        """
        response_string = super()._parse_response(response=response)
        if response_string not in self._valid_read_strings:
            raise InvalidResponseException(
                f"'{response_string}' is not a valid value for endpoint! "
                f"Valid values: {', '.join(self._valid_read_strings)}",
                path=self.path
            )
        return response_string

    def _parse_parameter(self, parameter: str) -> str:
        """

        :param parameter:
        :return:
        """
        parameter = super()._parse_parameter(parameter=parameter)
        if parameter not in self._valid_strings:
            raise IllegalQueryException(
                f"'{parameter}' is not a valid value for endpoint! "
                f"Valid values: {', '.join(self._valid_strings)}",
                path=self.path
            )
        return parameter


class StringMappingEndpoint(StringEnumEndpoint):
    """

    """
    _string_mapping: dict
    _allow_mapped_value_access: bool

    def _init(self, string_mapping: dict, allow_mapped_value_access: bool = True):
        """
        :return:
        """
        self._string_mapping = string_mapping
        self._allow_mapped_value_access = allow_mapped_value_access
        super()._init(valid_strings=list(self._string_mapping.keys()))

    def _parse_response(self, response):
        """

        :param response:
        :return:
        """
        internal_name = super()._parse_response(response=response)
        name = self._string_mapping[internal_name]
        if isinstance(name, list):
            return name[0]
        return name

    def _parse_parameter(self, parameter) -> str:
        """

        :param parameter:
        :return:
        """
        try:
            return super()._parse_parameter(parameter=self.reverse_map(value=parameter))
        except IllegalQueryException as e:
            if self._allow_mapped_value_access and "is not a valid value for endpoint" in str(e):
                try:
                    return super()._parse_parameter(parameter=parameter)
                except IllegalQueryException as e2:
                    if "is not a valid value for endpoint" in str(e2):
                        valid_strings = []
                        for internal_name, name in self._string_mapping.items():
                            valid_strings.append(f"'{str(name)}'/'{internal_name}'")
                        raise IllegalQueryException(
                            f"'{parameter}' is not a valid value for endpoint!"
                            f"Valid values: {', '.join(valid_strings)}"
                        ) from e
            else:
                raise e

    def reverse_map(self, value):
        """

        :param value:
        :return:
        """
        for internal_name, name in self._string_mapping.items():
            if isinstance(name, list):
                if value in name:
                    return internal_name
            if value == name:
                return internal_name
        raise IllegalQueryException(
            f"'{str(value)}' is not a valid value for endpoint! "
            f"Valid values: {', '.join(self._string_mapping.values())}",
            path=self.path
        )


class PrePostEndpoint(StringEnumEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(valid_strings=["PRE", "POST"])


class InputModeEndpoint(StringEnumEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(valid_strings=[ "M", "ST", "M/S" ])


class TriTupleEndpoint(Endpoint):
    """

    """
    def _parse_response(self, response) -> tuple:
        if not isinstance(response, tuple):
            raise InvalidResponseException("OSC-Client returned a non-tuple!", path=self.path)
        if len(response) < 3:
            raise InvalidResponseException(
                "OSC-Client returned a tuple with not enough values to unpack!", path=self.path
            )
        return response


class IntEndpoint(TriTupleEndpoint):
    """

    """
    _min: int | None
    _read_min: int | None
    _max: int | None
    _read_max: int | None
    _values: Type[Enum] | Dict[int, str] | None
    _read_offset: int
    _write_offset: int

    def _init(self, read_offset: int = 0, write_offset: int = 0, min: int | None = None,
              read_min: int | None = None, max: int | None = None, read_max: int | None = None,
              values: Type[Enum] | List[int] | None = None):
        """

        :param min:
        :param read_min:
        :param max:
        :param read_max:
        :return:
        """
        self._read_offset = read_offset
        self._write_offset = write_offset
        self._values = values

        self._min = min if min is not None else None
        self._max = max if max is not None else None

        self._read_min = read_min if read_min is not None else min
        self._read_max = read_max if read_max is not None else max

    def _parse_response(self, response) -> int:
        """

        :param response:
        :return:
        """
        response = super()._parse_response(response=response)
        if not isinstance(response[2], int):
            raise InvalidResponseException(
                "OSC-Client did not return an integer!", path=self.path
            )
        response = response[2] + self._read_offset
        if self._values is not None:
            if isinstance(self._values, Enum):
                if response not in set(item.value for item in self._values):
                    raise InvalidResponseException(
                        f"Value Out of Bounds for Endpoint: {response} not in "
                        f"{self._values.__name__}.", path=self.path
                    )
            elif isinstance(self._values, list):
                if response not in self._values:
                    raise InvalidResponseException(
                        f"Value Out of Bounds for Endpoint: {response} not in "
                        f"[{', '.join([str(i) for i in self._values])}].", path=self.path
                    )
        if self._read_min is not None:
            if response < self._read_min:
                raise InvalidResponseException(
                    f"Value Out of Bounds for Endpoint: {response} < {self._read_min}.",
                    path=self.path
                )
        if self._read_max is not None:
            if response > self._read_max:
                raise InvalidResponseException(
                    f"Value Out of Bounds for Endpoint: {response} > {self._read_max}.",
                    path=self.path
                )
        return response

    def _parse_parameter(self, parameter: int) -> str:
        """

        :param parameter:
        :return:
        """
        if not isinstance(parameter, int):
            raise IllegalQueryException(
                "Trying to write non-integer value to int endpoint.", path=self.path
            )
        if self._values is not None:
            if isinstance(self._values, Enum):
                if parameter not in set(item.value for item in self._values):
                    raise IllegalQueryException(
                        f"Value Out of Bounds for Endpoint: {parameter} not in "
                        f"{self._values.__name__}.",
                        path=self.path
                    )
            elif isinstance(self._values, list):
                if parameter not in self._values:
                    raise IllegalQueryException(
                        f"Value Out of Bounds for Endpoint: {parameter} not in "
                        f"[{', '.join([str(i) for i in self._values])}].", path=self.path
                    )
        if self._min is not None:
            if parameter < self._min:
                raise IllegalQueryException(
                    f"Value Out of Bounds for Endpoint: {parameter} < {self._min}.", path=self.path
                )
        if self._max is not None:
            if parameter > self._max:
                raise IllegalQueryException(
                    f"Value Out of Bounds for Endpoint: {parameter} > {self._max}.", path=self.path
                )
        return parameter + self._write_offset


class IntMappingEndpoint(IntEndpoint):
    """

    """
    _int_mapping: dict

    def _init(self, int_mapping: dict, read_offset: int = 0):
        """
        :return:
        """
        self._int_mapping = int_mapping
        super()._init(values=list(self._int_mapping.keys()), read_offset=read_offset)

    def _parse_response(self, response) -> str:
        """

        :param response:
        :return:
        """
        index = super()._parse_response(response=response)
        name = self._int_mapping[index]
        if isinstance(name, list):
            return name[0]
        return name

    def _parse_parameter(self, parameter: int | str) -> str:
        """

        :param parameter:
        :return:
        """
        try:
            return super()._parse_parameter(parameter=self.reverse_map(value=parameter))
        except IllegalQueryException as e:
            if "is not a valid value for endpoint" in str(e):
                try:
                    return super()._parse_parameter(parameter=parameter)
                except IllegalQueryException as e2:
                    if "is not a valid value for endpoint" in str(e2):
                        valid_values = []
                        for index, name in self._int_mapping.items():
                            valid_values.append(f"'{str(name)}'/'{index}'")
                        raise IllegalQueryException(
                            f"'{parameter}' is not a valid value for endpoint!"
                            f"Valid values: {', '.join(valid_values)}"
                        ) from e
            else:
                raise e

    def _reverse_map(self, value):
        """

        :param value:
        :return:
        """
        for index, name in self._int_mapping.items():
            if isinstance(name, list):
                if value in name:
                    return index
            if value == name:
                return index
        raise IllegalQueryException(
            f"'{str(value)}' is not a valid value for endpoint! "
            f"Valid values: {', '.join([str(i) for i in self._int_mapping.values()])}",
            path=self.path
        )


class BoolEndpoint(IntEndpoint):
    """

    """
    __invert: bool
    __name_mapping: Dict[bool, str] | None

    def _init(self, invert: bool = False, name_mapping: Dict[bool, str] | None = None):
        """

        :return:
        """
        self.__invert = invert
        if name_mapping is not None:
            if True not in name_mapping or False not in name_mapping:
                raise QueryException(
                    f"Invalid mapping for bool endpoint: '{name_mapping}'", path=self.path
                )

            self.__name_mapping = name_mapping
        else:
            self.__name_mapping = None

        super()._init(min=0, max=1)

    def _parse_response(self, response) -> str | bool:
        """

        :param response:
        :return:
        """
        response = super()._parse_response(response=response)
        match response:
            case 0:
                return self.__map_response(response=False != self.__invert)
            case 1:
                return self.__map_response(response=True != self.__invert)
            case _:
                raise InvalidResponseException(
                    "OSC-Client returned an integer flag that is neither 0 nor 1!", path=self.path
                )

    def _parse_parameter(self, parameter: str | bool) -> str:
        """

        :param parameter:
        :return:
        """
        parameter = self.__map_parameter(parameter=parameter)
        if not isinstance(parameter, bool):
            raise IllegalQueryException(
                "Trying to write non-bool value to bool endpoint.", path=self.path
            )
        match parameter:
            case False:
                return "0"
            case True:
                return "1"
            case _:
                raise IllegalQueryException(
                    "Somehow parameter is a boolean that is neither True nor False.... What?",
                    path=self.path
                )

    def __map_response(self, response: bool) -> str | bool:
        """

        :param response:
        :return:
        """
        if self.__name_mapping is None:
            return response
        return self.__name_mapping[response]

    def __map_parameter(self, parameter: str | bool) -> bool:
        """

        :param parameter:
        :return:
        """
        if isinstance(parameter, bool) or self.__name_mapping is None:
            return parameter
        for boolval, name in self.__name_mapping.items():
            if parameter == name:
                return boolval
        raise IllegalQueryException(
            f"Invalid value for mapped bool endpoint: '{parameter}'", path=self.path
        )


class FloatEndpoint(TriTupleEndpoint):
    """

    """
    _min: float | None
    _max: float | None
    _valid_values: List[float] | None

    def _init(
            self, min: float | None = None, max: float | None = None,
            valid_values: List[float] | None = None
    ):
        """

        :param min:
        :param max:
        :param valid_values
        :return:
        """
        self._min = min
        self._max = max
        self._valid_values = valid_values

    def _parse_response(self, response) -> float:
        """

        :param response:
        :return:
        """
        response = super()._parse_response(response=response)
        if not isinstance(response[2], float):
            raise InvalidResponseException(
                "OSC-Client did not return a float value!", path=self.path
            )
        if self._min is not None:
            # The values yielded by the console sometimes slightly break their boundaries
            # probably due to rounding errors based in conversion.
            if response[2] < self._min - 0.01:
                raise InvalidResponseException(
                    f"Value Out of Bounds for Endpoint: {response[2]} < {self._min}.",
                    path=self.path
                )
        if self._max is not None:
            # The values yielded by the console sometimes slightly break their boundaries
            # probably due to rounding errors based in conversion.
            if response[2] > self._max + 0.01:
                raise InvalidResponseException(
                    f"Value Out of Bounds for Endpoint: {response[2]} > {self._max}.",
                    path=self.path
                )
        if self._valid_values is not None:
            if response[2] not in self._valid_values:
                raise InvalidResponseException(
                    f"Value Out of Bounds for Endpoint: "
                    f"{response[2]} not in {self._valid_values_string(self._valid_values)}.",
                    path=self.path
                )
        return response[2]

    def _parse_parameter(self, parameter: float | int) -> str:
        """

        :param parameter:
        :return:
        """
        if isinstance(parameter, int):
            parameter = float(parameter)
        if not isinstance(parameter, float):
            raise IllegalQueryException(
                f"Provided parameter is not a float or integer. Received: {type(parameter)}",
                path=self.path
            )
        if self._min is not None:
            if parameter < self._min:
                raise IllegalQueryException(
                    f"Value Out of Bounds for Endpoint: {parameter} < {self._min}.", path=self.path
                )
        if self._max is not None:
            if parameter > self._max:
                raise IllegalQueryException(
                    f"Value Out of Bounds for Endpoint: {parameter} > {self._max}.", path=self.path
                )
        if self._valid_values is not None:
            if parameter not in self._valid_values:
                raise IllegalQueryException(
                    f"Value Out of Bounds for Endpoint: "
                    f"{parameter} not in {self._valid_values_string(self._valid_values)}.",
                    path=self.path
                )
        return str(parameter)

    @staticmethod
    def _valid_values_string(valid_values: list) -> str:
        """

        :param valid_values:
        :return:
        """
        str_valid_values = []
        for valid_value in valid_values:
            str_valid_values.append(str(valid_value))
        return f"[{', '.join(str_valid_values)}]"


class StandardKnob(FloatEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(min=0.0, max=10.0)


class FaderEndpoint(FloatEndpoint):
    """

    """
    def _parse_response(self, response) -> dB:
        """

        :param response:
        :return:
        """
        response = super()._parse_response(response=response)
        return dB(response)

    def _parse_parameter(self, parameter: dB | float | int) -> str:
        if isinstance(parameter, dB):
            if not -90.0 < float(parameter)  <= 10.0:
                raise IllegalQueryException(
                    f"dB value out of bounds for fader. Range is: ] -90.0 : 10.0 ] "
                    f"Received: '{parameter}'.", path=self.path
                )
            return str(float(parameter))
        if isinstance(parameter, float):
            if not 0.0 <= parameter <= 1.0:
                raise IllegalQueryException(
                    f"Fader value out of bounds for fader. Range is: [ 0.0 : 1.0 ] "
                    f"Received: '{parameter}'.", path=self.path
                )
            return str(float(dB.from_fader(parameter)))
        if isinstance(parameter, int):
            if not -90 < parameter <= 10:
                raise IllegalQueryException(
                    f"dB value out of bounds for fader. Range is: ] -90.0 : 10.0 ] "
                    f"Received: '{parameter}'.", path=self.path
                )
            return str(float(dB(parameter)))
        raise IllegalQueryException(
            f"Invalid parameter type for fader endpoint. Expected: dB/float/int; "
            f"Received: '{type(parameter)}'", path=self.path
        )


class PercentEndpoint(FloatEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(min=0.0, max=100.0)


class FXLowCutEndpoint(FloatEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(min=20.0, max=400.0)


class FXHighCutEndpoint(FloatEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(min=200.0, max=20000)


class IPv4Endpoint(ComplexEndpoint):
    """

    """
    def __init__(
            self, client: Client, path: str, index: str | int | None = None,
            index_format_string: str = "/{index}", read_only: bool = True
    ):
        """

        :param client:
        :param path:
        :param ip_address:
        :param index:
        :param index_format_string:
        """
        endpoints = {
            "0": {
                "path": "0",
                "class": IntEndpoint,
                "min": 0,
                "max": 255
            },
            "1": {
                "path": "1",
                "class": IntEndpoint,
                "min": 0,
                "max": 255
            },
            "2": {
                "path": "2",
                "class": IntEndpoint,
                "min": 0,
                "max": 255
            },
            "3": {
                "path": "3",
                "class": IntEndpoint,
                "min": 0,
                "max": 255
            },
        }
        super().__init__(
            client=client, path=path, endpoints=endpoints, index=index,
            index_format_string=index_format_string, read_only=read_only
        )

    def _parse_responses(self, responses: dict) -> IPAddress:
        """

        :param self:
        :param responses:
        :return:
        """
        return IPAddress(f"{responses['0']}.{responses['1']}.{responses['2']}.{responses['3']}")

    def _unpack_parameter(self, parameter: IPAddress | str) -> dict:
        """

        :param parameter:
        :return:
        """
        if not isinstance(parameter, IPAddress):
            if isinstance(parameter, str):
                parameter = IPAddress(parameter)
            else:
                raise IllegalQueryException("Non-IP-Address provided as parameter!")
        if parameter.version != 4:
            raise IllegalQueryException("Only IPv4-Addresses are supported!")
        return {
            "0": parameter.words[0],
            "1": parameter.words[1],
            "2": parameter.words[2],
            "3": parameter.words[3],
        }


class DatetimeEndpoint(ComplexEndpoint):
    """

    """
    _datetime_format: str

    def __init__(
            self, client: Client, path: str, date_endpoint: dict, time_endpoint: dict,
            datetime_format: str = "%Y-%m-%d %H:%M:%S", read_only: bool = True,
            index: str | int | None = None, index_format_string: str = "/{index}"
    ):
        """

        :param date_endpoint:
        :param time_endpoint:
        :param datetime_format:
        """
        super().__init__(
            client=client, path=path,
            endpoints={ "date": date_endpoint, "time": time_endpoint },
            index=index, index_format_string=index_format_string
        )
        self._datetime_format = datetime_format

    def _parse_responses(self, responses: dict) -> datetime:
        """

        :param responses:
        :return:
        """
        try:
            return datetime.strptime(
                f"{responses['date']} {responses['time']}", self._datetime_format
            )
        except ValueError as e:
            raise InvalidResponseException(
                f"Could not create datetime from OSC-Response: {e}",
                path=f"{self._endpoints['date'].path};{self._endpoints['time'].path}"
            )


class DelayEndpoint(ComplexEndpoint):
    """

    """
    __string_parameter_regex = re.compile(r"(?P<value>\d*\.?\d*)\s*(?P<unit>smp|ms|ft|m)")
    __mode_map: dict =  {
        "M": {
            "class": Meters,
            "min": 0.0,
            "max": 150.0
        },
        "FT": {
            "class": Feet,
            "min": 0.5,
            "max": 500.0
        },
        "MS": {
            "class": Milliseconds,
            "min": 0.5,
            "max": 500.0
        },
        "SMP": {
            "class": Samples,
            "min": 16.0,
            "max": 500.0
        },
    }

    def __init__(
            self, client: Client, path: str, enable_path: str, mode_path: str, value_path: str,
            read_only: bool = True, index: str | int | None = None,
            index_format_string: str = "/{index}"
    ):
        """

        """

        super().__init__(
            client=client, path=path,
            endpoints={
                "enable": {
                    "path": enable_path,
                    "class": BoolEndpoint
                },
                "mode": {
                    "path": mode_path,
                    "class": StringEnumEndpoint,
                    "valid_strings": [ "M", "FT", "MS", "SMP" ]
                },
                "value": {
                    "path": value_path,
                    "class": FloatEndpoint,
                    "min": 0.0,
                    "max": 500.0
                }
            }, read_only=read_only, index=index, index_format_string=index_format_string
        )

    def _parse_responses(self, responses: dict) -> DelayUnit | bool:
        """

        :param responses:
        :return:
        """
        if not responses["enable"]:
            return False
        if responses["mode"] not in self.__mode_map:
            raise InvalidResponseException(
                f"Invalid Mode for Input Delay: '{responses['mode']}'; "
                f"Valid Modes: [ {', '.join(self.__mode_map.keys())} ]", path=self._path
            )
        mode = self.__mode_map[responses["mode"]]
        value = responses["value"]
        if value < mode["min"]:
            raise InvalidResponseException(
                f"Value out of Bounds for {mode['class'].__name__}: {value} < {mode['min']}",
                path=self._path
            )
        if value > mode["max"]:
            raise InvalidResponseException(
                f"Value out of Bounds for {mode['class'].__name__}: {value} > {mode['max']}",
                path=self._path
            )
        return mode["class"](value)

    def _unpack_parameter(self, parameter: DelayUnit | float | str | bool) -> dict:
        """

        :param parameter:
        :return:
        """
        if not isinstance(parameter, DelayUnit):
            match parameter:
                case parameter if isinstance(parameter, float):
                    parameter = Meters(parameter)
                case parameter if isinstance(parameter, str):
                    parameter = self.__string_to_delay_unit(parameter=parameter)
                case parameter if isinstance(parameter, bool):
                    return { "enable": parameter }
                case _:
                    raise IllegalQueryException(
                        f"Invalid parameter type for Input Delay: {type(parameter)}",
                        path=self._path
                    )
        return {
            "enable": True,
            "mode": parameter.unit.upper(),
            "value": float(parameter)
        }

    def __string_to_delay_unit(self, parameter: str) -> DelayUnit:
        """

        :param parameter:
        :return:
        """
        param_match = self.__string_parameter_regex.match(parameter)
        if param_match is None:
            raise IllegalQueryException(
                f"Invalid string value for Input Delay: '{parameter}'", path=self._path
            )
        match param_match["unit"]:
            case "m":
                return Meters(float(param_match["value"]))
            case "ft":
                return Feet(float(param_match["value"]))
            case "ms":
                return Milliseconds(float(param_match["value"]))
            case "smp":
                return Samples(float(param_match["value"]))
            case _:
                raise IllegalQueryException(
                    f"Invalid Mode for Input Delay: '{param_match['unit'].upper()}'",
                    path=self._path
                )



class SourceSoloGroupEndpoint(IntMappingEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(
            int_mapping={
                1: "LOCAL IN",
                2: "AUX IN",
                3: "AES50 A",
                4: "AES50 B",
                5: "AES50 C",
                6: "ST CONNECT",
                7: "USB AUDIO",
                8: "CARD",
                9: "MODULE",
                10: "USB PLAYER",
                11: "AES/EBU IN",
                12: "USER SIGNAL",
                13: "OSCILLATOR"
            },
            read_offset=1
        )

class SourceGroupEndpoint(StringMappingEndpoint):
    """

    """
    _source_group_map = {
        "OFF": "OFF",
        "LCL": "LOCAL IN",
        "AUX": "AUX IN",
        "A": "AES50 A",
        "B": "AES50 B",
        "C": "AES50 C",
        "SC": "ST CONNECT",
        "USB": "USB AUDIO",
        "CRD": "CARD",
        "MOD": "MODULE",
        "PLAY": "USB PLAYER",
        "AES": "AES/EBU IN",
        "USR": "USER SIGNAL",
        "OSC": "OSCILLATOR",
        "BUS": "BUS",
        "MAIN": "MAIN",
        "MTX": "MATRIX",
    }

    def _init(self, only_external: bool = False):
        """

        :return:
        """
        if only_external:
            source_group_map = self._source_group_map.copy()
            del source_group_map["USR"]
            del source_group_map["OSC"]
            del source_group_map["BUS"]
            del source_group_map["MAIN"]
            del source_group_map["MTX"]
        super()._init(string_mapping=self._source_group_map)

class OutSourceGroupEndpoint(SourceGroupEndpoint):
    """

    """
    _source_group_map = deepcopy(SourceGroupEndpoint._source_group_map)
    _source_group_map.update({
        "SEND": "SEND",
        "MON": "MONITOR"
    })


#class Soul9000ChannelCompressorRatioEndpoint(TriTupleEndpoint):
#    """
#
#    """
#    def _parse_response(self, response) -> tuple:
#        """
#
#        :param response:
#        :return:
#        """
#        response = super()._parse_response(response=response)
#        return self._value_map[response[0]]
#
#    def _parse_parameter(self, parameter: str) -> str:
#        """
#
#        :param parameter:
#        :return:
#        """
#        if not isinstance(parameter, str):
#            raise IllegalQueryException(
#                f"Parameter is not of type string! Received: '{type(parameter)}'", path=self.path
#            )
#        return self.reverse_map(value=parameter)
#
#    def reverse_map(self, value: str):
#        """
#
#        :param value:
#        :return:
#        """
#        reverse_mapping = { value: key for key, value in self._value_map.items() }
#        if value not in reverse_mapping:
#            raise IllegalQueryException(
#                f"'{value}' is not a valid value for endpoint! "
#                f"Valid values: {', '.join(self._value_map.values())}",
#                path=self.path
#            )
#        return reverse_mapping[value]
