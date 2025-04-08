"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class Even88Gate(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "E88"

    @staticmethod
    def model_name() -> str:
        return "Even 88-Gate"

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
        "hysteresis": {
            "path": "/hyst",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 25.0,
            "aliases": [ "hyst" ]
        },
        "range": {
            "path": "/range",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 60.0
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 100.0,
            "max": 3000.0,
            "aliases": [ "rel" ]
        },
        "attack": {
            "path": "/fast",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "FAST",
                False: "SLOW"
            },
        },
        "fast": {
            "path": "/fast",
            "class": endpoint.BoolEndpoint
        },
        "attenuation": {
            "path": "/m40",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "-40dB",
                False: "None"
            }
        },
        "m40": {
            "path": "/m40",
            "class": endpoint.BoolEndpoint
        }
    }
