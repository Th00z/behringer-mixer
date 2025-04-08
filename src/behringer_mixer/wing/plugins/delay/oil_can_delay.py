"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class OilCanDelay(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "OILCAN"

    @staticmethod
    def model_name() -> str:
        return "OilCan Delay"

    _components = {}

    _endpoints = {
        "time": {
            "path": "/time",
            "class": endpoint.StandardKnob,
        },
        "sustain": {
            "path": "/sust",
            "class": endpoint.StandardKnob,
            "aliases": [ "sust" ]
        },
        "wobble": {
            "path": "/wb",
            "class": endpoint.StandardKnob,
            "aliases": [ "wb" ]
        },
        "tone": {
            "path": "/tone",
            "class": endpoint.StandardKnob
        }
    }
