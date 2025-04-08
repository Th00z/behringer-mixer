"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint


class EnvelopeSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 10.0,
            "max": 1000.0,
            "aliases": [ "att" ]
        },
        "hold": {
            "path": "/hld",
            "class": endpoint.FloatEndpoint,
            "min": 10.0,
            "max": 2000.0,
            "aliases": [ "hld" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 10.0,
            "max": 1000.0,
            "aliases": [ "rel" ]
        }
    }


class LFOSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "speed": {
            "path": "/spd",
            "class": endpoint.FloatEndpoint,
            "min": 0.05,
            "max": 5.0,
            "aliases": [ "spd" ]
        },
        "phase": {
            "path": "/phase",
            "class": endpoint.IntEndpoint,
            "min": -180, # Documentation states 0...180 but it's actually -180..180
            "max": 180,
            "read_offset": -180,
            "write_offset": 1,
            "aliases": [ "phase_l_r", "phase_lr" ]
        },
        "shape": {
            "path": "/wave",
            "class": endpoint.IntEndpoint,
            "min": -50,
            "max": 50,
            "aliases": [ "wave", "wave_form", "waveform" ]
        }
    }


class FilterSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "lo_cut": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc", "low_cut", "hp", "hi_pass", "high_pass" ]
        },
        "hi_cut": {
            "path": "/hc",
            "class": endpoint.FXHighCutEndpoint,
            "aliases": [ "hc", "high_cut", "lp", "lo_pass", "low_pass" ]
        }
    }
