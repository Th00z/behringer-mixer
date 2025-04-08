"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class SubOctaver(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "SUB"

    @staticmethod
    def model_name() -> str:
        return "Sub Octaver"

    _components = {}

    _endpoints = {
        "range": {
            "path": "/rng",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "LOW", "MID", "HIGH" ],
            "aliases": [ "rng" ]
        },
        "octave_1": {
            "path": "/oct1",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "oct1" ]
        },
        "octave_2": {
            "path": "/oct2",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "oct2" ]
        }
    }
