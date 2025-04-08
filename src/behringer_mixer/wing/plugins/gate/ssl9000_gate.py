"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class SSL9000Gate(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "9000G"

    @staticmethod
    def model_name() -> str:
        return "SSL 9000 Gate/Expander"

    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "threshold": {
            "path": "/thr",
            "class": endpoint.FloatEndpoint,
            "min": -40.0,
            "max": 0.0,
            "aliases": [ "thr" ]
        },
        "range": {
            "path": "/range",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 40.0
        },
        "hold": {
            "path": "/hld",
            "class": endpoint.FloatEndpoint,
            "min": 10.0,
            "max": 4000.0,
            "aliases": [ "hld" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 100.0,
            "max": 4000.0,
            "aliases": [ "rel" ]
        },
        "attack": {
            "path": "/fast",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "FAST",
                False: "SLOW"
            }
        },
        "fast": {
            "path": "/fast",
            "class": endpoint.BoolEndpoint
        },
        "mode": {
            "path": "/mode",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "GATE", "EXP" ]
        },
        "expand": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "GATE": False,
                "EXP": True
            }
        }
    }
