"""

"""
from copy import deepcopy

from behringer_mixer.component import Component
from behringer_mixer.exceptions import InvalidResponseException
from . import endpoint


class LockLockedEndpoint(endpoint.StringEndpoint):
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


class LockButtonsEndpoint(LockedEndpoint):
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


class LayerSelectEndpoint(endpoint.IntMappingEndpoint):
    """

    """
    _writable: dict
    _readable: dict

    def _init(self, writable: dict, readable: dict, read_offset: int = 0):
        """

        :param writable:
        :param readable:
        :return:
        """
        self._writable = writable
        self._readable = readable
        super()._init(int_mapping=writable | readable, read_offset=read_offset)

    def _reverse_map(self, value):
        """

        :param value:
        :return:
        """
        for index, name in self._writable.items():
            if isinstance(name, list):
                if value in name:
                    return index
            if value == name:
                return index
        raise IllegalQueryException(
            f"'{str(value)}' is not a valid writable value for endpoint! "
            f"Valid values: {', '.join([str(i) for i in self._writable.values()])}",
            path=self.path
        )


class ConsoleLock(Component):
    """

    """
    _components = {}

    _endpoints = {
        "locked": {
            "path": "",
            "class": LockLockedEndpoint
        },
        "unlock_buttons": {
            "path": "",
            "class": LockButtonsEndpoint
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


class UserLayerLinkConfig(Component):
    """

    """
    _components = {}

    _endpoints = {
        "left_center": {
            "path": "l",
            "class": endpoint.BoolEndpoint,
            "aliases": ["l", "layerlinkl", "lc", "l_c"]
        },
        "center_right": {
            "path": "r",
            "class": endpoint.BoolEndpoint,
            "aliases": ["r", "layerlinkr", "cr", "c_r"]
        }
    }


class ChannelAutoSelectConfig(Component):
    """

    """
    _components = {}

    _endpoints = {
        "left": {
            "path": "L",
            "class": endpoint.BoolEndpoint,
            "aliases": ["l", "autosel_l"]
        },
        "center": {
            "path": "C",
            "class": endpoint.BoolEndpoint,
            "aliases": ["c", "autosel_c"]
        },
        "right": {
            "path": "R",
            "class": endpoint.BoolEndpoint,
            "aliases": ["r", "autosel_r"]
        }
    }


class SOFConfig(Component):
    """

    """
    _components = {}

    _endpoints = {
        "right_section_sends_on_fader": {
            "path": "fdr",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "L/C": False,
                "ALL": True
            },
            "aliases": ["right_section_sof"]
        },
        "faders": {
            "path": "fdr",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["L/C", "ALL"],
            "aliases": ["fdr","soffdr","sends_on_fader_faders"]
        },
        "sof_button": {
            "path": "button",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["AUTO", "ON", "FLASH"],
            "aliases": [
                "button", "sofbutton", "button_function", "button_mode", "sof_button_function",
                "sof_button_mode", "sends_on_fader_button", "sends_on_fader_button_function",
                "sends_on_fader_button_mode"
            ]
        },
        "show_sof_frame": {
            "path": "frame",
            "class": endpoint.BoolEndpoint,
            "aliases": [
                "frame", "sofframe", "sof_frame", "show_frame", "sends_on_fader_frame",
                "show_sends_on_fader_frame"
            ]
        },
        "alternative_sof_mode": {
            "path": "mode",
            "class": endpoint.BoolEndpoint,
            "aliases": ["mode", "sofmode", "sof_mode", "alternative_sends_on_fader_mode"]
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
        },
        "user_layer_link": {
            "path": "/layerlink",
            "class": UserLayerLinkConfig,
            "aliases": ["layerlink", "layer_link"]
        },
        "sends_on_fader": {
            "path": "/sof",
            "class": SOFConfig,
            "aliases": ["sof"]
        }
    }

    _endpoints = {
        "mutegroup_sip_override": {
            # The documentation falsely states that the path is /$globals/muteovr, but it is
            # /$ctl/cfg/muteovr
            "path": "/muteovr",
            "class": endpoint.BoolEndpoint,
            "aliases": ["muteovr", "mutegroup_override"]
        },
        "exclusive_solo": {
            "path": "/soloexcl",
            "class": endpoint.BoolEndpoint,
            "aliases": ["soloexcl", "solo_exclusive"]
        },
        "select_follows_solo": {
            "path": "/selfsolo",
            "class": endpoint.BoolEndpoint,
            "aliases": ["selfsolo"]
        },
        "solo_follows_select": {
            "path": "/solofsel",
            "class": endpoint.BoolEndpoint,
            "aliases": ["solofsel"]
        },
        "bus_sof_activates_solo": {
            "path": "/sof2solo",
            "class": endpoint.BoolEndpoint,
            "aliases": [
                "sof2solo", "bus_sof_spill_activates_solo", "bus_sends_on_fader_activates_solo",
                "bus_sends_on_fader_spill_activates_solo"
            ]
        },
        "screen_follows_ch_strip": {
            "path": "/autoview",
            "class": endpoint.BoolEndpoint,
            "aliases": ["autoview", "screen_follows_channel_strip"]
        },
        "ch_strip_touch_select": {
            "path": "/csctouch",
            "class": endpoint.BoolEndpoint,
            "aliases": ["csctouch", "channel_strip_touch_select"]
        },
        "ch_autoselect": {
            "variants": {
                "compact": {
                    "path": "/autosel_CMPCT",
                    "class": endpoint.BoolEndpoint,
                    "aliases": [
                        "autosel", "channel_autoselect", "autoselect", "autosel_cmpct",
                        "ch_autoselect_cmpct", "channel_autoselect_compact",
                        "channel_autoselect_compact_layer"
                    ]
                },
                "rack": {
                    "path": "/autosel_RCK",
                    "class": endpoint.BoolEndpoint,
                    "aliases": [
                        "autosel", "channel_autoselect", "autoselect", "autosel_rck",
                        "ch_autoselect_rck", "channel_autoselect_rack",
                        "channel_autoselect_rack_layer"
                    ]
                },
                "ext": {
                    "path": "/autosel_EXT",
                    "class": endpoint.BoolEndpoint,
                    "aliases": [
                        "autosel", "channel_autoselect", "autoselect", "autosel_ext",
                        "ch_autoselect_ext", "channel_autoselect_ext",
                        "channel_autoselect_ext_layer"
                    ]
                },
                "virtual": {
                    "path": "/autosel_VRT",
                    "class": endpoint.BoolEndpoint,
                    "aliases": [
                        "autosel", "channel_autoselect", "autoselect", "autosel_vrt",
                        "ch_autoselect_vrt", "channel_autoselect_virtual",
                        "channel_autoselect_virtual_layer"
                    ]
                }
            }
        },
        "full_fader_paging": {
            "path": "/fdrbanking",
            "class": endpoint.BoolEndpoint,
            "aliases": ["fdrbanking", "fader_banking"]
        },
        "sel_dbl_click": {
            "path": "/seldblclick",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["OFF", "HOME", "BUSFX"],
            "aliases": ["seldblclick", "select_double_click", "select_double_click_action"]
        },
        "use_f1_f3_as_custom_controls": {
            "path": "/usrmode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "BUS": False,
                "CC": True
            },
            "aliases": ["use_f1_to_f3_as_custom_controls"]
        },
        "use_f1_f3_as_bus_or_custom_control": {
            "path": "/usrmode",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["BUS", "CC"],
            "aliases": ["usrmode", "use_f1_to_f3_as_bus_or_custom_control"]
        },
        "dca_spill": {
            "path": "/dcaspill",
            "class": endpoint.BoolEndpoint,
            "aliases": ["dcaspill"]
        },
        "show_fader_value_on_scribble": {
            "path": "/showfdr",
            "class": endpoint.BoolEndpoint,
            "aliases": ["showfdr"]
        }
    }


class FullsizeConfig(Config):
    """

    """
    _components = deepcopy(Config._components)
    _components.update({
        "ch_autoselect": {
            "path": "/autosel_",
            "class": ChannelAutoSelectConfig,
            "aliases": ["autosel", "channel_autoselect", "autoselect"]
        }
    })


class CompactConfig(Config):
    """
    Though only physically (and UI-wise) existing on the compact variant these endpoints are
    for some reason available on the fullsize, too, and I'm assuming the same goes for the other
    variants. It also takes values. However, as this is not relevant for any other console
    than the compact I decided to omit these endpoints for all other variants.
    If there's a valid use case for them being there for the other variants, please let me know.
    """
    _endpoints = deepcopy(Config._endpoints)
    _endpoints.update({
        "main_fader": {
            "variants": {
                "compact": {
                    "path": "/mfdr",
                    "class": endpoint.StringEnumEndpoint,
                    "valid_strings": [
                        "OFF", "MAIN.1", "MAIN.2", "MAIN.3", "MAIN.4", "MTX.1", "MTX.2", "MTX.3",
                        "MTX.4", "MTX.5", "MTX.6", "MTX.7", "MTX.8", "DCA.1", "DCA.2", "DCA.3",
                        "DCA.4", "DCA.5", "DCA.6", "DCA.7", "DCA.8", "DCA.9", "DCA.11", "DCA.12",
                        "DCA.13", "DCA.14", "DCA.15", "DCA.16"
                    ]
                }
            }
        },
        "custom_button_operation_mode": {
            "path": "/cscmode",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["BUS", "DCA", "MAIN", "USER"],
            "aliases": [
                "cscmode", "button_mode", "button_operation_mode", "csc_mode", "csc_operation_mode"
            ]
        },
        "bus_spill": {
            "path": "/busspill",
            "class": endpoint.BoolEndpoint,
            "aliases": ["busspill"]
        },
        "main_spill": {
            "path": "/mainspill",
            "class": endpoint.BoolEndpoint,
            "aliases": ["mainspill"]
        },
        "matrix_spill": {
            "path": "/mtxspill",
            "class": endpoint.BoolEndpoint,
            "aliases": ["mtxspill", "mtx_spill"]
        },
        "user_custom_control_buttons-on_dca_buttons": {
            "path": "/dcacc",
            "class": endpoint.BoolEndpoint,
            "aliases": ["dcacc", "dca_cc"]
        }
    })


class RackConfig(Config):
    """
    Though only physically (and UI-wise) existing on the rack variant this endpoint is for some
    reason available on the fullsize, too, and I'm assuming the same goes for the other variants.
    It also takes values. However, as this is not relevant for any other console than the rack
    I decided to omit this endpoint for all other variants. If there's a valid use case for it
    being there for the other variants, please let me know.
    """
    _endpoints = deepcopy(Config._endpoints)
    _endpoints.update({
        "custom_control_section": {
            "path": "/rackmode",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["CH", "MGRP", "CC", "USB", "SD-A", "SD-B"],
            "aliases": [
                "rackmode", "cc_mode", "cc_operation_mode", "custom_controls",
                "custom_controls_mode", "custom_controls_operation_mode",
                "custom_control_section_mode", "custom_control_section_operation_mode"
            ]
        }
    })


class LayerSet(Component):
    """

    """
    _components = {}

    _endpoints = {
        "select": {
            "path": "/sel",
            "class": endpoint.IntMappingEndpoint,
            "aliases": ["sel"]
        }
    }


class LeftLayerSet(LayerSet):
    """

    """
    _endpoints = deepcopy(LayerSet._endpoints)
    _endpoints["select"].update({
        "int_mapping": {
            1: ["1-12", "Ch 1..Ch 12"],
            2: ["13-24", "Ch 13..Ch 24"],
            3: ["25-36", "Ch 25..Ch 36"],
            4: ["37-40 AUX IN", "Ch 36.. Ch 40 / Aux 1..Aux 8"],
            5: ["BUS MASTER", "Bus 1..Bus 12"],
            6: ["USER 1", "User 1"],
            7: ["USER 2", "User 2"],
            10: "1-8",
            11: "9-16",
            12: "17-24",
            13: "25-32",
            14: "33-40",
            15: "AUX IN",
            16: "BUS 1-8",
            17: "BUS 9-16",
            18: "MAIN 1-4",
            19: "MATRIX 1-8",
            20: "DCA 1-8",
            21: "DCA 9-16",
            22: "SPILL",
        }
    })


class FullsizeLayerSection(Component):
    """

    """
    _components = {
        "left": {
            "path": "/L",
            "class": LeftLayerSet,
            "aliases": ["l"],
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
            "variants": {
                "fullsize": {
                    "path": "/cfg",
                    "class": FullsizeConfig,
                    "aliases": ["cfg", "configuration"]
                },
                "compact": {
                    "path": "/cfg",
                    "class": CompactConfig,
                    "aliases": ["cfg", "configuration"]
                },
                "rack": {
                    "path": "/cfg",
                    "class": RackConfig,
                    "aliases": ["cfg", "configuration"]
                },
                "ext": {
                    "path": "/cfg",
                    "class": Config,
                    "aliases": ["cfg", "configuration"]
                },
                "virtual": {
                    "path": "/cfg",
                    "class": Config,
                    "aliases": ["cfg", "configuration"]
                }
            }
        },
        "layer": {
            "variants": {
                "fullsize": {
                    "path": "/layer",
                    "class": FullsizeLayerSection
                }
            }
        }
    }

    _endpoints = {}
