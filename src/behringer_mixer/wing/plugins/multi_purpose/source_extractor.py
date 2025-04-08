"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class SourceExtractor(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "PSE"

    @staticmethod
    def model_name() -> str:
        return "Source Extractor"

    _components = {}

    _endpoints = {
        "threshold": {
            "path": "/thr",
            "class": endpoint.FloatEndpoint,
            "min": -36.0,
            "max": 12.0,
            "aliases": [ "thr" ]
        },
        "depth": {
            "path": "/depth",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 20.0
        },
        "fast": {
            "path": "/fast",
            "class": endpoint.BoolEndpoint
        },
        "peak": {
            "path": "/peak",
            "class": endpoint.BoolEndpoint
        }
    }
