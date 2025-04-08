"""

"""
from copy import deepcopy
from behringer_mixer.component import Component
from . import endpoint
from .utils import Color, Icon


class MuteGroup(Component):
    """

    """
    _components = {}

    _endpoints = {
        "name": {
            "path": "/name",
            "class": endpoint.StringEndpoint,
            "max_chars": 8
        },
        "mute": {
            "path": "/mute",
            "class": endpoint.BoolEndpoint
        }
    }


class DCA(MuteGroup):
    """

    """
    _endpoints = deepcopy(MuteGroup._endpoints)
    _endpoints.update({
        "color": {
            "path": "/col",
            "class": endpoint.IntEndpoint,
            "values": Color,
            "read_offset": 1,
            "aliases": [ "col" ]
        },
        "icon": {
            "path": "/icon",
            "class": endpoint.IntEndpoint,
            "values": Icon
        },
        "scribble_light": {
            "path": "/led",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "led" ]
        },
        "fader": {
            "path": "/fdr",
            "class": endpoint.FaderEndpoint,
            "aliases": [ "fdr" ]
        },
        "solo": {
            "path": "/$solo",
            "class": endpoint.BoolEndpoint
        },
        "solo_led": {
            "path": "/$sololed",
            "class": endpoint.IntEndpoint,
            "read_only": True,
            "min": 0,
            "max": 2,
            "aliases": [ "sololed" ]
        },
        "monitor": {
            "path": "/mon",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "A", "B", "A+B" ],
            "aliases": [ "mon", "monitor_mode" ]
        },
    })
