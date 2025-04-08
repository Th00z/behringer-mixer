"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from .effect_sections import EnvelopeSection, LFOSection


class MultiPhaserSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "range": {
            "path": "/range",
            "class": endpoint.IntEndpoint,
            "min": 2,
            "max": 98
        },
        "depth": {
            "path": "/depth",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100
        },
        "env_mod": {
            "path": "/emod",
            "class": endpoint.IntEndpoint,
            "min": -100,
            "max": 100,
            "aliases": [ "emod", "envmod" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100
        },
        "stages": {
            "path": "/stg",
            "class": endpoint.IntEndpoint,
            "min": 2,
            "max": 12,
            "aliases": [ "stg" ]
        },
        "resonance": {
            "path": "/reso",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 80,
            "aliases": [ "reso" ]
        }
    }


class Phaser(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "PHASER"

    @staticmethod
    def model_name() -> str:
        return "Phaser"

    _components = {
        "multi_phaser": {
            "path": "",
            "class": MultiPhaserSection
        },
        "lfo": {
            "path": "",
            "class": LFOSection
        },
        "envelope": {
            "path": "",
            "class": EnvelopeSection
        }
    }

    _endpoints = {}
