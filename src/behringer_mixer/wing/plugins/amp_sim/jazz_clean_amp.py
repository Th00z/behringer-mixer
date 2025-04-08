"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from .amp_base import MidAmpBase


class JazzCleanAmp(MidAmpBase):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "JAZZC"

    @staticmethod
    def model_name() -> str:
        return "Jazz Clean Amp"

    _endpoints = deepcopy(MidAmpBase._endpoints)
    _endpoints.update({
        "volume": {
            "path": "/vol",
            "class": endpoint.StandardKnob,
            "aliases": [ "vol" ]
        },
        "bri": {
            "path": "/bri",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "bright" ]
        }
    })
