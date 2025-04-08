"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin, LeftRightComponent

from .effect_sections import FilterSection


class ModulatorSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "wave": {
            "path": "/wave",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "waveform" ]
        },
        "phase": {
            "path": "/phase",
            "class": endpoint.FloatEndpoint,
            "min": 0.0, # Documentation states 0...100 but it's actually this!
            "max": 180.0
        },
        "spread": {
            "path": "/sprd",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "sprd" ]
        },
        "speed": {
            "path": "/spd",
            "class": endpoint.FloatEndpoint,
            "min": 0.05,
            "max": 5.0
        }
    }


class DelaySection(LeftRightComponent):
    """

    """
    _components = {}

    _endpoints = {
        "size": {
            "path": "/dly{side}",
            "class": endpoint.FloatEndpoint,
            "min": 5.0,
            "max": 50.0,
            "aliases": [ "delay", "dly", "length", "time" ]
        },
        "depth": {
            "path": "/dep{side}",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "dep" ]
        }
    }


class StereoChorus(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "CHORUS"

    @staticmethod
    def model_name() -> str:
        return "Stereo Chorus"

    _components = {
        "modulator": {
            "path": "",
            "class": ModulatorSection
        },
        "delay_left": {
            "path": "/l",
            "class": DelaySection
        },
        "delay_right": {
            "path": "/r",
            "class": DelaySection
        },
        "filter_wing": {
            "path": "",
            "class": FilterSection,
            "aliases": [ "filter" ]
        }
    }

    _endpoints = {
        "mix": {
            "path": "/mix",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "dry_wet" ]
        }
    }
