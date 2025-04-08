"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class WaveDesigner(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "WAVE"

    @staticmethod
    def model_name() -> str:
        return "Wave Designer"

    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": -15.0,
            "max": 15.0,
            "aliases": [ "att" ]
        },
        "sustain": {
            "path": "/sust",
            "class": endpoint.FloatEndpoint,
            "min": -24.0,
            "max": 24.0,
            "aliases": [ "sust" ]
        },
        "output_gain": {
            "path": "/g",
            "class": endpoint.FloatEndpoint,
            "min": -18.0,
            "max": 9.0,
            "aliases": [ "gain", "g" ]
        }
    }
