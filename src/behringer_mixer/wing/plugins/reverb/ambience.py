"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .base_reverb import BaseReverb


# The spelling in the documentation is ambiance, on the console it is ambience. Sticking with
# the console here.
class Ambience(BaseReverb):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "AMBI"

    @staticmethod
    def model_name() -> str:
        return "Ambience"

    _endpoints = deepcopy(BaseReverb._endpoints)
    _endpoints["size"].update({
        "min": 2.0,
        "max": 100.0
    })
    _endpoints["decay"].update({
        "min": 0.2,
        "max": 7.3
    })
    _endpoints["diffusion"].update({
        "min": 1,
        "max": 30
    })
    _endpoints.update({
        "tail_gain": {
            "path": "/tail",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "tail" ]
        },
        "mod_spd": {
            "path": "/mod",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "mod", "mod_speed" ]
        }
    })
