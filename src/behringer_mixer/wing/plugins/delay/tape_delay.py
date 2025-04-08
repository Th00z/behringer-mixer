"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class TapeDelay(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "TAPE-DL"

    @staticmethod
    def model_name() -> str:
        return "Tape Delay"

    _components = {}

    _endpoints = {
        "time": {
            "path": "/time",
            "class": endpoint.FloatEndpoint,
            "min": 60.0,
            "max": 650.0
        },
        "sustain": {
            "path": "/sust",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "sust" ]
        },
        "drive": {
            "path": "/drv",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "drv" ]
        },
        "flutter": {
            "path": "/wf",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "wf" ]
        }
    }
