"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class Exciter(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "EXCITER"

    @staticmethod
    def model_name() -> str:
        return "Exciter"

    _components = {}

    _endpoints = {
        "tune": {
            "path": "/tune",
            "class": endpoint.FloatEndpoint,
            "min": 1000.0,
            "max": 10000.0
        },
        "peak": {
            "path": "/peak",
            "class": endpoint.PercentEndpoint
        },
        "zero_fill": {
            "path": "/zero",  # Documentation states /zfill, but it's actually this!
            "class": endpoint.PercentEndpoint,
            "aliases": [ "zero" ]
        },
        "timbre": {
            "path": "/tmb",  # Documentation states /timbre, but it's actually this!
            "class": endpoint.FloatEndpoint,
            "min": -50.0,
            "max": 50.0,
            "aliases": [ "tmb" ]
        },
        "harmonics": {
            "path": "/hrm",  # Documentation states /harm, but it's actually this!
            "class": endpoint.PercentEndpoint,
            "aliases": [ "hrm" ]
        },
        "dry": {
            "path": "/solo",  # Documentation states /dry, but it's actually this!
            "class": endpoint.BoolEndpoint,
            "aliases": [ "solo" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.PercentEndpoint
        }
    }
