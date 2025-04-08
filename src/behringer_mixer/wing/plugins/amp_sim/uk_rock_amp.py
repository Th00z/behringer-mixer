"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from .amp_base import MidAmpBase


class UKRockAmp(MidAmpBase):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "UKROCK"

    @staticmethod
    def model_name() -> str:
        return "UK Rock Amp"

    _endpoints = deepcopy(MidAmpBase._endpoints)
    _endpoints.update({
        "gain": {
            "path": "/gain",
            "class": endpoint.StandardKnob,
            "aliases": [ "gains" ]
        },
        "presence": {
            "path": "/pres",
            "class": endpoint.StandardKnob,
            "aliases": [ "pres" ]
        },
        "master": {
            "path": "/mstr",
            "class": endpoint.StandardKnob,
            "aliases": [ "mstr" ]
        },
        "sag": {
            "path": "/sag",
            "class": endpoint.StandardKnob
        }
    })
