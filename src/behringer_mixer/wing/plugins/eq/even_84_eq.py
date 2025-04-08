"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from .common import StandardStringFrequencyGBand


class Even84EQLow(StandardStringFrequencyGBand):
    """

    """
    _endpoints = deepcopy(StandardStringFrequencyGBand._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "OFF", "35", "60", "110", "220" ]
    })
    _endpoints["frequency"]["aliases"].append("hz")


class Even84EQMid(StandardStringFrequencyGBand):
    """

    """
    _endpoints = deepcopy(StandardStringFrequencyGBand._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "OFF", "350", "700", "1k6", "3k2", "4k8", "7k2" ]
    })
    _endpoints["frequency"]["aliases"].append("khz")
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
    })


class Even84EQHigh(StandardStringFrequencyGBand):
    """

    """
    _endpoints = deepcopy(StandardStringFrequencyGBand._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "OFF", "10k", "12k", "16k" ]
    })
    _endpoints["frequency"]["aliases"].append("khz")


class Even84EQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "E84"

    @staticmethod
    def model_name() -> str:
        return "Even 84 EQ"

    _components = {
        "low": {
            "path": "/l",
            "class": Even84EQLow,
            "aliases": [ "l" ]
        },
        "mid": {
            "path": "/m",
            "class": Even84EQMid,
            "aliases": [ "m" ]
        },
        "high": {
            "path": "/h",
            "class": Even84EQHigh,
            "aliases": [ "h" ]
        }
    }

    _endpoints = {
        "gain": {
            "path": "/g",
            "class": endpoint.FloatEndpoint,
            "min": -20.0,
            "max": 20.0,
            "aliases": [ "g", "db" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 125.0
        }
    }
