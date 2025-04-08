"""

"""
from copy import deepcopy

from behringer_mixer.component import Component
from behringer_mixer.exceptions import InvalidResponseException
from . import endpoint


class LockedEndpoint(endpoint.StringEndpoint):
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


class ButtonsEndpoint(LockedEndpoint):
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


class ConsoleLock(Component):
    """

    """
    _components = {}

    _endpoints = {
        "locked": {
            "path": "",
            "class": LockedEndpoint
        },
        "unlock_buttons": {
            "path": "",
            "class": ButtonsEndpoint
        }
    }


class Status(Component):
    """

    """
    _components = {
        "console_lock": {
            "path": "/cnslock",
            "class": ConsoleLock,
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
            "aliases": ["chsetuptab"]
        }
    }


class ButtonLightsConfig(Component):
    """

    """
    _components = {}

    _endpoints = {
        "backlight_intensity": {
            "path": "/btns",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": ["btns", "backlight", "backlight_brightness"]
        },
        "leds": {
            "path": "/leds",
            "class": endpoint.IntEndpoint,
            "min": 5,
            "max": 100,
            "aliases": [
                "leds_intensity", "led_light_intensity", "leds_brightness", "led_light_brightness"
            ]
        }
    }


class ChannelLCDConfig(Component):
    """

    """
    _components = {}

    _endpoints = {
        "backlight_intensity": {
            "path": "s",
            "class": endpoint.IntEndpoint,
            "min": 5,
            "max": 100,
            "aliases": [
                "chlcds", "backlight", "backlight_brightness", "channel_lcd_intensity", "channel_lcd_brightness",
                "intensity", "brightness"
            ]
        },
        "contrast": {
            "path": "ctr",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": ["ctr"]
        }
    }


class LightsConfig(Component):
    """

    """
    _components = {
        "buttons": {
            "path": "",
            "class": ButtonLightsConfig,
            "aliases": ["button"]
        },
        "channel_lcd": {
            "path": "/chlcd",
            "class": ChannelLCDConfig,
            "aliases": ["lcd"]
        }
    }

    _endpoints = {
        "meters": {
            "path": "/meters",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": ["meters_intensity"]
        },
        "scribble_lights": {
            "path": "/rgbleds",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": ["rgbleds", "rgb_leds", "color_leds", "color_led_intensity"]
        },
        "channel_strip": {
            "path": "/chedit",
            "class": endpoint.IntEndpoint,
            "min": 5,
            "max": 100,
            "aliases": ["chedit", "channel_strip_intensity", "channel_strip_brightness"]
        },
        "touchscreen": {
            "path": "/main",
            "class": endpoint.IntEndpoint,
            "min": 5,
            "max": 100,
            "aliases": ["main", "touchscreen_intensity", "touchscreen_brightness"]
        },
        "under_console": {
            "path": "/glow",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [
                "glow", "glow_intensity", "glow_brightness", "under_console_intensity", "under_console_brightness"
            ]
        },
        "patch_panel": {
            "path": "/patch",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [
                "patch", "patch_intensity", "patch_brightness", "panel", "panel_intensity", "panel_brightness",
                "patch_panel_intensity", "patch_panel_brightness"
            ]
        },
        "lamp": {
            "path": "/lamp",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": ["lamp_intensity", "lamp_brightness"]
        }
    }


class RTAHomeConfig(Component):
    """

    """
    _components = {}

    _endpoints = {
        "size": {
            "path": "disp",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["OFF", "1/3", "FULL"],
            "aliases": ["disp", "mode"]
        },
        "color": {
            "path": "col",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "RD25", "RD50", "RD75", "AM25", "AM50", "AM75", "BL25", "BL50", "BL75"
            ],
            "aliases": ["col", "colour"]
        },
        "tap": {
            "path": "tap",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["IN", "EQ", "POST"]
        }
    }


class RTAEQConfig(RTAHomeConfig):
    """

    """
    _endpoints = deepcopy(RTAHomeConfig._endpoints)
    _endpoints["size"].update({
        "path": "/eqdisp",
        "valid_strings": ["OFF", "1/4", "1/3", "1/2", "OVL/", "OVL"]
    })
    _endpoints["color"].update({
        "path": "/eqcol",
    })
    _endpoints["tap"].update({
        "path": "/cheqtap",
        "valid_strings": ["PRE", "POST"]
    })


class RTAConfig(Component):
    """

    """
    _components = {
        "home": {
            "path": "/home",
            "class": RTAHomeConfig
        },
        "eq": {
            "path": "",
            "class": RTAEQConfig
        }
    }

    _endpoints = {
        "filter_tap": {
            "path": "/chflttap",
            "class": endpoint.PrePostEndpoint,
            "aliases": ["chflttap"]
        }
    }


class Config(Component):
    """

    """
    _components = {
        "lights": {
            "path": "/lights",
            "class": LightsConfig
        },
        "rta": {
            "path": "/rta",
            "class": RTAConfig
        }
    }

    _endpoints = {}


class Control(Component):
    """

    """
    _components = {
        "status": {
            "path": "/$stat",
            "class": Status,
            "aliases": ["stat"]
        },
        "config": {
            "path": "/cfg",
            "class": Config,
            "aliases": ["cfg", "configuration"]
        }
    }

    _endpoints = {}
