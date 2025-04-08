"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class PitchFix(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "PCORR"

    @staticmethod
    def model_name() -> str:
        return "Pitch Fix"

    _components = {}

    _endpoints = {
        "speed": {
            "path": "/spd",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 100.0,
            "aliases": [ "spd" ]
        },
        "amount": {
            "path": "/amnt",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 50.0,
            "aliases": [ "amnt" ]
        },
        "a4_pitch": {
            "path": "/a4",
            "class": endpoint.FloatEndpoint,
            "min": 410.0,
            "max": 470.0,
            "aliases": [ "a4", "a4pitch", "pitch" ]
        },
        # All the following enpoints are missing the "sw"-prefix in the documentation!
        "c": {
            "path": "/sw_c",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_c" ]
        },
        "d_flat": {
            "path": "/sw_db",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_db", "c_sharp", "db", "cs", "des", "cis" ]
        },
        "d": {
            "path": "/sw_d",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_d" ]
        },
        "e_flat": {
            "path": "/sw_eb",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_eb", "d_sharp", "eb", "ds", "es", "dis" ]
        },
        "e": {
            "path": "/sw_e",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_e" ]
        },
        "f": {
            "path": "/sw_f",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_f" ]
        },
        "g_flat": {
            "path": "/sw_gb",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_gb", "f_sharp", "gb", "fs", "ges", "fis" ]
        },
        "g": {
            "path": "/sw_g",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_g" ]
        },
        "a_flat": {
            "path": "/sw_ab",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_ab", "g_sharp", "ab", "gs", "aes", "gis" ]
        },
        "a": {
            "path": "/sw_a",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_a" ]
        },
        "b_flat": {
            "path": "/sw_bb",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_bb", "a_sharp", "bb", "as", "ais" ]
        },
        "b": {
            "path": "/sw_b",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sw_b", "h", "sw_h" ]
        }
    }
