"""

"""
from copy import deepcopy
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint


class StandardGBand(Component):
    """

    """
    _components = {}

    _endpoints = {
        "gain": {
            "path": "g",
            "class": endpoint.FloatEndpoint,
            "min": -5.0,
            "max": 5.0,
            "aliases": [ "g" ]
        }
    }


class StandardFGBand(StandardGBand):
    """

    """
    _endpoints = deepcopy(StandardGBand._endpoints)
    _endpoints.update({
        "frequency": {
            "path": "f",
            "class": endpoint.StandardKnob,
            "aliases": [ "f" ]
        },
    })


class StandardStringFrequencyGBand(StandardGBand):
    """

    """
    _endpoints = deepcopy(StandardGBand._endpoints)
    _endpoints.update({
        "frequency": {
            "path": "f",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [],
            "aliases": [ "f" ]
        }
    })


class StandardFGQBand(StandardFGBand):
    """

    """
    _endpoints = deepcopy(StandardFGBand._endpoints)
    _endpoints.update({
        "q": {
            "path": "q",
            "class": endpoint.StandardKnob
        }
    })


class StandardFGQBy3Band(StandardFGQBand):
    """

    """
    _endpoints = deepcopy(StandardFGQBand._endpoints)
    _endpoints.update({
        "by_3": {
            "path": "f3",
            "class": endpoint.BoolEndpoint,
        }
    })


class StandardFGQTimes3Band(StandardFGQBand):
    """

    """
    _endpoints = deepcopy(StandardFGQBand._endpoints)
    _endpoints.update({
        "times_3": {
            "path": "f3",
            "class": endpoint.BoolEndpoint,
        }
    })
