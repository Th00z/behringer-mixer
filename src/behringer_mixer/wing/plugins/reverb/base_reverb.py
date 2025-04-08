"""

"""
from copy import deepcopy
from abc import ABC

from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class BaseReverb(ConcretePlugin, ABC):
    """

    """
    _components = {}

    _endpoints = {
        "pre_dly": {
            "path": "/pdel",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 200,
            "aliases": [ "pdel", "pre_delay" ]
        },
        "size": {
            "path": "/size",
            "class": endpoint.FloatEndpoint,
            "min": 4.0,
            "max": 76.0
        },
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.3,
            "aliases": [ "dcy" ]
        },
        "damping": {
            "path": "/damp",
            "class": endpoint.FloatEndpoint,
            "min": 1000.0,
            "max": 20000.0,
            "aliases": [ "damp" ]
        },
        "lo_cut": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc", "low_cut", "hp", "hi_pass", "high_pass" ]
        },
        "hi_cut": {
            "path": "/hc",
            "class": endpoint.FXHighCutEndpoint,
            "aliases": [ "hc", "high_cut", "lp", "lo_pass", "low_pass" ]
        },
        "diffusion": {
            "path": "/diff",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "diff" ]
        }
    }


class BaseBMReverb(BaseReverb, ABC):
    """

    """
    _endpoints = deepcopy(BaseReverb._endpoints)
    _endpoints.update({
        "bass_mult": {
            "path": "/mult",
            "class": endpoint.FloatEndpoint,
            "min": 0.25,
            "max": 4.0,
            "aliases": [ "mult", "bass_multiplier", "bass" ]
        },
        "spread": {
            "path": "/sprd",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 50,
            "aliases": [ "sprd" ]
        }
    })


class BaseShapedReverb(BaseBMReverb, ABC):
    """

    """
    _endpoints = deepcopy(BaseBMReverb._endpoints)
    _endpoints.update({
        "shape": {
            "path": "/shp",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "aliases": [ "shp" ]
        }
    })


class HighShelvSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "freq": {
            "path": "f",  # There's a typo in the documentaion : "hfs" instead of "hsf"
            "class": endpoint.FloatEndpoint,
            "min": 200.0,
            "max": 20000.0,
            "aliases": [ "hsf", "frequency", "high_freq", "high_shelv_frequency" ]
        },
        "gain": {
            "path": "g",
            "class": endpoint.FloatEndpoint,
            "min": -30.0,
            "max": 0.0,
            "aliases": [ "hsg", "high_gain", "high_shelv_gain" ]
        }
    }


class DigitalReverb(ConcretePlugin, ABC):
    """

    """
    _components = {
        "high_shelv": {
            "path": "/hs",
            "class": HighShelvSection
        }
    }

    _endpoints = {
        "pre_delay": {
            "path": "/pdel",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 200,
            "aliases": [ "pdel" ]
        },
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.14,
            "max": 1.0,
            "aliases": [ "dcy" ]
        },
        "diffuse": {
            "path": "/diff",
            "class": endpoint.IntEndpoint,
            "min": 1,  # Documention says 0...30 on one plugin and 0...100 on the other
            "max": 30, # but it's actually neither...
            "aliases": [ "diff", "diffusion" ]
        },
        "spread": {
            "path": "/sprd",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100, # Documentation says 50 on one plugin but console yields 100 on all.
            "aliases": [ "sprd" ]
        },
        "lo_cut": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc", "low_cut", "hp", "hi_pass", "high_pass" ]
        }
    }
