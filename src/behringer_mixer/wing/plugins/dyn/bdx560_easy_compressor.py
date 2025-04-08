"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .threshold_ratio_compressor import ThresholdRatioCompressor


class BDX560EasyCompressor(ThresholdRatioCompressor):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "B560"

    @staticmethod
    def model_name() -> str:
        return "BDX 560 Easy Compressor"

    _endpoints = deepcopy(ThresholdRatioCompressor._endpoints)
    _endpoints["threshold"].update({
        "min": -40.0,
        "max": 20.0
    })
    _endpoints["ratio"].update({
        "valid_values": [
            1.1, 1.2, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0,
            10.0, 50.0, 999.0, -5.0, -3.0, -2.0, -1.0
        ],
        "aliases": [ "compression_ratio" ]
    })
    _endpoints.update({
        "bypass": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "invert": True
        },
        "output_gain": {
            "path": "/gain",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 12.0,
            "aliases": [ "gain" ]
        },
        "easy": {
            "path": "/easy",  # Documentation says auto, but it is actually easy
            "class": endpoint.BoolEndpoint,
            "aliases": [ "auto" ]
        },
    })
