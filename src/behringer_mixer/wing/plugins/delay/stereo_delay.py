"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class StereoDelay(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "ST-DL"

    @staticmethod
    def model_name() -> str:
        return "Stereo Delay"

    _components = {}

    _endpoints = {
        "time": {
            "path": "/time",
            "class": endpoint.FloatEndpoint,
            "min": 1.0,
            "max": 3000.0
        },
        "mode": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "ST": "STEREO",
                "X": "CROSS",
                "M": "MONO"
            }
        },
        "stereo": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "read_only": True, # read-only as the mapping is not injective
            "string_mapping": {
                "ST": True,
                "X": False,
                "M": False
            }
        },
        "cross": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "read_only": True, # read-only as the mapping is not injective
            "string_mapping": {
                "ST": False,
                "X": True,
                "M": False
            }
        },
        "mono": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "read_only": True, # read-only as the mapping is not injective
            "string_mapping": {
                "ST": False,
                "X": False,
                "M": True
            }
        },
        "factor": {
            "path": "/fact",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "1/4", "1/3", "1/2", "2/3", "3/4", "1", "5/4", "4/3", "3/2", "2" ],
            "aliases": [ "fact" ]
        },
        "pattern": {
            "path": "/pat",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "1/2:1", "2/3:1", "3/4:1", "7/8:1", "1:1", "1:9/8", "1:5/4", "1:4/3", "1:3/2"
            ],
            "aliases": [ "pat" ]
        },
        "offset": {
            "path": "/offs", # documentation states "/offset", but the console yields "offs"
            "class": endpoint.IntEndpoint,
            "min": -50,
            "max": 50,
            "aliases": [ "offs" ]
        },
        "feedback": {
            "path": "/feed",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "feed" ]
        },
        "fb_locut": {
            "path": "/flc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [
                "flc", "fb_lo_cut", "feed_l_cut", "feedback_low_cut", "fb_hp", "fb_hi_pass",
                "feedback_high_pass"
            ]
        },
        "fb_hicut": {
            "path": "/fhc",
            "class": endpoint.FXHighCutEndpoint,
            "aliases": [
                "fhc", "fb_hi_cut", "feed_h_cut", "feedback_high_cut", "fb_lp", "fb_lo_pass",
                "feedback_low_pass"
            ]
        },
        "low_cut": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc", "lo_cut", "hp", "hi_pass", "high_pass" ]
        },
        "high_cut": {
            "path": "/hc",
            "class": endpoint.FXHighCutEndpoint,
            "aliases": [ "hc", "hi_cut", "lp", "lo_pass", "low_pass" ]
        },
    }
