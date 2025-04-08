"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin
from behringer_mixer.wing.plugins.effects.effect_sections import FilterSection


class StereoSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "width": {
            "path": "/wid",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "wid" ]
        },
        "diffusion": {
            "path": "/diff",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "diff" ]
        }
    }


class DelaySection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "time": {
            "path": "/time",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 2000.0
        },
        "factor": {
            "path": "/fact",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "1/3", "1/2", "2/3", "3/4", "1", "5/4", "4/3", "3/2", "2" ],
            "aliases": [ "fact" ]
        },
        "pre_delay": {
            "path": "/pdel",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 500.0,
            "aliases": [ "pdel" ]
        }
    }


class TrimBalanceSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "repeats": {
            "path": "/rep",
            "class": endpoint.IntEndpoint,
            "min": 1,
            "max": 16,
            "aliases": [ "rep", "repeat" ]
        },
        "slope": {
            "path": "/slp",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 6.0,
            "aliases": [ "slp" ]
        },
        "mode": {
            "path": "/mode",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "MOVE", "JUMP", "FOCUS", "SPREAD" ]
        }
    }


class UltraTapDelay(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "TAP-DL"

    @staticmethod
    def model_name() -> str:
        return "UltraTap Delay"

    _components = {
        "stereo": {
            "path": "",
            "class": StereoSection
        },
        "filter": {
            "path": "",
            "class": FilterSection
        },
        "delay": {
            "path": "",
            "class": DelaySection
        },
        "trim_balance": {
            "path": "",
            "class": TrimBalanceSection,
            "aliases": [ "trimbalance", "trim", "balance" ]
        }
    }

    _endpoints = {}
