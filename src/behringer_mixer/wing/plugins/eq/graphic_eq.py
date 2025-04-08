"""

""""""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class GEQFader(endpoint.FloatEndpoint):
    """

    """
    def _init(self):
        """

        :return:
        """
        super()._init(min=-15.0, max=15.0)


class GraphicEQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "GEQ"

    @staticmethod
    def model_name() -> str:
        return "Graphic EQ"

    _components = {}

    _endpoints = {
        "true_curve": {
            "path": "/type",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "STD": [ False, "OFF" ],
                "TRU": [ True, "ON" ]
            }
        },
        "type": {
            "path": "/type",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "STD": "STANDARD",
                "TRU": "TRUE CURVE"
            }
        },
        "hz20": {
            "path": "/20",
            "class": GEQFader
        },
        "hz25": {
            "path": "/25",
            "class": GEQFader
        },
        "hz31": {
            "path": "/31",
            "class": GEQFader
        },
        "hz40": {
            "path": "/40",
            "class": GEQFader
        },
        "hz50": {
            "path": "/50",
            "class": GEQFader
        },
        "hz63": {
            "path": "/63",
            "class": GEQFader
        },
        "hz80": {
            "path": "/80",
            "class": GEQFader
        },
        "hz100": {
            "path": "/100",
            "class": GEQFader
        },
        "hz125": {
            "path": "/125",
            "class": GEQFader
        },
        "hz160": {
            "path": "/160",
            "class": GEQFader
        },
        "hz200": {
            "path": "/200",
            "class": GEQFader
        },
        "hz250": {
            "path": "/250",
            "class": GEQFader
        },
        "hz315": {
            "path": "/315",
            "class": GEQFader
        },
        "hz400": {
            "path": "/400",
            "class": GEQFader
        },
        "hz500": {
            "path": "/500",
            "class": GEQFader
        },
        "hz630": {
            "path": "/630",
            "class": GEQFader
        },
        "hz800": {
            "path": "/800",
            "class": GEQFader
        },
        "hz1k": {
            "path": "/1k",
            "class": GEQFader
        },
        "hz1k25": {
            "path": "/1k25",
            "class": GEQFader
        },
        "hz1k6": {
            "path": "/1k6",
            "class": GEQFader
        },
        "hz2k": {
            "path": "/2k",
            "class": GEQFader
        },
        "hz2k5": {
            "path": "/2k5",
            "class": GEQFader
        },
        "hz3k15": {
            "path": "/3k15",
            "class": GEQFader
        },
        "hz4k": {
            "path": "/4k",
            "class": GEQFader
        },
        "hz5k": {
            "path": "/5k",
            "class": GEQFader
        },
        "hz6k3": {
            "path": "/6k3",
            "class": GEQFader
        },
        "hz8k": {
            "path": "/8k",
            "class": GEQFader
        },
        "hz10k": {
            "path": "/10k",
            "class": GEQFader
        },
        "hz12k5": {
            "path": "/12k5",
            "class": GEQFader
        },
        "hz16k": {
            "path": "/16k",
            "class": GEQFader
        },
        "hz20k": {
            "path": "/20k",
            "class": GEQFader
        },
        "trim": {
            "path": "/TRIM",
            "class": GEQFader
        },
    }
