"""

"""
from behringer_mixer.component import Component
from behringer_mixer.exceptions import InvalidResponseException
from . import endpoint


class ConsoleLockLockedEndpoint(endpoint.StringEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(max_chars=19)

    @property
    def read_only(self) -> bool:
        """

        :return:
        """
        return True

    def _parse_response(self, response) -> bool:
        """

        :param response:
        :return:
        """
        response = super()._parse_response(response)
        match len(response):
            case 19:
                return True
            case 0:
                return False
            case _:
                raise InvalidResponseException(
                    f"Invalid console lock response: '{response}'", path=self.indexed_path
                )


class ConsoleLockButtonsEndpoint(ConsoleLockLockedEndpoint):
    """

    """
    _index_button_map = {
        0: "HOME",
        1: "EFFECTS",
        2: "METERS",
        3: "ROUTING",
        4: "SETUP",
        5: "LIBRARY",
        6: "UTILITY",
        17: "CLR_SOLO",
        18: "ENCODER_BTN"
    }

    def _parse_response(self, response) -> list:
        """

        :param response:
        :return:
        """
        response = endpoint.StringEndpoint._parse_response(self, response=response)
        match len(response):
            case 19:
                button_list = []
                for index, char in enumerate(response):
                    match char:
                        case "0":
                            continue
                        case "1":
                            if index in self._index_button_map:
                                button_list.append(self._index_button_map[index])
                            else:
                                raise InvalidResponseException(
                                    f"Invalid console lock response: '{response}'",
                                    path=self.indexed_path
                                )
                        case _:
                            raise InvalidResponseException(
                                f"Invalid console lock response: '{response}'",
                                path=self.indexed_path
                            )
                return button_list
            case 0:
                return []
            case _:
                raise InvalidResponseException(
                    f"Invalid console lock response: '{response}'", path=self.indexed_path
                )


class ControlStatusConsoleLock(Component):
    """

    """
    _components = {}

    _endpoints = {
        "locked": {
            "path": "",
            "class": ConsoleLockLockedEndpoint
        },
        "unlock_buttons": {
            "path": "",
            "class": ConsoleLockButtonsEndpoint
        }
    }


class ControlStatus(Component):
    """

    """
    _components = {
        "console_lock": {
            "path": "/cnslock",
            "class": ControlStatusConsoleLock,
            "aliases":  [ "cnslock" ]
        }
    }

    _endpoints = {
        "selected_channel_strip": {
            "path": "/selidx",
            "class": endpoint.IntEndpoint,
            "min": 1,
            "max": 76,
            "read_offset": 1,
            "aliases": [ "selidx", "channel_strip_selected", "channel_strip_selected_id" ]
        },
        "channel_page": {
            "path": "/pageidx",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 30,
            "aliases": [ "pageidx", "channel_page_id" ]
        },
        "channel_eq_band": {
            "path": "/bandidx",
            "class": endpoint.IntEndpoint,
            "min": 0,  # Documentation says 1 but it's 0 if none is selected!
            "max": 8,
            "aliases": [ "bandidx", "channel_eq_band_id" ]
        },
        "sends_on_fader": {
            "path": "/sof",
            "class": endpoint.IntEndpoint,
            "min": -1,
            "max": 76,
            "aliases": [ "sof", "sends_on_fader_status", "sof_channel", "sends_on_fader_channel" ]
        },
        "send_page": {
            "path": "/sendpage",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "BUS", "MATRIX" ],
            "aliases": [ "sendpage" ]
        },
        "home_page_tab": {
            "path": "/chsetuptab",
            "class": endpoint.IntMappingEndpoint,
            "int_mapping": {
                0: "NONE",
                1: "OVERVIEW",
                2: "ICON/COLOR",
                3: "NAME",
                4: "TAGS"
            },
            "aliases": [ "chsetuptab" ]
        }
    }


class Control(Component):
    """

    """
    _components = {
        "status": {
            "path": "/$stat",
            "class": ControlStatus,
            "aliases": [ "stat" ]
        }
    }

    _endpoints = {}
