"""

"""
from abc import ABC

from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class ChannelFilterLowcut(Component):
    """

    """
    _components = {}

    _endpoints = {
        "enable": {
            "path": "/lc",
            "class": endpoint.BoolEndpoint
        },
        "frequency": {
            "path": "/lcf",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 2000.0
        },
        "slope": {
            "path": "/lcs",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "6", "12", "18", "24" ]
        }
    }


class ChannelFilterHighcut(Component):
    """

    """
    _components = {}

    _endpoints = {
        "enable": {
            "path": "/hc",
            "class": endpoint.BoolEndpoint
        },
        "frequency": {
            "path": "/hcf",
            "class": endpoint.FloatEndpoint,
            "min": 50.0,
            "max": 20000.0
        },
        "slope": {
            "path": "/hcs",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "6", "12" ]
        }
    }


class BaseFilter(ConcretePlugin, ABC):
    """

    """
    _components = {
        "lowcut": {
            "path": "",
            "class": ChannelFilterLowcut
        },
        "highcut": {
            "path": "",
            "class": ChannelFilterHighcut
        }
    }

    _endpoints = {
        "tool_filter": {
            "path": "/tf",
            "class": endpoint.BoolEndpoint
        }
    }
