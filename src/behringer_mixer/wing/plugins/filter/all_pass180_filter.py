"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .base_filter import BaseFilter


class AllPass180Filter(BaseFilter):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "AP2"

    @staticmethod
    def model_name() -> str:
        return "AP180 Filter (all pass)"

    _endpoints = deepcopy(BaseFilter._endpoints)
    _endpoints.update({
        "frequency": {
            "path": "/f",
            "class": endpoint.FloatEndpoint,
            "min": 100.0,
            "max": 10000.0,
            "aliases": [ "f" ]
        },
        "q": {
            "path": "/q",
            "class": endpoint.FloatEndpoint,
            "min": 0.442,
            "max": 10.0
        }
    })
