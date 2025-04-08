"""

"""
from copy import deepcopy

from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from .threshold_ratio_compressor import ThresholdRatioCompressor


class DrawMoreCompressorLimiter(Component):
    """

    """
    _components = {}

    _endpoints = {
        "threshold": {
            "path": "/lim",
            "class": endpoint.FloatEndpoint,
            "min": -20.0,
            "max": 0.0,
            "aliases": [ "lim" ]
        },
        "release": {
            "path": "/lrel",
            "class": endpoint.FloatEndpoint,
            "min": -50.0,
            "max": 5000.0,
            "aliases": [ "lrel" ]
        }
    }


class DrawMoreCompressor(ThresholdRatioCompressor):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "D241"

    @staticmethod
    def model_name() -> str:
        return "Draw More Compressor"

    _components = deepcopy(ThresholdRatioCompressor._components)
    _components.update({
        "peak": {
            "path": "",
            "class": DrawMoreCompressorLimiter,
            "aliases": [ "l" ]
        }
    })

    _endpoints = deepcopy(ThresholdRatioCompressor._endpoints)
    _endpoints["threshold"].update({
        "min": -60.0,
        "max": 0.0
    })
    _endpoints["ratio"].update({
        "valid_values": [
            1.1, 1.2, 1.3, 1.5, 1.7, 2.0, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0,
            10.0, 20.0, 50.0, 100.0
        ]
    })
    _endpoints.update({
        "bypass": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "invert": True
        },
        "gain": {
            "path": "/gain",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 12.0
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 0.5,
            "max": 100.0,
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 50.0,
            "max": 5000.0,
            "aliases": [ "rel" ]
        },
        "auto": {
            "path": "/auto",
            "class": endpoint.BoolEndpoint
        }
    })
