"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .base_filter import BaseFilter


class AllPass90Filter(BaseFilter):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "AP1"

    @staticmethod
    def model_name() -> str:
        return "AP90 Filter (all pass)"

    _endpoints = deepcopy(BaseFilter._endpoints)
    _endpoints.update({
        "frequency": {
            "path": "/f", # Documentation says "freq" but it's actually just f
            "class": endpoint.FloatEndpoint,
            "min": 100.0,
            "max": 10000.0,
            "aliases": [ "f", "freq" ]
        }
    })
