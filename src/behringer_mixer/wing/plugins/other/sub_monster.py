"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class SubMonster(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "SUB-M"

    @staticmethod
    def model_name() -> str:
        return "Sub Monster"

    _components = {}

    _endpoints = {
        "mix": {
            "path": "/mix",
            "class": endpoint.PercentEndpoint
        },
        "tune": {
            "path": "/freq",
            "class": endpoint.FloatEndpoint,
            "min": 45.0,
            "max": 67.5,
            "aliases": [ "freq", "frequency", "f" ]
        },
        "band": {
            "path": "/bd",
            "class": endpoint.PercentEndpoint,
            "count": 5,
            "index_format_string": "{index}",
            "aliases": [ "bd" ]
        }
    }
