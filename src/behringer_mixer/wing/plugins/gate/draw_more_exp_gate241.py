"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class DrawMoreExpGate241(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "D241"

    @staticmethod
    def model_name() -> str:
        return "DrawMore Expander Gate 241"

    _components = {}

    _endpoints = {
        "bypass": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "invert": True
        },
        "threshold": {
            "path": "/thr",
            "class": endpoint.FloatEndpoint,
            "min": -80.0,
            "max": 0.0,
            "aliases": [ "thr" ]
        },
        "release": {
            "path": "/slow",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "Slow",
                False: "Fast"
            }
        },
        "slow": {
            "path": "/slow",
            "class": endpoint.BoolEndpoint
        }
    }
