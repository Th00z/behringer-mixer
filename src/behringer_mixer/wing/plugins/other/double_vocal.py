"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class DoubleVocal(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "DOUBLE"

    @staticmethod
    def model_name() -> str:
        return "Double Vocal"

    _components = {}

    _endpoints = {
        "mode": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "TIGHT": "Tight",
                "LOOSE": "Loose",
                "GROUP": "Group",
                "DETUNE": "Detune",
                "THICK": "Thick"
            }
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.PercentEndpoint
        },
        "spread": {
            "path": "/sprd",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "sprd" ]
        }
    }
