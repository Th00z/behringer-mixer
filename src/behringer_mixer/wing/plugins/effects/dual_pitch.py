"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin, PostIndexedComponent


class PitchSection(PostIndexedComponent):
    """

    """
    _components = {}

    _endpoints = {
        "semitones": {
            "path": "/semi{index}",
            "class": endpoint.IntEndpoint,
            "min": -12,
            "max": 12,
            "aliases": [ "semi" ]
        },
        "cents": {
            "path": "/cent{index}",
            "class": endpoint.IntEndpoint,
            "min": -50,
            "max": 50,
            "read_offset": -50,
            "write_offset": 1,
            "aliases": [ "cent" ]
        },
        "delay": {
            "path": "/dly{index}",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 500.0,
            "aliases": [ "dly" ]
        },
        "pan": {
            "path": "/pan{index}",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0
        },
        "level": {
            "path": "/lvl{index}",
            "class": endpoint.FaderEndpoint,
            "aliases": [ "lvl" ]
        },
    }


class DualPitch(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "D-PITCH"

    @staticmethod
    def model_name() -> str:
        return "Dual Pitch"

    _components = {
        "a": {
            "path": "",
            "class": PitchSection,
            "index": 1
        },
        "b": {
            "path": "",
            "class": PitchSection,
            "index": 2
        }
    }

    _endpoints = {
        "locut": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc", "lo_cut", "low_cut", "hp", "hi_pass", "high_pass" ]
        },
        "hicut": {
            "path": "/hc",
            "class": endpoint.FXHighCutEndpoint,
            "aliases": [ "hc", "hi_cut", "high_cut", "lp", "lo_pass", "low_pass" ]
        }
    }
