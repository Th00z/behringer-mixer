"""

"""
from copy import deepcopy
from typing import Dict, Type

from behringer_mixer.client import Client
from behringer_mixer.component import Component
from . import endpoint
from .component import PluginComponent
from . import plugins


class FX(PluginComponent):
    """

    """
    _endpoints = {
        "mix": {
            "path": "/fxmix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 100.0,
            "aliases": [ "fxmix" ]
        },
        "source": {
            "path": "/$esrc",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 400,
            "read_only": True,
            "aliases": [ "src", "esource", "esrc", "input_source", "input" ]
        },
        "mode": {
            "path": "/$emode",
            "class": endpoint.InputModeEndpoint,
            "read_only": True,
            "aliases": [ "emode", "input_mode" ]
        },
        "channel": {
            "path": "/$a_chn",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 76,
            "read_only": True,
            "aliases": [ "inserted_channel", "a_chn" ]
        },
        "position": {
            "path": "/$a_pos",
            "class": endpoint.IntMappingEndpoint,
            "int_mapping": {
                0: "PRE",
                1: "POST"
            },
            "read_only": True,
            "aliases": [ "inserted_position", "channel_insert", "a_pos" ]
        }
    }

    _models = [
        plugins.none.NonePlugin,
        plugins.other.ExternalEffect,
        plugins.eq.GraphicEQ,
        plugins.eq.PIA560GEQ,
        plugins.eq.TripleDynamicEQ,
        plugins.dyn.Combinator,
        plugins.dyn.PrecisionLimiter,
        plugins.other.SpeakerManager,
        plugins.dyn.DualDeEsser,
        plugins.other.UltraEnhancer,
        plugins.other.Exciter,
        plugins.other.PsychoBass,
        plugins.effects.SubOctaver,
        plugins.other.SubMonster,
        plugins.other.VelvetImager,
        plugins.other.DoubleVocal,
        plugins.other.PitchFix,
        plugins.amp_sim.RotarySpeaker,
        plugins.effects.Phaser,
        plugins.effects.TremoloPanner,
        plugins.other.TapeMachine,
        plugins.effects.MoodFilter,
        plugins.other.Bodyrez,
        plugins.amp_sim.RackAmp,
        plugins.amp_sim.UKRockAmp,
        plugins.amp_sim.AngelAmp,
        plugins.amp_sim.JazzCleanAmp,
        plugins.amp_sim.DeluxeAmp,
        plugins.eq.SoulAnalogEQ,
        plugins.eq.Even88FormantEQ,
        plugins.eq.Even84EQ,
        plugins.eq.FocusriteISA110EQ,
        plugins.eq.PulsarP1aM5EQ,
        plugins.eq.MachEQ4,
        plugins.channel_strip.EvenChannel,
        plugins.channel_strip.SoulChannel,
        plugins.channel_strip.VintageChannel,
        plugins.channel_strip.BusChannel,
        plugins.channel_strip.Mastering
    ]

    _premium_fx = [
        plugins.reverb.HallReverb,
        plugins.reverb.RoomReverb,
        plugins.reverb.ChamberReverb,
        plugins.reverb.PlateReverb,
        plugins.reverb.ConcertReverb,
        plugins.reverb.Ambience,
        plugins.reverb.VSS3Reverb,
        plugins.reverb.VintageRoom,
        plugins.reverb.VintageReverb,
        plugins.reverb.VintagePlate,
        plugins.reverb.BluePlate,
        plugins.reverb.GatedReverb,
        plugins.reverb.ReverseReverb,
        plugins.reverb.DelayReverb,
        plugins.reverb.ShimmerReverb,
        plugins.reverb.SpringReverb,
        plugins.effects.DimensionCRS,
        plugins.effects.StereoChorus,
        plugins.effects.StereoFlanger,
        plugins.delay.StereoDelay,
        plugins.delay.UltraTapDelay,
        plugins.delay.TapeDelay,
        plugins.delay.OilCanDelay,
        plugins.delay.BBDDelay,
        plugins.effects.StereoPitch,
        plugins.effects.DualPitch,
    ]

    def __init__(
            self, client: Client, path: str = "", variant: str | None = None,
            index: str | int | None = None, index_format_string: str = "/{index}"
    ):
        """

        :param client:
        :param path:
        :param index:
        :param variant:
        """
        self._models = deepcopy(self._models)
        if index in range(1, 9):
            self._models.extend(deepcopy(self._premium_fx))
        super().__init__(
            client=client, path=path, variant=variant, index=index,
            index_format_string=index_format_string
        )
