"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from behringer_mixer.wing.plugins.gate import Even88Gate
from behringer_mixer.wing.plugins.eq import Even88FormantEQ
from behringer_mixer.wing.plugins.dyn.even_compressor_limiter import (
    EvenCompressor, EvenLimiter, EvenCompressorLimiter
)


class ChannelGate(Even88Gate):
    """

    """
    _endpoints = deepcopy(Even88Gate._endpoints)
    for endpoint in _endpoints:
        _endpoints[endpoint].update({ "path": _endpoints[endpoint]["path"].removeprefix("/") })


class ChannelEQ(Even88FormantEQ):
    """

    """
    _endpoints = deepcopy(Even88FormantEQ._endpoints)
    _endpoints.update({
        "on": {
            "path": "/eq_on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "eq_on" ]
        }
    })


class ChannelCompressor(EvenCompressor):
    """

    """
    _endpoints = deepcopy(EvenCompressor._endpoints)
    for ep in _endpoints:
        _endpoints[ep].update({ "path": _endpoints[ep]["path"].removeprefix("/") })
    _endpoints["gain"].update({
        "path": "gain"
    })


class ChannelLimiter(EvenLimiter):
    """

    """
    _endpoints = deepcopy(EvenLimiter._endpoints)
    for endpoint in _endpoints:
        _endpoints[endpoint].update({ "path": _endpoints[endpoint]["path"].removeprefix("/") })


class ChannelCompressorLimiter(EvenCompressorLimiter):
    """

    """
    _components = deepcopy(EvenCompressorLimiter._components)
    _components["limit"].update({ "class": ChannelLimiter })
    _components["compress"].update({ "class": ChannelCompressor })

    _endpoints = deepcopy(EvenCompressorLimiter._endpoints)
    del _endpoints["power"]


class EvenChannel(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "*EVEN*"

    @staticmethod
    def model_name() -> str:
        return "Even Channel"

    _components = {
        "gate": {
            "path": "/g_",
            "class": ChannelGate,
            "aliases": [ "g", "e88g", "e88_g", "e88_gate", "even_88_gate", "gate_88" ]
        },
        "eq": {
            "path": "",
            "class": ChannelEQ,
            "aliases": [ "e88eq", "e88_eq", "even_88_formant_eq", "formant_eq_88", "formant_eq" ]
        },
        "dyn": {
            "path": "/d_",
            "class": ChannelCompressorLimiter,
            "aliases": [ "d", "ecl33", "even_compressor_limiter", "compressor_limiter" ]
        }
    }

    _endpoints = {}
