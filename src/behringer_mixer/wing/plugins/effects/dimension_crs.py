"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class DimensionCRS(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "DIMCRS"

    @staticmethod
    def model_name() -> str:
        return "Dimension CRS"

    _components = {}

    _endpoints = {
        "preset_1": {
            "path": "/sw1",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw1" ]
        },
        "preset_2": {
            "path": "/sw2",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw2" ]
        },
        "preset_3": {
            "path": "/sw3",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw3" ]
        },
        "preset_4": {
            "path": "/sw4",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw4" ]
        },
        "mode": {
            "path": "/in",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "MONO", "STEREO" ],
            "aliases": [ "input_mode", "in" ]
        },
        "stereo": {
            "path": "/in",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "MONO": False,
                "STEREO": True
            }
        },
        "mono": {
            "path": "/in",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "MONO": True,
                "STEREO": False
            }
        },
        "mix": {
            "path": "/drysw",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "DRY",
                False: "WET"
            }
        },
        "dry": {
            "path": "/drysw",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "drysw" ]
        }
    }
