"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from . import RoomReverb


class PlateReverb(RoomReverb):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "PLATE"

    @staticmethod
    def model_name() -> str:
        return "Plate Reverb"

    _endpoints = deepcopy(RoomReverb._endpoints)
    del _endpoints["shape"]
    _endpoints.update({
        "attack": {
            "path": "/att",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 100.0,
            "aliases": [ "att" ]
        }
    })
