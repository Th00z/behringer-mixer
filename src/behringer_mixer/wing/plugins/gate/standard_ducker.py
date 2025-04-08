"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class StandardDucker(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "DUCK"

    @staticmethod
    def model_name() -> str:
        return "Standard Ducker"

    _components = {}

    _endpoints = {
        "threshold": {
            "path": "/thr",
            "class": endpoint.FloatEndpoint,
            "min": -80.0,
            "max": 0.0,
            "aliases": [ "thr" ]
        },
        "range": {
            "path": "/range",
            "class": endpoint.FloatEndpoint,
            "min": 3.0,
            "max": 60.0
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 120.0,
            "aliases": [ "att" ]
        },
        "hold": {
            # Gate Plugin Documentation says path is /hold, while it actually is /hld
            "path": "/hld",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 200.0,
            "aliases": [ "hld" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 4000.0,
            "aliases": [ "rel" ]
        }
    }
