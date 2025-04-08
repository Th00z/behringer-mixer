"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class AutoRiderDynamics(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "RIDE"

    @staticmethod
    def model_name() -> str:
        return "Auto Rider Dynamics"

    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "threshold": {
            "path": "/thr",
            "class": endpoint.FloatEndpoint,
            "min": -54.0,
            "max": 18.0,
            "aliases": [ "thr" ]
        },
        "target": {
            "path": "/tgt",
            "class": endpoint.FloatEndpoint,
            "min": -48.0,
            "max": 0.0,
            "aliases": [ "tgt" ]
        },
        "speed": {
            "path": "/spd",
            "class": endpoint.IntEndpoint,
            "min": 1,
            "max": 50,
            "aliases": [ "spd" ]
        },
        "ratio": {
            "path": "/ratio",
            "class": endpoint.FloatEndpoint,
            "valid_values": [ 2.0, 4.0, 8.0, 20.0, 100.0 ]
        },
        "hold": {
            "path": "/hld",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 10.0,
            "aliases": [ "hld" ]
        },
        "range": {
            "path": "/range",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 15.0
        }
    }
