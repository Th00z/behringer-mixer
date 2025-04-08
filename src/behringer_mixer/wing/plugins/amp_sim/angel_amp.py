"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.plugins.amp_sim import UKRockAmp


class AngelAmp(UKRockAmp):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "ANGEL"

    @staticmethod
    def model_name() -> str:
        return "Angel Amp"

    _endpoints = deepcopy(UKRockAmp._endpoints)

    _endpoints["clean_gain"] = deepcopy(_endpoints["gain"])
    _endpoints["clean_gain"]["aliases"].append("gain")
    del _endpoints["gain"]

    _endpoints.update({
        "mid_boost": {
            "path": "/midb",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "midb" ]
        },
        "bright": {
            "path": "/bri",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "bri" ]
        },
        "bottom": {
            "path": "/bot",  # Documentation states "/bt" but it's actually "/bot"!
            "class": endpoint.BoolEndpoint,
            "aliases": [ "bt" ]
        }
    })
