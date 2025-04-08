"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class StereoPitch(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "PITCH"

    @staticmethod
    def model_name() -> str:
        return "Stereo Pitch"

    _components = {}

    _endpoints = {
        "semi": {
            "path": "/semi",
            "class": endpoint.IntEndpoint,
            "min": -12,
            "max": 12,
            "aliases": [ "semitones", "pitch_coarse", "pitch_c" ]
        },
        "cents": {
            "path": "/cent",
            "class": endpoint.IntEndpoint,
            "min": -50,
            "max": 50,
            "read_offset": -50,
            "write_offset": 1,
            "aliases": [ "cent", "pitch_fine", "pitch_f" ]
        },
        "delay": {
            "path": "/dly",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 500.0,
            "aliases": [ "dly" ]
        },
        "locut": {
            "path": "/lc",
            "class": endpoint.FXLowCutEndpoint,
            "aliases": [ "lc", "lo_cut", "low_cut", "hp", "hi_pass", "high_pass" ]
        },
        "hicut": {
            "path": "/hc",
            "class": endpoint.FXHighCutEndpoint,
            "aliases": [ "hc", "hi_cut", "high_cut", "lp", "lo_pass", "low_pass" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.PercentEndpoint
        }
    }
