"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class NoStressor(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "NSTR"

    @staticmethod
    def model_name() -> str:
        return "No Stressor"

    _components = {}

    _endpoints = {
        "bypass": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "invert": True
        },
        "input": {
            "path": "/in",
            "class": endpoint.StandardKnob
        },
        "output": {
            # Documentation states path is "/ou", but console yields "/out"
            "path": "/out",
            "class": endpoint.StandardKnob,
            "aliases": [ "out" ]
        },
        "attack": {
            "path": "/att",
            "class": endpoint.StandardKnob,
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.StandardKnob,
            "aliases": [ "rel" ]
        },
        "ratio": {
            "path": "/ratio",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "1.5:1", "2:1", "3:1", "4:1", "6:1", "10:1", "20:1", "NUKE" ]
        }
    }
