"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class BluePlate(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "BPLATE"

    @staticmethod
    def model_name() -> str:
        return "Blue Plate"

    _components = {}

    _endpoints = {
        "predelay": {
            "path": "/pdel",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 200,
            "aliases": [ "pdel", "pre_dly", "pre_delay" ]
        },
        "size": {
            "path": "/size",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100
        },
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.2,
            "max": 5.0,
            "aliases": [ "dcy" ]
        },
        "bassmult": {
            "path": "/mult",
            "class": endpoint.FloatEndpoint,
            "min": 0.5,
            "max": 2.0,
            "aliases": [ "mult", "bass_mult", "bass_multiplier", "multiplier" ]
        },
        "damping": {
            "path": "/damp",
            "class": endpoint.FloatEndpoint,
            "min": 1000.0,
            "max": 20000.0,
            "aliases": [ "damp" ]
        },
        "locut": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc", "lo_cut", "low_cut", "hp", "hi_pass", "high_pass" ]
        },
        "hicut": {
            "path": "/hc",
            "class": endpoint.FXHighCutEndpoint,
            "aliases": [ "hc", "hi_cut", "high_cut", "lp", "lo_pass", "low_pass" ]
        },
        "xover": {
            "path": "/xover",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 500.0,
            "aliases": [ "crossover" ]
        },
        "mod": {
            "path": "/mdep",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 50.0,
            "aliases": [ "mdep", "mod_depth", "modulation", "modulation_depth" ]
        },
        "spd": {
            "path": "/mspd", # Documentation has a typo: "msdp" instead of "mspd"
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "mspd", "mod_spd", "speed", "modulation_speed" ]
        },
        "diff": {
            "path": "/diff",
            "class": endpoint.IntEndpoint,
            "min": 1,
            "max": 30,
            "aliases": [ "diffusion" ]
        }
    }
