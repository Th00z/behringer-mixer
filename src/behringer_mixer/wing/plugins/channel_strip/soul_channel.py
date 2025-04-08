"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from behringer_mixer.wing.plugins.gate import SSL9000Gate
from behringer_mixer.wing.plugins.eq import SoulAnalogEQ
from behringer_mixer.wing.plugins.dyn import Soul9000ChannelCompressor


class ChannelGate(SSL9000Gate):
    """

    """
    _endpoints = deepcopy(SSL9000Gate._endpoints)
    for endpoint in _endpoints:
        _endpoints[endpoint].update({ "path": _endpoints[endpoint]["path"].removeprefix("/") })


class ChannelEQ(SoulAnalogEQ):
    """

    """
    _endpoints = deepcopy(SoulAnalogEQ._endpoints)
    _endpoints.update({
        "on": {
            "path": "/eq_on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "eq_on" ]
        }
    })


class ChannelCompressor(Soul9000ChannelCompressor):
    """

    """
    _endpoints = deepcopy(Soul9000ChannelCompressor._endpoints)
    for endpoint in _endpoints:
        _endpoints[endpoint].update({ "path": _endpoints[endpoint]["path"].removeprefix("/") })


class SoulChannel(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "*SOUL*"

    @staticmethod
    def model_name() -> str:
        return "Soul Channel"

    _components = {
        "gate": {
            "path": "/g_",
            "class": ChannelGate,
            "aliases": [
                "g", "g9000", "g_9000", "gate_9000", "ssl9000_gate_expander",
                "soul9000_gate_expander", "gate_expander_9000"
            ]
        },
        "eq": {
            "path": "",
            "class": ChannelEQ,
            "aliases": [ "soul", "soul_analog_eq", "soul_analogue_eq" ]
        },
        "dyn": {
            "path": "/d_",
            "class": ChannelCompressor,
            "aliases": [ "d", "c9000", "c_9000", "compressor_9000", "soul_9000_channel_compressor" ]
        }
    }

    _endpoints = {}
