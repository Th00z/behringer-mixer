"""

"""
from copy import deepcopy

from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint

from .base_reverb import DigitalReverb


class ReverseReverb(DigitalReverb):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "REVERSE"

    @staticmethod
    def model_name() -> str:
        return "Reverse Reverb"

    _endpoints = deepcopy(DigitalReverb._endpoints)
    _endpoints.update({
        "rise": {
            "path": "/rise",
            "class": endpoint.IntEndpoint,
            "min": 0, # Documentation states 4...50 but the console yields 0...60
            "max": 60
        }
    })
