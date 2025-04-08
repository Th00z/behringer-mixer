"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

class PrecisionLimiter(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "LIMITER"

    @staticmethod
    def model_name() -> str:
        return "Precision Limiter"

    _components = {}

    _endpoints = {
        "in_gain": {
            "path": "/gin",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 18.0,
            "aliases": [ "gin" ]
        },
        "out_gain": {
            "path": "/gout",
            "class": endpoint.FloatEndpoint,
            "min": -18.0,
            "max": 0.0,
            "aliases": [ "gout" ]
        },
        "squeeze": {
            "path": "/sqz",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "sqz" ]
        },
        "knee": {
            "path": "/knee",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 10
        },
        "auto_gain": {
            "path": "/again",
            "class": endpoint.BoolEndpoint,
            "aliases":  [ "again" ]
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 0.05,
            "max": 1.0,
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 2000.0,
            "aliases": [ "rel" ]
        }
    }
