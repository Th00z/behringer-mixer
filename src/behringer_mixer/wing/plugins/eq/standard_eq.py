"""

"""
from copy import deepcopy

from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin, EQBand


class EQParametricShelf(Component):
    """

    """
    _components = {}

    _endpoints = {
        "gain": {
            "path": "g",
            "class": endpoint.FloatEndpoint,
            "min": -15.0,
            "max": 15.0,
            "aliases": [ "g" ]
        },
        "frequency": {
            "path": "f",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 20000.0,
            "aliases": [ "f" ]
        },
        "q": {
            "path": "q",
            "class": endpoint.FloatEndpoint,
            "min": 0.44,
            "max": 10.0
        },
        "type": {
            "path": "eq",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "PEQ", "SHV" ],
            "aliases": [ "eq" ]
        }
    }


class EQParametricLowShelf(EQParametricShelf):
    """

    """
    _endpoints = deepcopy(EQParametricShelf._endpoints)
    _endpoints["frequency"].update({
        "max": 2000.0
    })


class EQParametricHighShelf(EQParametricShelf):
    """

    """
    _endpoints = deepcopy(EQParametricShelf._endpoints)
    _endpoints["frequency"].update({
        "min": 50.0
    })


class Standard6BandEQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "STD"

    @staticmethod
    def model_name() -> str:
        return "Standard EQ"

    _components = {
        "low": {
            "path": "/l",
            "class": EQParametricLowShelf,
            "aliases": [ "l" ]
        },
        "band": {
            "path": "",
            "class": EQBand,
            "count": 4
        },
        "high": {
            "path": "/h",
            "class": EQParametricHighShelf,
            "aliases": [ "h" ]
        }
    }

    _endpoints = {}


class EQParametricSendShelf(EQParametricShelf):
    """

    """
    _endpoints = deepcopy(EQParametricShelf._endpoints)
    _endpoints["q"].update({
        "min": 0.442
    })
    # I haven't found a way of selecting any of these on the console directly, yet but it does
    # actually work through OSC :)
    _endpoints["type"]["valid_strings"].extend(
        [ "CUT", "BW6", "BW12", "BS12", "LR12", "BW18", "BW24", "BS24", "LR24", "BW48", "LR48" ]
    )


class EQParametricSendLowShelf(EQParametricSendShelf):
    """

    """
    _endpoints = deepcopy(EQParametricShelf._endpoints)
    _endpoints["frequency"].update({
        "max": 2000.0
    })


class EQParametricSendHighShelf(EQParametricSendShelf):
    """

    """
    _endpoints = deepcopy(EQParametricShelf._endpoints)
    _endpoints["frequency"].update({
        "min": 50.0
    })


class EQSendBand(EQBand):
    """

    """
    _endpoints = deepcopy(EQBand._endpoints)
    _endpoints["q"].update({
        "min": 0.442
    })


class StandardSendEQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "STD"

    @staticmethod
    def model_name() -> str:
        return "Standard EQ"

    _components = {
        "low": {
            "path": "/l",
            "class": EQParametricSendLowShelf,
            "aliases": [ "l" ]
        },
        "band": {
            "path": "",
            "class": EQSendBand,
            "count": 6
        },
        "high": {
            "path": "/h",
            "class": EQParametricSendHighShelf,
            "aliases": [ "h" ]
        }
    }

    _endpoints = {
        "tilt": {
            "path": "/tilt",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 6.0
        }
    }
