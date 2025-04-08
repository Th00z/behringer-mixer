"""

"""
from abc import ABC
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class ThresholdRatioCompressor(ConcretePlugin, ABC):
    """

    """
    _components = {}

    _endpoints = {
        "threshold": {
            "path": "/thr",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 0.0,
            "aliases": [ "thr" ]
        },
        "ratio": {
            "path": "/ratio",
            "class": endpoint.FloatEndpoint,
            "valid_values": []
        }
    }
