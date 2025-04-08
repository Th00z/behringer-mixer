"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import LeftRightComponent
from .base_reverb import BaseShapedReverb


class Reflection(LeftRightComponent):
    """

    """
    _components = {}

    _endpoints = {
        "depth": {
            "path": "rf{side}",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 1200.0,
            "aliases": [ "rf", "refl", "reflection", "size", "length" ]
        },
        "level": {
            "path": "rfl{side}",
            "class": endpoint.FaderEndpoint,
            "aliases": [
                "lvl", "rfl", "refl_lvl", "reflection_lvl", "refl_fdr", "reflection_fdr",
                "refl_fader", "reflection_fader", "refl_fdr_lvl", "reflection_fdr_lvl",
                "refl_fader_lvl", "reflection_fader_lvl", "refl_fader_level",
                "reflection_fader_level"
            ]
        }
    }


class ConcertReverb(BaseShapedReverb):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "CONCERT"

    @staticmethod
    def model_name() -> str:
        return "Concert Reverb"

    _components = deepcopy(BaseShapedReverb._components)
    _components.update({
        "refl_l": {
            "path": "/l",
            "class": Reflection,
            "aliases": [ "rfl", "refl_left", "reflection_l", "reflection_left" ]
        },
        "refl_r": {
            "path": "/r",
            "class": Reflection,
            "aliases": [ "rfr", "refl_right", "reflection_r", "reflection_right" ]
        }
    })

    _endpoints = deepcopy(BaseShapedReverb._endpoints)
    _endpoints["size"].update({
        "min": 20.0,
    })
    _endpoints["decay"].update({
        "max": 29.0
    })
    _endpoints["shape"].update({
        "max": 50.0
    })
    # Documentation states diffusion is 1..16 but it's actually 0..100 just like in the
    # other reverbs
    _endpoints.update({
        "depth": {
            "path": "/depth",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100
        },
        "spin": {
            "path": "/spin",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100
        },
        "chorus": {
            "path": "/crs",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "crs" ]
        }
    })
