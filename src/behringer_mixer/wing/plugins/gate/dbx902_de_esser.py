"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class DBX902DeEsser(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "DS902"

    @staticmethod
    def model_name() -> str:
        return "DBX 902 De-Esser"

    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "solo": {
            "path": "sc/$solo",
            "class": endpoint.BoolEndpoint
        },
        "mode": {
            "path": "/mode",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "FULL", "HF" ]
        },
        "hf_only": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "FULL": False,
                "HF": True
            }
        },
        "frequency": {
            "path": "/f",
            "class": endpoint.FloatEndpoint,
            "min": 800.0,
            "max": 8000.0,
            "aliases": [ "freq", "f" ]
        },
        "range": {
            "path": "/range",
            "class": endpoint.FloatEndpoint,
            "min": 3.0,
            "max": 12.0
        },
    }
