"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class SpeedControlSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "leslie_switch": {
            "path": "/sw",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "STOP", "SLOW", "FAST" ],
            "aliases": [ "speed_switch", "switch", "sw" ]
        },
        "slow_rate": {
            "path": "/lo",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 3.999,
            "aliases": [ "lo", "lo_speed" ]
        },
        "fast_rate": {
            "path": "/hi",
            "class": endpoint.FloatEndpoint,
            "min": 4.0,
            "max": 10.0,
            "aliases": [ "hi", "hi_speed" ]
        }
    }


class AccelerationSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "bass": {
            "path": "/dac",
            "class": endpoint.PercentEndpoint,
            "aliases": [
                "dac", "bass_accel", "bass_acceleration", "drum", "drum_accel", "drum_acceleration"
            ]
        },
        "horn": {
            "path": "/hac",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "hac", "horn_accel", "horn_acceleration" ]
        },
    }


class RotarySpeaker(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "ROTARY"

    @staticmethod
    def model_name() -> str:
        return "Rotary Speaker"

    _components = {
        "speed_control": {
            "path": "",
            "class": SpeedControlSection,
            "aliases": [ "speed" ]
        },
        "acceleration": {
            "path": "",
            "class": AccelerationSection,
            "aliases": [ "acc", "ac", "accel" ]
        }
    }

    _endpoints = {
        "balance": {
            "path": "/bal",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "bal" ]
        },
        "distance": {
            "path": "/dist",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "dist" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.PercentEndpoint
        }
    }
