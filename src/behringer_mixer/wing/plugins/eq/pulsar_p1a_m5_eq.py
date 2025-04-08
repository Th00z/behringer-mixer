"""

"""
from copy import deepcopy

from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class PulsarP1aM5Band(Component):
    """

    """
    _components = {}

    _endpoints = {
        "frequency": {
            "path": "f",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [],
            "aliases": [ "f" ]
        }
    }


class PulsarP1aM5BoostBand(PulsarP1aM5Band):
    """

    """
    _endpoints = deepcopy(PulsarP1aM5Band._endpoints)
    _endpoints.update({
        "boost": {
            "path": "b",
            "class": endpoint.StandardKnob,
            "aliases": [ "b" ]
        }
    })


class PulsarP1aM5EQ1Band(PulsarP1aM5BoostBand):
    """

    """
    _endpoints = deepcopy(PulsarP1aM5BoostBand._endpoints)
    _endpoints.update({
        "attenuation": {
            "path": "att",
            "class": endpoint.StandardKnob,
            "aliases": [ "att" ]
        }
    })


class PulsarP1aM5EQ1Low(PulsarP1aM5EQ1Band):
    """

    """
    _endpoints = deepcopy(PulsarP1aM5EQ1Band._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "20", "30", "60", "100" ]
    })
    _endpoints["frequency"]["aliases"].append("lo_freq")
    _endpoints["boost"]["aliases"].append("lo_boost")
    _endpoints["attenuation"]["aliases"].append("lo_att")


class PulsarP1aM5EQ1High(PulsarP1aM5EQ1Band):
    """

    """
    _endpoints = deepcopy(PulsarP1aM5EQ1Band._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "3k", "4k", "5k", "8k", "10k", "12k", "16k" ]
    })
    _endpoints["frequency"]["aliases"].append("hi_freq")
    _endpoints["boost"]["aliases"].append("hi_boost")
    _endpoints["attenuation"]["aliases"].append("hi_att")
    _endpoints.update({
        "width": {
            "path": "w",
            "class": endpoint.StandardKnob,
            "aliases": [ "w", "hi_width" ]
        },
        "attenuation_frequency": {
            "path": "attf",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "5k", "10k", "20k" ],
            "aliases": [ "attf", "hi_att_freq" ]
        }
    })


class PulsarP1aM5EQ5MidLow(PulsarP1aM5BoostBand):
    """

    """
    _endpoints = deepcopy(PulsarP1aM5BoostBand._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "200", "300", "500", "700", "1k" ]
    })
    _endpoints["frequency"]["aliases"].append("lo_mid_freq")
    _endpoints["boost"]["aliases"].append("lo_mid_boost")


class PulsarP1aM5EQ5Mid(PulsarP1aM5Band):
    """

    """
    _endpoints = deepcopy(PulsarP1aM5Band._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "200", "300", "500", "700", "1k", "1k5", "2k", "3k", "4k", "5k", "7k" ]
    })
    _endpoints["frequency"]["aliases"].append("mid_freq")
    _endpoints.update({
        "dip": {
            "path": "d",
            "class": endpoint.StandardKnob,
            "aliases":  [ "d", "mid_dip" ]
        }
    })


class PulsarP1aM5EQ5MidHigh(PulsarP1aM5BoostBand):
    """

    """
    _endpoints = deepcopy(PulsarP1aM5BoostBand._endpoints)
    _endpoints["frequency"].update({
        "valid_strings": [ "1k5", "2k", "3k", "4k", "5k" ]
    })
    _endpoints["frequency"]["aliases"].append("hi_mid_freq")
    _endpoints["boost"]["aliases"].append("hi_mid_boost")


class PulsarP1aM5EQ(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "PULSAR"

    @staticmethod
    def model_name() -> str:
        return "Pulsar P1a/M5 EQ"

    _components = {
        "low": {
            "path": "/1l",
            "class": PulsarP1aM5EQ1Low,
            "aliases":  [ "l1" ]
        },
        "low_mid": {
            "path": "/5l",
            "class": PulsarP1aM5EQ5MidLow,
            "aliases":  [ "l5" ]
        },
        "mid": {
            "path": "/5m",
            "class": PulsarP1aM5EQ5Mid,
            "aliases":  [ "m5" ]
        },
        "high_mid": {
            "path": "/5h",
            "class": PulsarP1aM5EQ5MidHigh,
            "aliases":  [ "h5" ]
        },
        "high": {
            "path": "/1h",
            "class": PulsarP1aM5EQ1High,
            "aliases":  [ "h1" ]
        }
    }

    _endpoints = {
        "hi_lo_eq1_in": {
            "path": "/eq1",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "eq1", "hi_lo_eq1" ]
        },
        "mid_eq5_in": {
            "path": "/eq5",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "eq5", "mid_eq5" ]
        }
    }
