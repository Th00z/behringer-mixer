"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class DualDeEsserKnob(endpoint.FloatEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(min=0.0, max=50.0)


class DualDeEsser(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "DE-S2"

    @staticmethod
    def model_name() -> str:
        return "2-Band DeEsser"

    _components = {}

    _endpoints = {
        "low": {
            "path": "/lo",
            "class": DualDeEsserKnob,
            "aliases": [ "lo" ]
        },
        "high": {
            "path": "/hi",
            "class": DualDeEsserKnob,
            "aliases": [ "hi" ]
        },
        "low_side":  {
            "path": "/los",
            "class": DualDeEsserKnob,
            "aliases": [ "los" ]
        },
        "high_side": {
            "path": "/his",
            "class": DualDeEsserKnob,
            "aliases": [ "his" ]
        },
        "gender": {
            "path": "/gdr",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": { # Documentation states [FEMALE, MALE], but it's actually [f, m]!
                "f": "FEMALE",
                "m": "MALE"
            },
            "aliases": [ "gdr" ]
        },
        "female": {
            "path": "/gdr",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "f": True,
                "m": False
            },
            "aliases": [ "f" ]
        },
        "male": {
            "path": "/gdr",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "f": False,
                "m": True
            },
            "aliases": [ "m" ]
        },
        "m_s_mode": { # Documentation states [STEREO, MID/SIDE], but it's actually [st, ms]!
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "st": [ False, "STEREO" ],
                "ms": [ True, "MID/SIDE" ]
            },
            "aliases": [ "ms_mode", "ms" ]
        }
    }
