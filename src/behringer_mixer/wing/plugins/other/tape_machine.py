"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class TapeMachine(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "TAPE"

    @staticmethod
    def model_name() -> str:
        return "Tape Machine"

    _components = {}

    _endpoints = {
        "drive": {
            "path": "/drv",
            "class": endpoint.FloatEndpoint,
            "min": -5.0, # Documentation states -12...12 but it's actually this.
            "max": 25.0,
            "aliases": [ "drv" ]
        },
        "speed": {
            "path": "/spd",
            "class": endpoint.FloatEndpoint,
            "min": 7.5,
            "max": 30.0,
            "aliases": [ "spd" ]
        },
        "low_bump": {
            "path": "/low",
            "class": endpoint.BoolEndpoint,
            "aliases":  [ "low" ]
        },
        "high_shelv": {
            "path": "/hi",
            "class": endpoint.BoolEndpoint,
            "aliases":  [ "hi" ]
        },
        "out_gain": {
            "path": "/out",
            "class": endpoint.FloatEndpoint,
            "min": -12.0,
            "max": 12.0,
            "aliases": [ "out" ]
        }
    }
