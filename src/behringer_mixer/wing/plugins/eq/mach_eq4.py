"""

"""
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class MachEQ4Knob(endpoint.FloatEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        return super()._init(min=-5.0, max=5.0)


class MachEQ4(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "MACH4"

    @staticmethod
    def model_name() -> str:
        return "Mach EQ4"

    _components = {}

    _endpoints = {
        # No "in_out" endpoint as that would clash with the plugin's representation within
        # the FX section.
        "sub": {
            "path": "/sub",
            "class": MachEQ4Knob
        },
        "hz40": {
            "path": "/40",
            "class": MachEQ4Knob
        },
        "hz160": {
            "path": "/160",
            "class": MachEQ4Knob
        },
        "hz650": {
            "path": "/650",
            "class": MachEQ4Knob
        },
        "hz2k5": {
            "path": "/2k5",
            "class": MachEQ4Knob
        },
        "air_gain": {
            "path": "/air",
            "class": endpoint.StandardKnob
        },
        "air_freq": {
            "path": "/airm",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "OFF", "2k5", "5k", "10k", "20k", "40k" ]
        },
        "auto": {
            "path": "/again",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "again" ]
        }
    }
