"""

"""
import re
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import LeftRightComponent
from .base_reverb import BaseShapedReverb


class Echo(LeftRightComponent):
    """

    """
    _components = {}

    _endpoints = {
        "depth": {
            "path": "ec{side}",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 1200.0,
            "aliases": [ "ec", "echo", "size", "length" ]
        },
        "feed": {
            "path": "ef{side}",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "ef", "echo_feed" ]
        }
    }


class RoomReverb(BaseShapedReverb):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "ROOM"  # Documentation has a typo: R-OOM instead of ROOM

    @staticmethod
    def model_name() -> str:
        return "Room Reverb"

    _components = deepcopy(BaseShapedReverb._components)
    _components.update({
        "echo_l": {
            "path": "/l",
            "class": Echo,
            "aliases":  [ "el", "echo_left" ]
        },
        "echo_r": {
            "path": "/r",
            "class": Echo,
            "aliases":  [ "er", "echo_right" ]
        }
    })

    _endpoints = deepcopy(BaseShapedReverb._endpoints)
    _endpoints["decay"].update({
        "max": 25.0
    })
    _endpoints["shape"].update({
        "max": 250.0
    })
    _endpoints.update({
        "spin": {
            "path": "/spin",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100
        }
    })
