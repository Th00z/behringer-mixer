"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class PIA2250(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "2250"

    @staticmethod
    def model_name() -> str:
        return "PIA 2250"

    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "tresh": {
            "path": "/thr",
            "class": endpoint.StandardKnob,
            "aliases": [ "threshold" ]
        },
        "ratio": {
            "path": "/ratio",
            "class": endpoint.StandardKnob
        },
        "attack": {
            "path": "/att",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "FAST", "MED", "SLOW" ],
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 50.0,
            "max": 3000.0,
            "aliases": [ "rel" ]
        },
        "knee": {
            "path": "/knee",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "HARD", "SOFT" ]
        },
        "type": {
            "path": "/Type",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "OLD", "NEW" ]
        }
    }
