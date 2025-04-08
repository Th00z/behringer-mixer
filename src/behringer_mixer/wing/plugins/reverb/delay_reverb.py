"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class DelaySection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "time": {
            "path": "/time",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 3000.0
        },
        "feedback": {
            "path": "/feed",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "feed" ]
        },
        "hicut": {
            "path": "/fhc",  # Documentation says 200...2000, there's a 0 missing.
            "class": endpoint.FXHighCutEndpoint,
            "aliases": [
                "fhc", "hi_cut", "high_cut", "feed_hc", "feed_hi_cut", "feedback_high_cut",
                "lp", "lo_pass", "low_pass"
            ]
        },
        "level": {
            "path": "/dly",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "dly", "dly_lvl", "delay", "delay_level" ]
        }
    }


class ReverbSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "delay": {
            "path": "/d2r",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "d2r", "dly_to_rev", "delay_to_reverb", "delay_input" ]
        },
        "predel": {
            "path": "/pdel",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 200,
            "aliases": [ "pdel", "pre_dly", "pre_delay" ]
        },
        "size": {
            "path": "/size",
            "class": endpoint.IntEndpoint,
            "min": 2,
            "max": 100
        },
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 5.0,
            "aliases": [ "dcy" ]
        },
        "damping": {
            "path": "/damp",
            "class": endpoint.FloatEndpoint,
            "min": 1000.0,
            "max": 20000.0,
            "aliases": [ "damp" ]
        },
        "locut": {
            "path": "/rlc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [
                "rlc", "rev_lc", "rev_lcut", "lo_cut", "low_cut", "hp", "hi_pass", "high_pass"
            ]
        },
        "direct": {
            "path": "/i2r",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "i2r", "in_to_rev", "input_to_reverb", "direct_input" ]
        }
    }


class DelayReverb(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "DEL/REV"

    @staticmethod
    def model_name() -> str:
        return "Delay/Reverb"

    _components = {
        "delay": {
            "path": "",
            "class": DelaySection
        },
        "reverb": {
            "path": "",
            "class": ReverbSection
        }
    }

    _endpoints = {}
