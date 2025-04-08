"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .base_reverb import BaseShapedReverb


class HallReverb(BaseShapedReverb):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "HALL"

    @staticmethod
    def model_name() -> str:
        return "Hall Reverb"

    _endpoints = deepcopy(BaseShapedReverb._endpoints)
    _endpoints["size"].update({
        "class": endpoint.IntEndpoint,
        "min": 0,
        "max": 100
    })
    _endpoints["decay"].update({
        "min": 0.2,
        "max": 5.0
    })
    _endpoints["bass_mult"].update({
        "min": 0.5,
        "max": 2.0
    })
    _endpoints["shape"].update({
        "max": 50.0
    })
    _endpoints["diffusion"].update({
        "min": 1,
        "max": 30
    })
    _endpoints.update({
        "mod_spd": {
            "path": "/mspd",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "mspd", "mod_speed" ]
        }
    })
