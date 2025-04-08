"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from .common import StandardFGBand, StandardFGQBand


class dBNamedGainBand(StandardFGBand):
    """

    """
    _endpoints = deepcopy(StandardFGBand._endpoints)
    _endpoints["gain"]["aliases"].append("db")


class LowBand(dBNamedGainBand):
    """

    """
    _endpoints = deepcopy(dBNamedGainBand._endpoints)
    _endpoints["frequency"]["aliases"].append("hz")


class HighBand(dBNamedGainBand):
    """

    """
    _endpoints = deepcopy(dBNamedGainBand._endpoints)
    _endpoints["frequency"]["aliases"].append("khz")


class MidBand(StandardFGQBand):
    """

    """
    _endpoints = deepcopy(StandardFGQBand._endpoints)
    _endpoints["gain"]["aliases"].append("db")
    _endpoints["frequency"]["aliases"].append("khz")


class LowMidBand(MidBand):
    """

    """
    _endpoints = deepcopy(MidBand._endpoints)
    _endpoints.update({
        "by_3": {
            "path": "f3",
            "class": endpoint.BoolEndpoint,
        }
    })


class HighMidBand(MidBand):
    """

    """
    _endpoints = deepcopy(MidBand._endpoints)
    _endpoints.update({
        "times_3": {
            "path": "f3",
            "class": endpoint.BoolEndpoint,
        }
    })


class SoulAnalogEQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "SOUL"

    @staticmethod
    def model_name() -> str:
        return "Soul Analog EQ"

    _components = {
        "low": {
            "path": "/l",
            "class": LowBand,
            "aliases": [ "lf" ]
        },
        "low_mid": {
            "path": "/lm",
            "class": LowMidBand,
            "aliases": [ "lmf" ]
        },
        "high_mid": {
            "path": "/hm",
            "class": HighMidBand,
            "aliases": [ "hmf" ]
        },
        "high": {
            "path": "/h",
            "class": HighBand,
            "aliases": [ "hf" ]
        }
    }

    _endpoints = {
        # No "eq_in" endpoint as that would clash with the plugin's representation within
        # the FX section.
        "mix": {
            "path": "/mix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 125.0
        }
    }
