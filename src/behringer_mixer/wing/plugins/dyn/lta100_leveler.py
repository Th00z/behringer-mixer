"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class LTA100Leveler(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "L100"

    @staticmethod
    def model_name() -> str:
        return "LTA100 Leveler"

    _components = {}

    _endpoints = {
        "gain": {
            "path": "/ingain",
            "class": endpoint.StandardKnob,
            "aliases": [ "ingain" ]
        },
        "gain_reduction": {
            "path": "/gr",
            "class": endpoint.StandardKnob,
            "aliases": [ "gr" ]
        },
        "attack": {
            "path": "/att",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "FAST", "MED", "SLOW" ],
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "FAST", "MED", "SLOW" ],
            "aliases": [ "rel" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 100.0,
            "aliases": [ "dry_wet" ]
        }
    }
