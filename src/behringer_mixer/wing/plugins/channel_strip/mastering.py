"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin

from behringer_mixer.wing.plugins.other import TapeMachine
from behringer_mixer.wing.plugins.other.ultra_enhancer import UltraEnhancer, StereoSection
from behringer_mixer.wing.plugins.eq import MachEQ4
from behringer_mixer.wing.plugins.dyn import PrecisionLimiter


class ChannelTape(TapeMachine):
    """

    """
    _endpoints = deepcopy(TapeMachine._endpoints)
    del _endpoints["out_gain"]
    for ep in _endpoints:
        _endpoints[ep].update({ "path": _endpoints[ep]["path"].removeprefix("/") })
    _endpoints.update({
        "power": {
            "path": "on",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "ON",
                False: "OFF"
            }
        },
        "on": {
            "path": "on",
            "class": endpoint.BoolEndpoint
        }
    })


class ChannelEQ(MachEQ4):
    """

    """
    _endpoints = deepcopy(MachEQ4._endpoints)
    del _endpoints["auto"]
    _endpoints.update({
        "on": {
            "path": "/eq_on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "eq_on" ]
        }
    })


class ChannelStereoSection(StereoSection):
    """

    """
    _endpoints = deepcopy(StereoSection._endpoints)
    for ep in _endpoints:
        _endpoints[ep].update({ "path": _endpoints[ep]["path"].removeprefix("/") })


class ChannelEnhancer(UltraEnhancer):
    """

    """
    _components = deepcopy(UltraEnhancer._components)
    _components["stereo"].update({ "class": ChannelStereoSection })
    for component in _components:
        _components[component].update({ "path": _components[component]["path"].removeprefix("/") })

    _endpoints = deepcopy(UltraEnhancer._endpoints)
    del _endpoints["gain"]
    del _endpoints["solo"]
    _endpoints.update({
        "on": {
            "path": "on",
            "class": endpoint.BoolEndpoint
        }
    })


class ChannelLimiter(PrecisionLimiter):
    """

    """
    _endpoints = deepcopy(PrecisionLimiter._endpoints)
    for ep in _endpoints:
        _endpoints[ep].update({ "path": _endpoints[ep]["path"].removeprefix("/") })
    _endpoints.update({
        "on": {
            "path": "on",
            "class": endpoint.BoolEndpoint
        }
    })


class Mastering(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "*MASTER*"

    @staticmethod
    def model_name() -> str:
        return "Mastering"

    _components = {
        "tape": {
            "path": "/t_",
            "class": ChannelTape,
            "aliases": [ "t", "tape_machine" ]
        },
        "eq": {
            "path": "",
            "class": ChannelEQ,
            "aliases": [ "mach4", "mach4_eq", "mach_eq4" ]
        },
        "enh": {
            "path": "/e_",
            "class": ChannelEnhancer,
            "aliases": [ "e", "enhance", "enhancer", "stereo_enhancer", "ultra_enhancer" ]
        },
        "lim": {
            "path": "/l_",
            "class": ChannelLimiter,
            "aliases": [ "l", "limiter", "precision_limiter" ]
        }
    }

    _endpoints = {}
