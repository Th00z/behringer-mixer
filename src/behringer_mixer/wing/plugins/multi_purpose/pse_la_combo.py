"""

"""
from copy import deepcopy
from behringer_mixer.wing import endpoint

from .source_extractor import SourceExtractor
from .leveling_amplifier_2a import LevelingAmplifier2A


class PSELACombo(SourceExtractor, LevelingAmplifier2A):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "CMB"

    @staticmethod
    def model_name() -> str:
        return "PSE/LA Combo"

    _components = {}

    _endpoints = deepcopy(SourceExtractor._endpoints)

    _la2a_endpoints = deepcopy(LevelingAmplifier2A._endpoints)
    # The peak_reduction and mode endpoints of the combined plugin are c-prefixed.
    # This is not documented.
    _la2a_endpoints["peak_reduction"].update({ "path": "/cpeak" })
    del _la2a_endpoints["peak_reduction"]["aliases"]
    _la2a_endpoints["mode"].update({ "path": "/cmode" })
    del _la2a_endpoints["power"]

    _endpoints.update(_la2a_endpoints)
