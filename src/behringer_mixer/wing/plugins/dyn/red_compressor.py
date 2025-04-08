"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .threshold_ratio_compressor import ThresholdRatioCompressor


class REDCompressor(ThresholdRatioCompressor):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "RED3"

    @staticmethod
    def model_name() -> str:
        return "Red Compressor"

    _endpoints = deepcopy(ThresholdRatioCompressor._endpoints)
    _endpoints["threshold"].update({
        "min": -48.0,
        "max": 0.0
    })
    _endpoints["ratio"].update({
        "valid_values": [ 1.1, 1.2, 1.3, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0, 10.0 ]
    })
    _endpoints.update({
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "make_up_gain": {
            "path": "/gain",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 12.0,
            "aliases": [ "gain" ]
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 50.0,
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 100.0,
            "max": 4000.0,
            "aliases": [ "rel" ]
        },
        "auto": {
            "path": "/auto",
            "class": endpoint.BoolEndpoint
        }
    })
