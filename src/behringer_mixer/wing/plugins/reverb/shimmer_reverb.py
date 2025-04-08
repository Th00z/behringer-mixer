"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class ShimmerReverb(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "SHIMMER"

    @staticmethod
    def model_name() -> str:
        return "Shimmer Reverb"

    _components = {}

    _endpoints = {
        "pre_delay": {
            "path": "/pdel",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 250,
            "aliases": [ "pdel" ]
        },
        "size": {
            "path": "/size",
            "class": endpoint.IntEndpoint,
            "min": 2,
            "max": 50
        },
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 20.0,
            "aliases": [ "dcy" ]
        },
        "lo_cut": {
            "path": "/lc",
            "class": endpoint.FloatEndpoint,
            "min": 25.0,
            "max": 250.0,
            "aliases": [ "lc", "low_cut", "hp", "hi_pass", "high_pass" ]
        },
        "hi_cut": {
            "path": "/hc",
            "class": endpoint.FloatEndpoint,
            "min": 500.0,
            "max": 7000.0,
            "aliases": [ "hc", "high_cut", "lp", "lo_pass", "low_pass" ]
        },
        "damping": {
            "path": "/damp",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "damp" ]
        },
        "shimmer": {
            "path": "/shim",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "shim" ]
        },
        "shine": {
            "path": "/shine",
            "class": endpoint.PercentEndpoint
        }
    }
