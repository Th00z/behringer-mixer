"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class FairkidModel670(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "F670"

    @staticmethod
    def model_name() -> str:
        return "Fairkid Model 670"

    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "out_gain": {
            "path": "/gain",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 12.0,
            "aliases": [ "gain" ]
        },
        "input_gain": {
            "path": "/in",
            "class": endpoint.FloatEndpoint,
            "min": -20.0,
            "max": 0.0
        },
        "threshold": {
            "path": "/thr",
            "class": endpoint.StandardKnob,
            "aliases": [ "thr" ]
        },
        "time_constant": {
            "path": "/time",
            "class": endpoint.IntEndpoint,
            "min": 1,
            "max": 6,
            "aliases": [ "time" ]
        },
        "dc_bias": {
            "path": "/bias",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 1.0,
            "aliases": [ "bias" ]
        }
    }
