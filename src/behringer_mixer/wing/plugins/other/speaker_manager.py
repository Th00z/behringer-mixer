"""

"""
from copy import deepcopy

from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin
from behringer_mixer.wing.plugins.gate import DynamicEQ


class LimiterSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "active": {
            "path": "/lim",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "on", "enable", "lim" ]
        },
        "threshold": {
            "path": "/limthr",
            "class": endpoint.FloatEndpoint,
            "min": -24.0,
            "max": 0.0
        },
        "mode": {
            "path": "/limrms",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "RMS",
                False: "Peak"
            }
        },
        "rms": {
            "path": "/limrms",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "root_mean_square" ]
        },
        "peak": {
            "path": "/limrms",
            "class": endpoint.BoolEndpoint,
            "invert": True
        }
    }


class DEQSection(DynamicEQ):
    """

    """
    _endpoints = deepcopy(DynamicEQ._endpoints)
    _endpoints["threshold"].update({
        "path": "/deqthr",  # Documentation states "/dynthr", but it's "/deqthr"!
        "aliases": [ "thr", "deqthr" ]
    })
    _endpoints["ratio"].update({
        "path": "/deqratio",
        "aliases": [ "deqratio" ]
    })
    _endpoints["attack"].update({
        "path": "/deqatt",
        "aliases": [ "att", "deqatt" ]
    })
    _endpoints["release"].update({
        "path": "/deqrel",
        "aliases": [ "rel", "deqrel" ]
    })
    _endpoints["filter_types"].update({
        "path": "/deqfilt",
        "aliases": [ "filter_type", "filt", "deqfilt" ]
    })
    _endpoints["gain"].update({
        "path": "/deqg",
        "aliases": [ "g", "deqg" ]
    })
    _endpoints["freq"].update({
        "path": "/deqf",
        "aliases": [ "f", "frequency", "deqf" ]
    })
    _endpoints["q"].update({
        "path": "/deqq",
        "aliases": [ "deqq" ]
    })
    _endpoints["mode"].update({
        "path": "/deqmode",
        "aliases": [ "deqmode" ]
    })
    _endpoints["above"].update({
        "path": "/deqmode"
    })
    _endpoints["below"].update({
        "path": "/deqmode"
    })
    _endpoints.update({
        "dyn_eq": {
            "path": "/dyneq",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "On",
                False: "Off"
            }
        },
        "on": {
            "path": "/dyneq",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "enable" ]
        }
    })


class PassFilter(Component):
    """

    """
    _components = {}

    _endpoints = {
        "frequency": {
            "path": "f",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 20000.0,
            "aliases": [ "freq", "f" ]
        },
        "type": {
            "path": "type",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "FLAT": "FLAT",
                "BW6": "BUTTERWORTH 6 dB/Oct",
                "BW12": "BUTTERWORTH 12 dB/Oct",
                "BS12": "BESSEL 12 dB/Oct",
                "LR12": "LINKWITZ-RILEY 12 dB/Oct",
                "BW18": "BUTTERWORTH 18 dB/Oct",
                "BW24": "BUTTERWORTH 24 dB/Oct",
                "BS24": "BESSEL 24 dB/Oct",
                "LR24": "LINKWITZ-RILEY 24 dB/Oct",
                "BW48": "BUTTERWORTH 48 dB/Oct",
                "LR48": "LINKWITZ-RILEY 48 dB/Oct",
            }
        }
    }


class TiltFilter(Component):
    """

    """
    _components = {}

    _endpoints = {
        "freq": {
            "path": "f",
            "class": endpoint.FloatEndpoint,
            "min": 100.0,
            "max": 10000.0,
            "aliases": [ "frequency", "f", "tilt f" ]
        },
        "gain": {
            "path": "g",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 6.0,
            "aliases": [ "g", "tilt" ]
        }
    }


class FilterSection(Component):
    """

    """
    _components = {
        "high_pass": {
            "path": "/hp",
            "class": PassFilter,
            "aliases": [ "hp" ]
        },
        "tilt_eq": {
            "path": "/tilt",
            "class": TiltFilter,
            "aliases": [ "tilt" ]
        },
        "low_pass": {
            "path": "/lp",
            "class": PassFilter,
            "aliases": [ "lp" ]
        }
    }

    _endpoints = {
        "phase": {
            "path": "/phase",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 180.0
        },
        "polarity": {
            "path": "/invert",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "invert_polarity", "invert_phase", "invert" ]
        },
        "precision_delay": {
            "path": "/dist",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 5.0,
            "aliases": [ "dist", "distance" ]
        },
        "position": {
            "path": "/pos",
            "class": endpoint.FloatEndpoint,
            "min": -5.0,
            "max": 5.0,
            "aliases": [ "pos" ]
        }
    }


class SpeakerManager(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "SPKMAN"

    @staticmethod
    def model_name() -> str:
        return "Speaker Manager"

    _components = {
        "filter": {
            "path": "",
            "class": FilterSection
        },
        "dyn_eq": {
            "path": "",
            "class": DEQSection,
            "aliases":  [ "deq", "dyn" ]
        },
        "limiter": {
            "path": "",
            "class": LimiterSection,
            "aliases": [ "lim" ]
        }
    }

    _endpoints = {}
