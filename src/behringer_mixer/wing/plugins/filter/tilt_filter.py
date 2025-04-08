"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .base_filter import BaseFilter


class TiltFilter(BaseFilter):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "TILT"

    @staticmethod
    def model_name() -> str:
        return "Tilt Filter"

    _endpoints = deepcopy(BaseFilter._endpoints)
    _endpoints.update({
        "tilt": {
            "path": "/tilt",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 6.0
        }
    })
