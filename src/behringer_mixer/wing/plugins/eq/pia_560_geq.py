"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class GEQFader(endpoint.FloatEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(min=-12.0, max=12.0)


class PIA560GEQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "PIA"

    @staticmethod
    def model_name() -> str:
        return "PIA 560 GEQ"

    _components = {}

    _endpoints = {
        "mix": {
            "path": "/mix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 125.0
        },
        "gain": {
            "path": "/g",
            "class": GEQFader,
            "aliases": [ "g" ]
        },
        "hz31": {
            "path": "/31",
            "class": GEQFader
        },
        "hz63": {
            "path": "/63",
            "class": GEQFader
        },
        "hz125": {
            "path": "/125",
            "class": GEQFader
        },
        "hz250": {
            "path": "/250",
            "class": GEQFader
        },
        "hz500": {
            "path": "/500",
            "class": GEQFader
        },
        "khz1": {
            "path": "/1k",
            "class": GEQFader
        },
        "khz2": {
            "path": "/2k",
            "class": GEQFader
        },
        "khz4": {
            "path": "/4k",
            "class": GEQFader
        },
        "khz8": {
            "path": "/8k",
            "class": GEQFader
        },
        "khz16": {
            "path": "/16k",
            "class": GEQFader
        },
    }
