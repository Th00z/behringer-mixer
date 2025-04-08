"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .base_filter import BaseFilter


class MaximizerFilter(BaseFilter):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "MAX"

    @staticmethod
    def model_name() -> str:
        return "Maxer Filter"

    _endpoints = deepcopy(BaseFilter._endpoints)
    _endpoints.update({
        "low_contour": {
            "path": "/low",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 100.0,
            "aliases": [ "low" ]
        },
        "high_process": {
            "path": "/proc",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 100.0,
            "aliases": [ "proc" ]
        }
    })
