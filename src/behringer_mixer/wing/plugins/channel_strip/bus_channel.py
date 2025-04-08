"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from behringer_mixer.wing.plugins.gate import SoulWarmthPreamp
from behringer_mixer.wing.plugins.eq import Even84EQ
from behringer_mixer.wing.plugins.dyn import SoulGBusCompressor


class ChannelGate(SoulWarmthPreamp):
    """

    """
    _endpoints = deepcopy(SoulWarmthPreamp._endpoints)
    for endpoint in _endpoints:
        _endpoints[endpoint].update({ "path": _endpoints[endpoint]["path"].removeprefix("/") })


class ChannelEQ(Even84EQ):
    """

    """
    _endpoints = deepcopy(Even84EQ._endpoints)
    _endpoints.update({
        "on": {
            "path": "/eq_on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "eq_on" ]
        }
    })


class ChannelCompressor(SoulGBusCompressor):
    """

    """
    _endpoints = deepcopy(SoulGBusCompressor._endpoints)
    for endpoint in _endpoints:
        _endpoints[endpoint].update({ "path": _endpoints[endpoint]["path"].removeprefix("/") })


class BusChannel(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "*BUS*"

    @staticmethod
    def model_name() -> str:
        return "Bus Channel"

    _components = {
        "warm": {
            "path": "/w_",
            "class": ChannelGate,
            "aliases": [
                "w", "warmth", "soul_warmth_preamp", "soul_warmth", "gate", "preamp"
            ]
        },
        "eq": {
            "path": "",
            "class": ChannelEQ,
            "aliases": [ "e84", "e84_eq", "even_84", "even_84_eq" ]
        },
        "dyn": {
            "path": "/d_",
            "class": ChannelCompressor,
            "aliases": [
                "d", "dynamics", "c", "compressor", "bus_compressor", "g_bus_compressor",
                "soul_g_bus_compressor"
            ]
        }
    }

    _endpoints = {}
