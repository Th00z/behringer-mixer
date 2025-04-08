"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class Bodyrez(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "BODY"

    @staticmethod
    def model_name() -> str:
        return "Bodyrez"

    _components = {}

    _endpoints = {
        "body": {
            "path": "/body",
            "class": endpoint.PercentEndpoint
        }
    }
