"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class DynamicEQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "DEQ"

    @staticmethod
    def model_name() -> str:
        return "DynamicEQ"

    _components = {}

    _endpoints = {
        "threshold": {
            "path": "/thr",
            "class": endpoint.FloatEndpoint,
            "min": -60.0,
            "max": 0.0,
            "aliases": [ "thr" ]
        },
        "ratio": {
            "path": "/ratio",
            "class": endpoint.FloatEndpoint,
            "valid_values": [ 1.2, 1.3, 1.5, 2.0, 3.0, 5.0, 10.0 ]
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 200.0,
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 4000.0,
            "aliases": [ "rel" ]
        },
        "filter_types": {
            "path": "/filt",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "OFF": "OFF",
                "BP": "BP",
                "LP6": "LP 6dB",
                "LP12": "LP 12dB",
                "HP6": "HP 6dB",
                "HP12": "HP 12dB"
            },
            "aliases": [ "filter_type", "filt" ]
        },
        "gain": {
            "path": "/g",
            "class": endpoint.FloatEndpoint,
            "min": -15.0,
            "max": 15.0,
            "aliases": [ "g" ]
        },
        "freq": {
            "path": "/f",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 20000.0,
            "aliases": [ "f", "frequency" ]
        },
        "q": {
            "path": "/q",
            "class": endpoint.FloatEndpoint,
            "min": 0.442,
            "max": 10.0
        },
        "mode": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "low": "Below",
                "high": "Above"
            }
        },
        "above": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "low": False,
                "high": True
            }
        },
        "below": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "low": True,
                "high": False
            }
        }
    }
