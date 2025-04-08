"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class VintageRoom(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "V-ROOM"

    @staticmethod
    def model_name() -> str:
        return "Vintage Room"

    _components = {}

    _endpoints = {
        "rcv_delay": {
            "path": "/pdel",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 200,
            "aliases": [ "pdel", "pre_delay" ]
        },
        "room_size": {
            "path": "/size",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 50,
            "aliases": [ "size" ]
        },
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 20.0,
            "aliases": [ "dcy" ]
        },
        "density": {
            "path": "/dens",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 30.0,
            "aliases": [ "dens" ]
        },
        "er_level": {
            "path": "/erlvl",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 100.0,
            "aliases": [ "erlvl", "early_level" ]
        },
        "low_multiply": {
            "path": "/lmult",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 10.0,
            "aliases": [ "lmult", "low_multiplier" ]
        },
        "high_multiply": {
            "path": "/hmult",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 10.0,
            "aliases": [ "hmult", "high_multiplier" ]
        },
        "low_cut": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc" ]
        },
        "high_cut": {
            "path": "/hc",
            "class": endpoint.FXHighCutEndpoint,
            "aliases": [ "hc" ]
        },
        "freeze": {
            "path": "/frz",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "frz" ]
        },
        "er_delay_l": {
            "path": "/erl",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 200.0,
            "aliases": [ "erl", "er_delay_left", "early_delay_l", "early_delay_left" ]
        },
        "er_delay_r": {
            "path": "/err",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 200.0,
            "aliases": [ "err", "er_delay_right", "early_delay_r", "early_delay_right" ]
        },
        "add": {
            "path": "/add",
            "class": endpoint.BoolEndpoint
        },
        "level": {
            "path": "/lvl",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 6.0,
            "aliases": [ "lvl" ]
        }
    }
