"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class SoulWarmthPreamp(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "WARM"

    @staticmethod
    def model_name() -> str:
        return "Soul Warmth Preamp"

    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "drive": {
            "path": "/drv",
            "class": endpoint.FloatEndpoint,
            "min": 10.0,
            "max": 125.0, # Documentation states it's 100 but it's actually 125.
            "aliases": [ "drv" ]
        },
        "harmonics": {
            "path": "/hrm",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "hrm" ]
        },
        "color": {
            "path": "/col",
            "class": endpoint.FloatEndpoint,
            "min": -1.0,
            "max": 1.0,
            "aliases":  [ "col" ]
        },
        "trim": {
            "path": "/trim",
            "class": endpoint.FloatEndpoint,
            "min": -18.0,
            "max": 6.0
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.PercentEndpoint
        },
    }
