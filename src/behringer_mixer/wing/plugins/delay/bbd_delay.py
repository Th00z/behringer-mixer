"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class BBDDelay(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "BBD-DL"

    @staticmethod
    def model_name() -> str:
        return "BBD Delay"

    _components = {}

    _endpoints = {
        "delay": {
            "path": "/dly",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "dly" ]
        },
        "feedback": {
            "path": "/fb",  # Documentation states "/feed" but console clearly yields "/fb"
            "class": endpoint.PercentEndpoint,
            "aliases": [ "fb" ]
        }
    }
