"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .threshold_ratio_compressor import ThresholdRatioCompressor


class SoulGBusCompressor(ThresholdRatioCompressor):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "SBUS"

    @staticmethod
    def model_name() -> str:
        return "Soul G Bus Compressor"

    _endpoints = deepcopy(ThresholdRatioCompressor._endpoints)
    _endpoints["threshold"].update({
        "min": -40.0,  # Documentation states -48 but it's actually -40
        "max": 0.0
    })
    _endpoints["ratio"].update({
        "valid_values": [ 1.5, 2.0, 3.0, 4.0, 5.0, 10.0 ]
    })
    _endpoints.update({
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "valid_values": [ 0.1, 0.3, 1.0, 3.0, 10.0, 30.0 ],
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "0.1", "0.2", "0.4", "0.8", "1.6", "AUTO" ],
            "aliases": [ "rel" ]
        },
        "makeup": {
            "path": "/gain",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 12.0,
            "aliases": [ "gain" ]
        }
    })
