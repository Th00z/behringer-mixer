"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .threshold_ratio_compressor import ThresholdRatioCompressor


class BDX160CompressorLimiter(ThresholdRatioCompressor):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "B160"

    @staticmethod
    def model_name() -> str:
        return "BDX 160 Compressor/Limiter"

    _endpoints = deepcopy(ThresholdRatioCompressor._endpoints)
    _endpoints["threshold"].update({
        "min": 0.01,
        "max": 5.0
    })
    _endpoints["ratio"].update({
        # Documentation states the path is still ratio, but it isn't
        "path": "/comp",
        "valid_values": [
            1.1, 1.2, 1.3, 1.5, 1.7, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0,
            10.0, 20.0, 50.0
        ],
        "aliases": [ "compression" ]
    })
    _endpoints.update({
        "power": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "on" ]
        },
        "output_gain": {
            "path": "/gain",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 12.0,
            "aliases": [ "gain" ]
        },
    })
