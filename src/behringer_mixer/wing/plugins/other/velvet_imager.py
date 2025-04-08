"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class VelvetImager(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "V-IMG"  # Documentation has a typo: '_' instead of '-'.

    @staticmethod
    def model_name() -> str:
        return "Velvet Imager"

    _components = {}

    _endpoints = {
        "ms_width": {
            "path": "/wid",
            "class": endpoint.FloatEndpoint,
            "min": -1.0,
            "max": 1.0,
            "aliases": [ "wid", "width" ]
        },
        "stereoize": {
            "path": "/st",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "st", "stereo" ]
        },
        "gain": {
            "path": "/g", # Documentation states it's "/gain" but it's "/g"!
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 6.0,
            "aliases": [ "g" ]
        },
        "mode": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "K-STEREO": "K-Stereo",
                "VELVET": "Velvet"
            }
        },
        "k_stereo": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "K-STEREO": True,
                "VELVET": False
            }
        },
        "velvet": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "K-STEREO": False,
                "VELVET": True
            }
        },
        "deep": {
            "path": "/deep",
            "class": endpoint.BoolEndpoint
        }
    }
