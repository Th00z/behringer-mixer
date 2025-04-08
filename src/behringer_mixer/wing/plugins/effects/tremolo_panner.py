"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from .effect_sections import EnvelopeSection, LFOSection


class EnvelopeModulationSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "speed": {
            "path": "spd",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "espd", "spd", "envelope_modulation_speed" ]
        },
        "depth": {
            "path": "dep",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "edep", "dep", "envelope_modulation_depth" ]
        }
    }


class TremoloSection(Component):
    """

    """
    _components = {
        "envelope_modulation": {
            "path": "/e",
            "class": EnvelopeModulationSection,
            "aliases": [ "envelope", "env" ]
        }
    }

    _endpoints = {
        "depth": {
            "path": "/depth",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100
        }
    }


class TremoloPanner(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "PANNER"

    @staticmethod
    def model_name() -> str:
        return "Tremolo Panner"

    _components = {
        "tremolo": {
            "path": "",
            "class": TremoloSection
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
