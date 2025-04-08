"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class ExternalEffect(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "EXT"

    @staticmethod
    def model_name() -> str:
        return "External"

    _components = {}

    _endpoints = {
        "source_group": {
            "path": "/egrp",
            "class": endpoint.SourceGroupEndpoint,
            "aliases":  [ "group", "external_source_group", "external_group", "egrp" ]
        },
        "source_index": {
            "path": "/ein",
            "class": endpoint.IntEndpoint,
            "min": 1,
            "max": 64,
            "read_offset": 1,
            "aliases": [
                "group_index", "index", "input", "external_group_index", "external_index",
                "external_input", "ein"
            ]
        },
        "mode": {
            "path": "/emode",
            "class": endpoint.InputModeEndpoint,
            "aliases": [ "emode", "input_mode", "external_input_mode", "external_mode" ]
        },
        "latency": {
            "path": "/lat",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 200,
            "aliases": [ "lat" ]
        },
        "trim": {
            "path": "/trim",
            "class": endpoint.FloatEndpoint,
            "min": -18.0,
            "max": 18.0
        }
    }
