"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin
from behringer_mixer.wing.plugins.gate import DynamicEQ


class DEQBand(DynamicEQ):
    """

    """
    _endpoints = deepcopy(DynamicEQ._endpoints)
    _endpoints["threshold"].update({ "path": "-thr" })
    _endpoints["ratio"].update({ "path": "-ratio" })
    _endpoints["attack"].update({ "path": "-att" })
    _endpoints["release"].update({ "path": "-rel" })
    _endpoints["filter_types"].update({ "path": "-filt" })
    _endpoints["gain"].update({ "path": "-g" })
    _endpoints["freq"].update({ "path": "-f" })
    _endpoints["q"].update({ "path": "-q", "min": 0.44 })
    _endpoints["mode"].update({ "path": "-mode" })
    _endpoints["above"].update({ "path": "-mode" })
    _endpoints["below"].update({ "path": "-mode" })


class TripleDynamicEQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "DEQ3"

    @staticmethod
    def model_name() -> str:
        return "Triple Dynamic EQ"

    _components = {
        "band": {
            "path": "",
            "class": DEQBand,
            "count": 3
        }
    }

    _endpoints = {}
