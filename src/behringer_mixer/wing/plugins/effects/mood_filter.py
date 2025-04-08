"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class EnvelopeSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "depth": {
            "path": "/env",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "env" ]
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 10.0,
            "max": 250.0,
            "aliases": [ "att" ]
        },
        "hold": {
            "path": "/hld",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 500.0,
            "aliases": [ "hld" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 500.0,
            "aliases": [ "rel" ]
        }
    }


class FilterSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "base_freq": {
            "path": "/fbase",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 15000.0,
            "aliases": [ "fbase", "base_frequency", "base" ]
        },
        "type": {
            "path": "/filt",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "LP", "HP", "BP", "NOTCH" ],
            "aliases": [ "filt" ]
        },
        "slope": {
            "path": "/slope",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "12": [ "12 dB", 12 ],
                "24": [ "24 dB", 24 ]
            }
        },
        "resonance": {
            "path": "/reso",
            "class": endpoint.StandardKnob,
            "aliases": [ "reso" ]
        }
    }


class LFOSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "depth": {
            "path": "/lfo", # Documentation states 0..10 but it's 0..100
            "class": endpoint.PercentEndpoint,
            "aliases": [ "lfo" ]
        },
        "speed": {
            "path": "/spd",
            "class": endpoint.FloatEndpoint,
            "min": 0.05,
            "max": 20.0,
            "aliases": [ "spd" ]
        },
        "phase": {
            "path": "/phase",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 180
        },
        "wave": {
            "path": "/wave",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "TRI": "TRI",
                "SIN": "SIN",
                "SAW+": "SAW+",
                "SAW-": "SAW-",
                "RMP": "RAMP",
                "SQU": "SQUARE",
                "RND": "RANDOM"
            },
            "aliases": [ "wave_form", "waveform", "lfo_wave" ]
        }
    }


class MoodFilter(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "MOOD"

    @staticmethod
    def model_name() -> str:
        return "Mood Filter"

    _components = {
        "envelope": {
            "path": "",
            "class": EnvelopeSection,
            "aliases": [ "env" ]
        },
        "filter": {
            "path": "",
            "class": FilterSection,
            "aliases": [ "filt" ]
        },
        "lfo": {
            "path": "",
            "class": LFOSection
        }
    }

    _endpoints = {
        "drive": {
            "path": "/drv",
            "class": endpoint.StandardKnob,
            "aliases": [ "drv" ]
        },
        "mix": {
            "path": "/mix", # Documentation states 0..10 but it's 0..100
            "class": endpoint.PercentEndpoint
        }
    }
