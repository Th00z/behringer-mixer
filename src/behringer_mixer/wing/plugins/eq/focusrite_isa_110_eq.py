"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from .common import StandardStringFrequencyGBand, StandardFGQBy3Band, StandardFGQTimes3Band


class FocusriteISA100LowShelf(StandardStringFrequencyGBand):
    """

    """
    _endpoints = deepcopy(StandardStringFrequencyGBand._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "33", "56", "95", "160", "270", "460" ]
    })


class FocusriteISA100HighShelf(StandardStringFrequencyGBand):
    """

    """
    _endpoints = deepcopy(StandardStringFrequencyGBand._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "3k3", "4k7", "6k8", "10k", "15k", "18k" ]
    })


class FocusriteISA110EQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "F110"

    @staticmethod
    def model_name() -> str:
        return "Focusrite ISA 110 EQ"

    _components = {
        "low_shelf": {
            "path": "/l",
            "class": FocusriteISA100LowShelf,
            "aliases": [ "l" ]
        },
        "low_mid": {
            "path": "/lm",
            "class": StandardFGQBy3Band,
            "aliases": [ "lm" ]
        },
        "high_mid": {
            "path": "/hm",
            "class": StandardFGQTimes3Band,
            "aliases": [ "hm" ]
        },
        "high_shelf": {
            "path": "/h",
            "class": FocusriteISA100HighShelf,
            "aliases": [ "h" ]
        }
    }

    _endpoints = {
        # No "all_eq" endpoint as that would clash with the plugin's representation within
        # the FX section.
        "gain": {
            "path": "/g",
            "class": endpoint.FloatEndpoint,
            "min": -18.0,
            "max": 18.0,
            "aliases": [ "g" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 125.0
        },
        "peq_in": {
            "path": "/peq",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "peq" ]
        },
        "sheq_in": {
            "path": "/shv",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "shv" ]
        },
    }
