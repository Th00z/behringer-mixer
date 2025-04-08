"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class LevelingAmplifier2A(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "LA"

    @staticmethod
    def model_name() -> str:
        return "Leveling Amplifier 2A"

    _components = {}

    _endpoints = {
        "power": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "ON",
                False: "OFF"
            },
            "aliases": [ "on" ]
        },
        "gain": {
            "path": "/ingain",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "ingain" ]
        },
        "peak_reduction": {
            "path": "/peak",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "peak" ]
        },
        "mode": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                # Documentation speaks of lowercase "comp"/"lim", but actually it's uppercase
                "COMP": "COMPRESS",
                "LIM": "LIMIT"
            }
        },
        "limit": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                # Documentation speaks of lowercase "comp"/"lim", but actually it's uppercase
                "COMP": False,
                "LIM": True
            }
        },
        "compress": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                # Documentation speaks of lowercase "comp"/"lim", but actually it's uppercase
                "COMP": True,
                "LIM": False
            }
        }
    }
