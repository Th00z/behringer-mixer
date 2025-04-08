"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .threshold_ratio_compressor import ThresholdRatioCompressor


class StandardCompressor(ThresholdRatioCompressor):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "COMP"

    @staticmethod
    def model_name() -> str:
        return "Standard compressor"

    _endpoints = deepcopy(ThresholdRatioCompressor._endpoints)
    _endpoints["threshold"].update({
        "min": -60.0,
        "max": 0.0
    })
    _endpoints["ratio"].update({
        "valid_values": [
            1.1, 1.2, 1.3, 1.5, 1.7, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0,
            10.0, 20.0, 50.0, 100.0
        ]
    })
    _endpoints.update({
        "knee": {
            "path": "/knee",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 5
        },
        "detector": {
            "path": "/det",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "PEAK", "RMS" ],
            "aliases": [ "det" ]
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 120.0,
            "aliases": [ "att" ]
        },
        "hold": {
            "path": "/hld",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 200.0,
            "aliases": [ "hld" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 4.0,
            "max": 4000.0,
            "aliases": [ "rel" ]
        },
        "envelope": {
            "path": "/env",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "LIN", "LOG" ],
            "aliases": [ "env" ]
        },
        "auto_envelope": {
            "path": "/auto",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "auto" ]
        }
    })
