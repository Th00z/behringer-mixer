"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from behringer_mixer.wing.plugins.multi_purpose import LimitingAmp76, LevelingAmplifier2A
from behringer_mixer.wing.plugins.eq import PulsarP1aM5EQ


class ChannelDyn(LimitingAmp76):
    """

    """
    _endpoints = deepcopy(LimitingAmp76._endpoints)
    for ep in _endpoints:
        _endpoints[ep].update({ "path": _endpoints[ep]["path"].removeprefix("/") })
    _endpoints.update({
        "on": {
            "path": "on",
            "class": endpoint.BoolEndpoint
        }
    })


class ChannelLevel(LevelingAmplifier2A):
    """

    """
    _endpoints = deepcopy(LevelingAmplifier2A._endpoints)
    for endpoint in _endpoints:
        _endpoints[endpoint].update({ "path": _endpoints[endpoint]["path"].removeprefix("/") })


class VintageChannel(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "*VINTAGE*"

    @staticmethod
    def model_name() -> str:
        return "Vintage Channel"

    _components = {
        "dyn": {
            "path": "/d_",
            "class": ChannelDyn,
            "aliases": [ "d", "dynamics", "la76", "la_76", "limiting_amp_76", "limiter" ]
        },
        "eq": {
            "path": "",
            "class": PulsarP1aM5EQ,
            "aliases": [ "pulsar", "pulsar_eq", "pulsar_p1a_m5_eq" ]
        },
        "lvl": {
            "path": "/l_",
            "class": ChannelLevel,
            "aliases": [
                "l", "level", "leveling", "leveling_amp", "leveling_amplifier", "la", "la2a",
                "la_2a", "leveling_amplifier_2a"
            ]
        }
    }

    _endpoints = {}
