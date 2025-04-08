"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from .common import StandardFGBand, StandardFGQBand


class EdgeBand(StandardFGBand):
    """

    """
    _endpoints = deepcopy(StandardFGBand._endpoints)
    _endpoints.update({
        "q": {
            "path": "q",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "LOW", "HIGH" ]
        },
        "hi_q": {
            "path": "q",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "LOW": False,
                "HIGH": True
            }
        },
        "type": {
            "path": "t",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "BELL", "SHELV" ]
        }
    })


class LowBand(EdgeBand):
    """

    """
    _endpoints = deepcopy(EdgeBand._endpoints)
    _endpoints["gain"]["aliases"].append("db")
    _endpoints["frequency"]["aliases"].append("hz")


class LowMidBand(StandardFGQBand):
    """

    """
    _endpoints = deepcopy(StandardFGQBand._endpoints)
    _endpoints["gain"]["aliases"].append("db")
    _endpoints["frequency"]["aliases"].append("hz")


class HighMidBand(StandardFGQBand):
    """

    """
    _endpoints = deepcopy(StandardFGQBand._endpoints)
    _endpoints["gain"]["aliases"].append("db")
    _endpoints["frequency"]["aliases"].append("khz")


class HighBand(EdgeBand):
    """

    """
    _endpoints = deepcopy(EdgeBand._endpoints)
    _endpoints["gain"]["aliases"].append("db")
    _endpoints["frequency"]["aliases"].append("khz")


class Even88FormantEQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "E88"

    @staticmethod
    def model_name() -> str:
        return "Even 88-Formant EQ"

    _components = {
        "low": {
            "path": "/l",
            "class": LowBand,
            "aliases": [ "l" ]
        },
        "low_mid": {
            "path": "/lm",
            "class": LowMidBand,
            "aliases": [ "lm" ]
        },
        "high_mid": {
            "path": "/hm",
            "class": HighMidBand,
            "aliases": [ "hm" ]
        },
        "high": {
            "path": "/h",
            "class": HighBand,
            "aliases": [ "h" ]
        }
    }

    _endpoints = {
        # No "eq" endpoint as that would clash with the plugin's representation within
        # the FX section.
        "mix": {
            "path": "/mix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 125.0
        }
    }
