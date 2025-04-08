"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .threshold_ratio_compressor import ThresholdRatioCompressor


class Soul9000ChannelCompressor(ThresholdRatioCompressor):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "9000C"

    @staticmethod
    def model_name() -> str:
        return "Soul 9000 Channel Compressor"

    _endpoints = deepcopy(ThresholdRatioCompressor._endpoints)
    _endpoints["threshold"].update({
        "min": -30.0,  # Documentation states -48...0 though it is actually this.
        "max": 18.0
    })
    _endpoints.update({
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "ratio": {
            "path": "/ratio",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "1.3": "1.1:1",
                "1.4": "1.2:1",
                "1.6": "1.3:1",
                "1.8": "1.5:1",
                "2.0": "1.7:1",
                "2.5": "2:1",
                "2.8": "2.5:1",
                "3.3": "3:1",
                "4.0": "3.5:1",
                "5.0": "4:1",
                "6.0": "5.1",
                "7.0": "6:1",
                "9.0": "8:1",
                " 12": "10:1",  # Yes, there is actually whitespace...
                " 20": "20:1",  # This is actually what we get back
                " 50": "50:1",  # from the console..
                "100": "100:1"
            },
            "allow_mapped_value_access": False
        },
        "attack": {
            "path": "/fast",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "FAST",
                False: "SLOW"
            }
        },
        "fast": {
            "path": "/fast",
            "class": endpoint.BoolEndpoint
        },
        "release": {
            "path": "/rel",
            "class": endpoint.FloatEndpoint,
            "min": 100.0,
            "max": 4000.0,
            "aliases": [ "rel" ]
        },
        "peak": {
            "path": "/peak",
            "class": endpoint.BoolEndpoint
        }
    })
