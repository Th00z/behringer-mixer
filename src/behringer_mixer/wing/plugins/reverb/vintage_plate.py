"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class VintagePlate(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "V-PLATE"

    @staticmethod
    def model_name() -> str:
        return "Vintage Plate"

    _components = {}

    _endpoints = {
        "pre_delay": {
            "path": "/pdel",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 250,
            "aliases": [ "pdel" ]
        },
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 6.0,
            "aliases": [ "dcy" ]
        },
        "filter": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc", "low_cut" ]
        },
        "colour": {
            "path": "/col",
            "class": endpoint.FloatEndpoint,
            "min": -20.0,
            "max": 20.0,
            "aliases": [ "col", "color" ]
        }
    }
