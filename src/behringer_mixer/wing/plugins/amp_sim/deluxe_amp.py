"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from .amp_base import AmpBase


class DeluxeAmp(AmpBase):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "DELUXE"

    @staticmethod
    def model_name() -> str:
        return "Deluxe Amp"

    _endpoints = deepcopy(AmpBase._endpoints)
    _endpoints.update({
        "volume": {
            "path": "/vol",
            "class": endpoint.StandardKnob,
            "aliases": [ "vol" ]
        },
        "sag": {
            "path": "/sag",
            "class": endpoint.StandardKnob
        }
    })
