"""

"""
from copy import deepcopy

from behringer_mixer.component import Component

from . import endpoint

from .utils import Color, Icon
from .component import PluginComponent
from .plugins import eq, dyn, multi_purpose


class InSettings(Component):
    """

    """
    _components = {}

    _endpoints = {
        "invert_polarity": {
            "path": "/inv",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "phase_invert", "inv" ]
        },
        "trim": {
            "path": "/trim",
            "class": endpoint.FloatEndpoint,
            "min": -18.0,
            "max": 18.,
            "aliases": [ "input_trim" ]
        },
        "balance": {
            "path": "/bal",
            "class": endpoint.FloatEndpoint,
            "min": -9.0,
            "max": 9.0,
            "aliases": [ "input_balance", "bal" ]
        }
    }


class EQ(PluginComponent):
    """

    """
    _endpoints = {
        "enable": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "on" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 125.0
        },
        "solo": {
            "path": "/$solo",
            "class": endpoint.BoolEndpoint
        },
        "solo_band": {
            "path": "/$solobd",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 6,
            "aliases": [ "solobd" ]
        }
    }

    _models = []


class DynXover(Component):
    """

    """
    _components = {}

    _endpoints = {
        "depth": {
            "path": "/depth",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 20.0
        },
        "mode": {
            "path": "/type",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "OFF": "FLAT",
                "LO6": "6dB LO",
                "LO12": "12dB LO",
                "HI6": "6dB HI",
                "HI12": "12dB HI",
                "PC": "PRESENCE"
            },
            "aliases": [ "type" ]
        },
        "freq": {
            "path": "/f",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 20000.0,
            "aliases": [ "frequency" ]
        },
        "solo": {
            "path": "/$solo",
            "class": endpoint.BoolEndpoint
        }
    }


class DynKeyFilter(Component):
    """

    """
    _components = {}

    _endpoints = {
        "type": {
            "path": "/type",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "OFF": "FLAT",
                "LP12": "LOWPASS",
                "HP12": "HIGHPASS",
                "BP": "BANDPASS"
            }
        },
        "freq": {
            "path": "/f",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 20000.0,
            "aliases": [ "frequency", "f" ]
        },
        "q": {
            "path": "/q",
            "class": endpoint.FloatEndpoint,
            "min": 0.44,
            "max": 10.0
        }
    }


class DynKey(Component):
    """

    """
    _components = {
        "filter": {
            "path": "",
            "class": DynKeyFilter
        }
    }

    _endpoints = {
        "source": {
            "path": "/src",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": []
        },
        "tap": {
            "path": "/tap",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {}
        },
        "solo": {
            "path": "/$solo",
            "class": endpoint.BoolEndpoint
        }
    }


class Dyn(PluginComponent):
    """

    """
    _components = {
        "xover": {
            "path": "xo",
            "class": DynXover,
            "aliases": [ "crossover" ]
        },
        "key": {
            "path": "sc",
            "class": DynKey,
            "aliases": [ "sidechain" ]
        },
    }

    _endpoints = {
        "enable": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "on" ]
        },
        "mix": {
            "path": "/mix",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 100.0
        },
        "gain": {
            "path": "/gain",
            "class": endpoint.FloatEndpoint,
            "min": -6.0,
            "max": 12.0
        }
    }

    _models = [
        dyn.StandardCompressor,
        dyn.StandardExpander,
        dyn.BDX160CompressorLimiter,
        dyn.BDX560EasyCompressor,
        dyn.DrawMoreCompressor,
        dyn.REDCompressor,
        dyn.Soul9000ChannelCompressor,
        dyn.SoulGBusCompressor,
        dyn.EvenCompressorLimiter,
        dyn.EternalBliss,
        dyn.Amplifier76LimitingAmplifier,
        multi_purpose.LevelingAmplifier2A,
        multi_purpose.PSELACombo,
        dyn.FairkidModel670,
        dyn.NoStressor,
        dyn.PIA2250,
        dyn.LTA100Leveler,
        multi_purpose.WaveDesigner,
        multi_purpose.AutoRiderDynamics
    ]


class Insert(Component):
    """

    """
    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "enable" ]
        },
        "fx_processor": {
            "path": "/ins",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "NONE", "FX1", "FX2", "FX3", "FX4", "FX5", "FX6", "FX7", "FX8",
                "FX9", "FX10", "FX11", "FX12", "FX13", "FX14", "FX15", "FX16"
            ],
            "aliases": [ "ins", "insert" ]
        },
        "status": {
            "path": "/$stat",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "-", "OK", "N/A" ],
            "read_only": True,
            "aliases": [ "stat" ]
        }
    }


class SendComponent(Component):
    """

    """
    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "enable" ]
        },
        "level": {
            "path": "/lvl",
            "class": endpoint.FaderEndpoint,
            "aliases": [ "lvl" ]
        }
    }


class Sends(SendComponent):
    """

    """
    _endpoints = deepcopy(SendComponent._endpoints)
    _endpoints.update({
        # Documentation positions this on the Mains-global level, but this is obviously wrong
        "pre": {
            "path": "/pre",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "pre_fader" ]
        }
    })


class ProcessingStrip(Component):
    """

    """
    _components = {
        "pre_insert": {
            "path": "/preins",
            "class": Insert,
            "aliases": [ "preins" ]
        },
    }

    _endpoints = {
        "color": {
            "path": "/col",
            "read_path": "/$col",
            "class": endpoint.IntEndpoint,
            "values": Color,
            "read_offset": 1,
            "aliases": [ "col" ]
        },
        "name": {
            "path": "/name",
            "read_path": "/$name",
            "class": endpoint.StringEndpoint,
            "max_chars": 16
        },
        "icon": {
            "path": "/icon",
            "read_path": "/$icon",
            "class": endpoint.IntEndpoint,
            "values": Icon
        },
        "scribble_light": {
            "path": "/led",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "led" ]
        },
        "mute": {
            "path": "/mute",
            "class": endpoint.BoolEndpoint
        },
        "fader": {
            "path": "/fdr",
            "class": endpoint.FaderEndpoint,
            "aliases": [ "fdr" ]
        },
        "pan": {
            "path": "/pan",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0
        },
        "width": {
            "path": "/wid",
            "class": endpoint.FloatEndpoint,
            "min": -150.0,
            "max": 150.0,
            "aliases": [ "wid" ]
        },
        "solo": {
            "path": "/$solo",
            "class": endpoint.BoolEndpoint
        },
        "solo_led": {
            "path": "/$sololed",
            "class": endpoint.IntEndpoint,
            "read_only": True,
            "min": 0,
            "max": 2,
            "aliases": [ "sololed" ]
        },
        "monitor": {
            "path": "/mon",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "A", "B", "A+B" ],
            "aliases": [ "mon", "monitor_mode" ]
        },
        "tags": {
            "path": "/tags",
            "class": endpoint.StringEndpoint,
            "max_chars": 80
        },
        "post_dca_level": {
            "path": "/$fdr",
            "class": endpoint.FaderEndpoint,
            "read_only": True,
            "aliases": [ "post_dca_fader" ]
        },
        "post_group_mute": {
            "path": "/$mute",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 2,
            "read_only": True,
        },
        "mute_override": {
            "path": "/$muteovr",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "muteovr" ]
        }
    }