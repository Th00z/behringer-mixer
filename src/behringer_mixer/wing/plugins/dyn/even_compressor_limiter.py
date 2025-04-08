"""

"""
from copy import deepcopy
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class EvenCompressor(Component):
    """

    """
    _components = {}

    _endpoints = {
        "compress": {
            "path": "/con",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "in",
                False: "out"
            }
        },
        "con": {
            "path": "/con",
            "class": endpoint.BoolEndpoint
        },
        "threshold": {
            "path": "/cthr",
            "class": endpoint.FloatEndpoint,
            "min": -35.0,
            "max": -5.0,
            "aliases": [ "cthr" ]
        },
        "ratio": {
            "path": "/ratio",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "1.5", "2.0", "3.0", "4.0", "6.0" ]
        },
        "recovery": {
            "path": "/crec",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "100": "100",
                "400": "400",
                "800": "800",
                "1500": "1500",
                "A1": "auto1",
                "A2": "auto2"
            },
            "aliases": [ "crec" ]
        },
        "gain": {
            "path": "/cgain",
            "class": endpoint.FloatEndpoint,
            "valid_values": [ -6.0, -3.0, 0, 3.0, 6.0, 12.0 ],
            "aliases": [ "cgain" ]
        },
        "attack": {
            "path": "/cfast",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "FAST",
                False: "SLOW"
            }
        },
        "fast": {
            "path": "/cfast",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "cfast" ]
        }
    }


class EvenLimiter(Component):
    """

    """
    _components = {}

    _endpoints = {
        "limit": {
            "path": "/lon",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "in",
                False: "out"
            }
        },
        "lon": {
            "path": "/lon",
            "class": endpoint.BoolEndpoint
        },
        "threshold": {
            "path": "/lthr",
            "class": endpoint.FloatEndpoint,
            "min": -12.0,
            "max": 0.0,
            "aliases": [ "lthr" ]
        },
        "recovery": {
            "path": "/lrec",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "50": "50",
                "100": "100",
                "200": "200",
                "800": "800",
                "A1": "auto1",
                "A2": "auto2"
            },
            "aliases": [ "lrec" ]
        },
        "attack": {
            "path": "/lfast",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "FAST",
                False: "SLOW"
            }
        },
        "fast": {
            "path": "/lfast",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "lfast" ]
        }
    }


class EvenCompressorLimiter(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "ECL33"

    @staticmethod
    def model_name() -> str:
        return "Even Compressor/Limiter"

    _components = {
        "limit": {
            "path": "",
            "class": EvenLimiter
        },
        "compress": {
            "path": "",
            "class": EvenCompressor
        }
    }

    _endpoints = {
        "power": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "on" ]
        }
    }
