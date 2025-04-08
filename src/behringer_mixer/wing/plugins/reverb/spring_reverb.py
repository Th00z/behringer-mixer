"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class SpringReverb(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "SPRING"

    @staticmethod
    def model_name() -> str:
        return "Spring Reverb"

    _components = {}

    _endpoints = {
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 1.5,
            "max": 6.0,
            "aliases": [ "dcy" ]
        },
        "density": {
            "path": "/dens",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 30.0,
            "aliases": [ "dens" ]
        },
        "bass": {
            "path": "/low",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 50.0,
            "aliases": [ "low" ]
        },
        "treble": {
            "path": "/high",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 50.0,
            "aliases": [ "high" ]
        }
    }
