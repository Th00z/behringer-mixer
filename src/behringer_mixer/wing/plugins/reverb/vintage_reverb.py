"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class VintageReverb(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "V-REV"

    @staticmethod
    def model_name() -> str:
        return "Vintage Reverb"

    _components = {}

    _endpoints = {
        "predelay": {
            "path": "/pdel",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 120,
            "aliases": [ "pdel", "pre_delay" ]
        },
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.4,
            "max": 4.5,
            "aliases": [ "dcy" ]
        },
        "lo_multi": {
            "path": "/lmult",
            "class": endpoint.FloatEndpoint,
            "min": 0.5,
            "max": 2.0,
            "aliases": [ "lmult", "low_multiplier" ]
        },
        "hi_multi": {
            "path": "/hmult",
            "class": endpoint.FloatEndpoint,
            "min": 0.25,
            "max": 0.68,
            "aliases": [ "hmult", "high_multiplier" ]
        },
        "modulate": {
            "path": "/mod",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "mod", "modulation_speed" ]
        },
        "lo_cut": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc" ]
        },
        "hi_cut": {
            "path": "/hc",
            "class": endpoint.FloatEndpoint,
            "min": 5000.0,
            "max": 20000.0,
            "aliases": [ "hc" ]
        },
        "output": {
            "path": "/out",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "FRONT": "FRONT",
                "REAR": "BACK"
            },
            "aliases": [ "out" ]
        },
        "transformer": {
            "path": "/trans",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "ON",
                False: "OFF"
            },
            "aliases": [ "trans" ]
        }
    }
