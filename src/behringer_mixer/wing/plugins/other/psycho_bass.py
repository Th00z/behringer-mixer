"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class PsychoBass(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "P-BASS"

    @staticmethod
    def model_name() -> str:
        return "Psycho Bass"

    _components = {}

    _endpoints = {
        "intensity": {
            "path": "/int",
            "class": endpoint.FloatEndpoint,
            "min": -24.0,
            "max": 6.0,
            "aliases": [ "int" ]
        },
        "bass_gain": {
            "path": "/bass",
            "class": endpoint.FloatEndpoint,
            "min": -60.0,
            "max": 0.0,
            "aliases": [ "bass" ]
        },
        "x_o_frequency": {
            "path": "/xf",
            "class": endpoint.FloatEndpoint,
            "min": 32.0,
            "max": 200.0,
            "aliases": [
                "xo_frequency", "xf", "x_o", "xo", "x_o_freq", "xo_freq", "x_o_f", "xo_f", "xof"
            ]
        },
        "solo": {
            "path": "/solo",
            "class": endpoint.BoolEndpoint
        }
    }
