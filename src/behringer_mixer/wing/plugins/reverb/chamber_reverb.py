"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint
from .room_reverb import RoomReverb, Echo as RoomEcho


class Echo(RoomEcho):
    """

    """
    _endpoints = deepcopy(RoomEcho._endpoints)
    _endpoints["depth"].update({
        "max": 300.0
    })
    del _endpoints["feed"]
    _endpoints.update({
        # We can't have two endpoints with the same name, so we have to deviate here.
        "level": {
            "path": "/el{side}",
            "class": endpoint.FaderEndpoint,
            "aliases": [
                "lvl", "el", "echo_lvl", "echo_fdr", "echo_fader", "echo_fdr_lvl", "echo_fader_lvl",
                "echo_fader_level"
            ]
        },
    })


class ChamberReverb(RoomReverb):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "CHAMBER"

    @staticmethod
    def model_name() -> str:
        return "Chamber Reverb"

    _components = deepcopy(RoomReverb._components)
    _components["echo_l"].update({
        "class": Echo
    })
    _components["echo_r"].update({
        "class": Echo
    })
