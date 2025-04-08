"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class ColourSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "lo_eq": {
            "path": "/leq",
            "class": endpoint.StandardKnob,
            "aliases": [ "leq", "loeq", "low_eq" ]
        },
        "hi_eq": {
            "path": "/heq",
            "class": endpoint.StandardKnob,
            "aliases": [ "heq", "hieq", "high_eq" ]
        }
    }


class RackAmp(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "RACKAMP"

    @staticmethod
    def model_name() -> str:
        return "Rack Amp"

    _components = {
        "colour": {
            "path": "",
            "class": ColourSection,
            "aliases": [ "color", "col" ]
        }
    }

    _endpoints = {
        "pre_amp": {
            "path": "/pre",
            "class": endpoint.StandardKnob,
            "aliases": [ "pre", "preamp" ]
        },
        "buzz": {
            "path": "/buzz",
            "class": endpoint.StandardKnob
        },
        "punch": {
            "path": "/punch",
            "class": endpoint.StandardKnob
        },
        "crunch": {
            "path": "/crunch",
            "class": endpoint.StandardKnob
        },
        "drive": {
            "path": "/drive",
            "class": endpoint.StandardKnob
        },
        "out_gain": {
            "path": "/out",
            "class": endpoint.StandardKnob,
            "aliases": [ "out" ]
        },
        "cabinet_simulation": {
            "path": "/cab",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "cab", "cab_sim", "cabsim", "cabinet_sim", "cabinet", "cab_simulation" ]
        }
    }
