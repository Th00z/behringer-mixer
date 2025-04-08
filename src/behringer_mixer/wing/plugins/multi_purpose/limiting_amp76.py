"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class LimitingAmp76(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "76LA"

    @staticmethod
    def model_name() -> str:
        return "76 Limiting Amp"

    _components = {}

    _endpoints = {
        "input": {
            "path": "/in",
            "class": endpoint.FloatEndpoint,
            "min": -48.0,
            "max": 0.0
        },
        "output": {
            "path": "/out",
            "class": endpoint.FloatEndpoint,
            "min": -48.0,
            "max": 0.0,
            "aliases": [ "out" ]
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 7.0,
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 7.0,
            "aliases": [ "rel" ]
        },
        "ratio": {
            "path": "/ratio",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "4", "8", "12", "20", "ALL" ]
        }
    }
