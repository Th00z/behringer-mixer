"""

"""
from typing import List
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin, PostIndexedComponent


class CombinatorBand(PostIndexedComponent):
    """

    """
    _components = {}

    _endpoints = {
        "thresh": {
            "path": "/thr_{index}",
            "class": endpoint.FloatEndpoint,
            "min": -10.0,
            "max": 10.0,
            "aliases": [ "threshold", "thr" ]
        },
        "gain": {
            "path": "/gain_{index}",
            "class": endpoint.FloatEndpoint,
            "min": -10.0,
            "max": 10.0
        },
        "bypass": {
            "path": "/byp_{index}",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "byp" ]
        },
        "width": {
            "path": "/width_{index}",
            "class": endpoint.FloatEndpoint,
            "min": -50.0,
            "max": 50.0
        }
    }


class Combinator(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "C5-CMB"

    @staticmethod
    def model_name() -> str:
        return "Combinator"

    _components = {
        "band": {
            "path": "",
            "class": CombinatorBand,
            "count": 5
        }
    }

    _endpoints = {
        "thresh": {
            "path": "/thr",
            "class": endpoint.FloatEndpoint,
            "min": -40.0,
            "max": 0.0,
            "aliases": [ "thr" ]
        },
        "gain": {
            "path": "/gain",
            "class": endpoint.FloatEndpoint,
            "min": -10.0,
            "max": 10.0
        },
        "ratio": {
            "path": "/ratio",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "1.1": [ "1.1:1", 1.1 ],
                "1.2": [ "1.2:1", 1.2 ],
                "1.3": [ "1.3:1", 1.3 ],
                "1.5": [ "1.5:1", 1.5 ],
                "1.7": [ "1.7:1", 1.7 ],
                "2.0": [ "2:1", 2.0 ],
                "2.5": [ "2.5:1", 2.5 ],
                "3.0": [ "3:1", 3.0 ],
                "3.5": [ "3.5:1", 3.5 ],
                "4.0": [ "4:1", 4.0 ],
                "5.0": [ "5.1", 5.0 ],
                "7.0": [ "7:1", 7.0 ],
                " 10": [ "10:1", 10.0 ],  # Yes, there is actually whitespace...
                "100": [ "100:1", 100.0 ]
            }
        },
        "slope": {
            "path": "/slope",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "48": [ "48 dB/Oct", "ON", True ],
                "24": [ "48 dB/Oct", "OFF", False ]
            }
        },
        "selected_band": {
            "path": "/bandsel",  # There's a typo in the documentation adding a whitespace
            "class": endpoint.IntEndpoint,
            "min": 1,
            "max": 5,
            "aliases": [ "bandsel" ]
        },
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 20.0,
            "aliases": [ "att" ]
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 3000.0,
            "aliases": [ "rel" ]
        },
        "auto_release": {
            "path": "/arel",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "auto", "arel" ]
        },
        "sbc": {
            "path": "/sbc",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 10.0,
            "aliases": [ "sbc_speed" ]
        },
        "sbc_on": {
            "path": "/sbcon",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "sbcon", "sbc_enable", "enable_sbc" ]
        },
        "band_solo": {
            "path": "/$bdsolo",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "bdsolo", "solo" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 100.0
        }
    }
