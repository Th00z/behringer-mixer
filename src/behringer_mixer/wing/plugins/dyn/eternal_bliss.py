"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .threshold_ratio_compressor import ThresholdRatioCompressor


class EternalBliss(ThresholdRatioCompressor):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "BLISS"

    @staticmethod
    def model_name() -> str:
        return "Eternal Bliss"

    _endpoints = deepcopy(ThresholdRatioCompressor._endpoints)
    _endpoints["threshold"].update({
        "min": -50.0,
        "max": 0.0
    })
    _endpoints["ratio"].update({
        "valid_values": [ 1.2, 1.3, 1.6, 2.0, 3.0, -1.0, -2.0, -3.0, -4.0 ]
    })
    _endpoints.update({
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 0.4,
            "max": 150.0,
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 5.0,
            "max": 120.0,
            "aliases": [ "rel" ]
        },
        "auto_fast": {
            "path": "/afast",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "afast" ]
        },
        "anti_log": {
            "path": "/alog",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "alog" ]
        },
        "on": {
            "path": "/glon",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "glon" ]
        },
        "gr_limit": {
            "path": "/glim",
            "class": endpoint.FloatEndpoint,
            "min": -21.0,
            "max": 0.0,
            "aliases": [ "glim" ]
        },
        "gain": {
            "path": "/gain",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 12.0
        }
    })
