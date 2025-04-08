"""

"""
from copy import deepcopy

from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin, LeftRightComponent

from .stereo_chorus import DelaySection as ChorusDelaySection
from .effect_sections import FilterSection


class FeedbackSection(FilterSection):
    """

    """
    _endpoints = deepcopy(FilterSection._endpoints)
    _endpoints["lo_cut"].update({
        "path": "/flc"
    })
    _endpoints["lo_cut"]["aliases"].append("flc")
    _endpoints["hi_cut"].update({
        "path": "/fhc"
    })
    _endpoints["hi_cut"]["aliases"].append("fhc")
    _endpoints.update({
        "feedback": {
            "path": "/feed",
            "class": endpoint.FloatEndpoint,
            "min": -90.0,
            "max": 90.0,
            "aliases": [ "feed" ]
        }
    })


class DelaySection(ChorusDelaySection):
    """

    """
    _endpoints = deepcopy(ChorusDelaySection._endpoints)
    # Documentation states 5...20, but it's actually 0.5
    _endpoints["size"].update({ "min": 0.5, "max": 20 })


class StereoFlanger(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "FLANGER"  # Documentation states "FLANGER", probably a copy&paste error ;)

    @staticmethod
    def model_name() -> str:
        return "Stereo Flanger"

    _components = {
        "feedback": {
            "path": "",
            "class": FeedbackSection
        },
        "delay_left": {
            "path": "/l",
            "class": DelaySection
        },
        "delay_right": {
            "path": "/r",
            "class": DelaySection
        },
        "twin_filter": {
            "path": "",
            "class": FilterSection,
            "aliases": [ "filter" ]
        }
    }

    _endpoints = {
        "mix": {
            "path": "/mix",
            "class": endpoint.PercentEndpoint,
            "aliases": [ "dry_wet" ]
        },
        "phase": {
            "path": "/phase",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 180.0
        },
        "speed": {
            "path": "/spd",
            "class": endpoint.FloatEndpoint,
            "min": 0.05,
            "max": 5.0,
            "aliases": [ "spd" ]
        }
    }
