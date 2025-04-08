"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class AmpBase(ConcretePlugin):
    """

    """
    _components = {}

    _endpoints = {
        "bass": {
            "path": "/bass",
            "class": endpoint.StandardKnob
        },
        "treble": {
            "path": "/treb",
            "class": endpoint.StandardKnob,
            "aliases": [ "treb" ]
        },
        "output_gain": {
            "path": "/out",
            "class": endpoint.StandardKnob,
            "aliases": [ "out_gain", "out" ]
        },
        "cabinet": {
            "path": "/cab",
            "class": endpoint.BoolEndpoint,
            "aliases": [
                "cab", "cab_sim", "cabsim", "cabinet_sim", "cab_simulation", "cabinet_simulation"
            ]
        }
    }


class MidAmpBase(AmpBase):
    """

    """

    _endpoints = deepcopy(AmpBase._endpoints)
    _endpoints.update({
        "middle": {
            "path": "/mid",
            "class": endpoint.StandardKnob,
            "aliases": [ "mid" ]
        }
    })
