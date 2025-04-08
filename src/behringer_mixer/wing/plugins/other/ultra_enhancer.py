"""

"""
from copy import deepcopy
from behringer_mixer.component import Component

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class BandSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "gain": {
            "path": "",
            "class": endpoint.PercentEndpoint
        }
    }


class EdgeBand(BandSection):
    """

    """
    _endpoints = deepcopy(BandSection._endpoints)
    _endpoints.update({
        "freq": {
            "path": "f",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 50.0,
            "aliases": [ "frequency", "f" ]
        }
    })


class MidBand(BandSection):
    """

    """
    _endpoints = deepcopy(BandSection._endpoints)
    _endpoints.update({
        "q": {
            "path": "q",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 50.0
        }
    })


class StereoSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "lmf_spread": {
            "path": "/lmf",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "lmf", "low_mid_frequency_spread" ]
        },
        "level": {
            "path": "/stlvl",  # Typo in documentation: trailing 'l' missing.
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "stlvl", "stlv", "stereo_level", "stereo_lvl", "st_lvl", "st_lv" ]
        },
        "pan": {
            "path": "/st",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "st", "st_pan", "stereo_pan" ]
        }
    }


class MonoSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "level": {
            "path": "lvl",  # Typo in documentation: leading 'm' and 'l' swapped.
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "lvl", "mono_level", "mono_lvl", "m_lvl", "mlvl", "lmvl" ]
        },
        "pan": {
            "path": "",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases":  [ "m", "m_pan", "mono_pan" ]
        }
    }


class UltraEnhancer(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "ENHANCE"

    @staticmethod
    def model_name() -> str:
        return "Ultra Enhancer"

    _components = {
        "bass": {
            "path": "/bass",
            "class": EdgeBand
        },
        "mid": {
            "path": "/mid",
            "class": MidBand
        },
        "high": {
            "path": "/high",
            "class": EdgeBand
        },
        "stereo": {
            "path": "",
            "class": StereoSection,
            "aliases": [ "st" ]
        },
        "mono": {
            "path": "/m",
            "class": MonoSection,
            "aliases": [ "m" ]
        }
    }

    _endpoints = {
        "gain": {
            "path": "/g",
            "class": endpoint.FloatEndpoint,
            "min": -112.0,
            "max": 12.0,
            "aliases": [ "g" ]
        },
        "solo": {
            "path": "/solo",
            "class": endpoint.BoolEndpoint
        }
    }
