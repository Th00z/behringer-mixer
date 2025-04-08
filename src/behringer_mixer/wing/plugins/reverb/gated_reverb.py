"""

"""
from copy import deepcopy

from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint

from .base_reverb import DigitalReverb


class GatedReverb(DigitalReverb):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "GATED"

    @staticmethod
    def model_name() -> str:
        return "Gated Reverb"

    _endpoints = deepcopy(DigitalReverb._endpoints)
    _endpoints.update({
        "attack": {
            "path": "/att",
            "class": endpoint.IntEndpoint,
            "min": 4,
            "max": 30,
            "aliases": [ "att" ]
        },
        "density": {
            "path": "/dens",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "dens" ]
        }
    })
