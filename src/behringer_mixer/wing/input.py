"""

"""
from copy import deepcopy

from behringer_mixer.component import Component

from . import processing_strip
from . import endpoint

from .component import PluginComponent, EQBand
from .plugins import filter, gate, eq, dyn, multi_purpose


class InputInSettings(processing_strip.InSettings):
    """

    """
    _endpoints = deepcopy(processing_strip.InSettings._endpoints)
    _endpoints.update({
        "mode": {
            "path": "/$mode",
            "class": endpoint.InputModeEndpoint,
            "read_only": True,
            "aliases": [ "input_mode" ]
        },
        "alt_switch_source": {
            "path": "/srcauto",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "GLOBAL",
                False: "INDIVIDUAL"
            },
            "aliases": [ "auto_source", "srcauto" ]
        },
        "alt_switch": {
            "path": "/altsrc",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "Alt",
                False: "Main"
            },
            "aliases": [ "alt_source", "alt_src", "altsrc" ]
        },
        "invert_polarity": {
            "path": "/inv",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "inv", "phase_invert" ]
        },
        "trim": {
            "path": "/trim",
            "class": endpoint.FloatEndpoint,
            "min": -18.0,
            "max": 18.0,
            "aliases": [ "input_trim" ]
        },
        "balance": {
            "path": "/bal",
            "class": endpoint.FloatEndpoint,
            "min": -9.0,
            "max": 9.0,
            "aliases": [ "input_balance", "bal" ]
        },
        "gain": {
            "path": "/$g",
            "class": endpoint.FloatEndpoint,
            "min": -3.0,
            "max": 45.5,
            "aliases":  [ "input_gain", "g" ]
        },
        "phantom": {
            "path": "/$vph",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "phantom_power", "input_phantom_power", "vph" ]
        },
        "delay": {
            "path": "",
            "class": endpoint.DelayEndpoint,
            "enable_path": "/dlyon",
            "mode_path": "/dlymode",
            "value_path": "/dly",
            "aliases": [ "input_delay" ]
        }
    })


class InputInConnSource(Component):
    """

    """
    _components = {}

    _endpoints = {
        "group": {
            "path": "grp",
            "class": endpoint.SourceGroupEndpoint,
            "aliases":  [ "grp" ]
        },
        "index": {
            "path": "in",
            "class": endpoint.IntEndpoint,
            "min": 1,
            "max": 64,
            "read_offset": 1,
            "aliases": [ "group_index", "input" ]
        }
    }


class InputInConn(Component):
    """

    """
    _components = {
        "main": {
            "path": "/",
            "class": InputInConnSource
        },
        "alt": {
            "path": "/alt",
            "class": InputInConnSource
        }
    }

    _endpoints = {}


class InputIn(Component):
    """

    """
    _components = {
        "settings": {
            "path": "/set",
            "class": InputInSettings,
            "aliases": [ "set" ]
        },
        "source": {
            "path": "/conn",
            "class": InputInConn,
            "aliases": [ "conn", "con", "connection" ]
        }
    }

    _endpoints = {}


class InputSends(processing_strip.SendComponent):
    """

    """
    _endpoints = deepcopy(processing_strip.SendComponent._endpoints)
    _endpoints.update({
        "ignore_channel_mute": {
            "path": "/pon",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "pon", "pre_always_on" ]
        },
        "mode": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "PRE": "TAP",
                "POST": "POST",
                "GRP": "GROUP"
            }
        },
        "link_send_pan_to_channel_pan": {
            "path": "/plink",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "plink", "pan_link" ]
        },
        "pan": {
            "path": "/pan",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0
        }
    })


class Input(processing_strip.ProcessingStrip):
    """

    """
    _components = deepcopy(processing_strip.ProcessingStrip._components)
    _components.update({
        "input": {
            "path": "/in",
            "class": InputIn
        },
        "eq": {
            "path": "/eq",
            "class": processing_strip.EQ
        },
        "main_send": {
            "variants": {
                "fullsize": {
                    "path": "/main",
                    "class": processing_strip.Sends,
                    "count": 4,
                },
                "compact": {
                    "path": "/main",
                    "class": processing_strip.Sends,
                    "count": 4
                },
                "rack": {
                    "path": "/main",
                    "class": processing_strip.Sends,
                    "count": 8
                }
            },
            "aliases": [ "main" ]
        },
        "bus_send": {
            "path": "/send",
            "class": InputSends,
            "count": 16,
            "aliases": [ "send", "bus" ]
        },
        "matrix_send": {
            "path": "/send/MX",
            "class": InputSends,
            "count": 8,
            "index_format_string": "{index}",
            "aliases": [ "matrix", "mtx", "mx" ]
        },
    })

    _endpoints = deepcopy(processing_strip.ProcessingStrip._endpoints)
    _endpoints.update({
        "custom_link": {
            "path": "/clink",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "clink" ]
        },
        "solo_safe": {
            "path": "/solosafe",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "solosafe" ]
        },
    })


class ChannelPreSendEQ(Component):
    """

    """
    _components = {
        "band": {
            "path": "",
            "class": EQBand,
            "count": 3
        }
    }

    _endpoints = {
        "enable": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "on" ]
        }
    }


class ChannelGateSidechain(Component):
    """

    """
    _components = {}

    _endpoints = {
        "type": {
            "path": "/type",
            "class": endpoint.StringEnumEndpoint,
            # Documentation states a valid string is 'Off' but it is actually 'OFF'
            "valid_strings": [ "OFF", "LP12", "HP12", "BP" ]
        },
        "frequency": {
            "path": "/f",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 20000.0
        },
        "q": {
            "path": "/q",
            "class": endpoint.FloatEndpoint,
            "min": 0.44,
            "max": 10.0
        },
        "source": {
            "path": "/src",
            "class": endpoint.StringEnumEndpoint,
            # Documentation states a valid string is 'SHELF' but it is actually 'SELF'
            "valid_strings": [
                "SELF", "Ch.1", "Ch.2", "Ch.3", "Ch.4", "Ch.5", "Ch.6", "Ch.7", "Ch.8",
                "Ch.9", "Ch.10", "Ch.11", "Ch.12", "Ch.13", "Ch.14", "Ch.15", "Ch.16",
                "Ch.17", "Ch.18", "Ch.19", "Ch.20", "Ch.21", "Ch.22", "Ch.23", "Ch.24",
                "Ch.25", "Ch.26", "Ch.27", "Ch.28", "Ch.29", "Ch.30", "Ch.31", "Ch.32",
                "Ch.33", "Ch.34", "Ch.35", "Ch.36", "Ch.37", "Ch.38", "Ch.39", "Ch.40"
            ]
        },
        "solo": {
            "path": "/$solo",
            "class": endpoint.BoolEndpoint
        }
    }


class ChannelFilter(PluginComponent):
    """

    """
    _models = [
        filter.TiltFilter,
        filter.MaximizerFilter,
        filter.AllPass90Filter,
        filter.AllPass180Filter
    ]


class ChannelGate(PluginComponent):
    """

    """
    _endpoints = {
        "enable": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "on" ]
        }
    }

    _components = {
        "sidechain": {
            "path": "sc",
            "class": ChannelGateSidechain
        }
    }

    _models = [
        gate.StandardGate,
        gate.StandardDucker,
        gate.Even88Gate,
        gate.SSL9000Gate,
        gate.DrawMoreExpGate241,
        gate.DBX902DeEsser,
        multi_purpose.WaveDesigner,
        gate.DynamicEQ,
        gate.SoulWarmthPreamp,
        multi_purpose.LimitingAmp76,
        multi_purpose.LevelingAmplifier2A,
        multi_purpose.AutoRiderDynamics,
        multi_purpose.SourceExtractor,
        multi_purpose.PSELACombo
    ]


class ChannelEQ(processing_strip.EQ):
    """

    """
    _models = [
        eq.Standard6BandEQ,
        eq.SoulAnalogEQ,
        eq.Even88FormantEQ,
        eq.Even84EQ,
        eq.FocusriteISA110EQ,
        eq.PulsarP1aM5EQ,
        eq.MachEQ4
    ]


class ChannelDynKey(processing_strip.DynKey):
    """

    """
    _endpoints = deepcopy(processing_strip.DynKey._endpoints)
    _endpoints["source"].update({
        "valid_strings": [
            "SELF", "CH.1", "CH.2", "CH.3", "CH.4", "CH.5", "CH.6", "CH.7", "CH.8",
            "CH.9", "CH.10", "CH.11", "CH.12", "CH.13", "CH.14", "CH.15", "CH.16",
            "CH.17", "CH.18", "CH.19", "CH.20", "CH.21", "CH.22", "CH.23", "CH.24",
            "CH.25", "CH.26", "CH.27", "CH.28", "CH.29", "CH.30", "CH.31", "CH.32",
            "CH.33", "CH.34", "CH.35", "CH.36", "CH.37", "CH.38", "CH.39", "CH.40",
        ]
    })
    _endpoints["tap"].update({
        "string_mapping": {
            "IN": "INPUT",
            "FILT": "FILTER",
            "3": "TAP 3",
            "4": "TAP 4",
            "5": "TAP 5",
            "PFL": "PRE FDR",
            "AFL": "POST FDR",
            "POST": "POST PROC"
        }
    })


class ChannelDyn(processing_strip.Dyn):
    """

    """
    _components = deepcopy(processing_strip.Dyn._components)
    _components["key"].update({
        "class": ChannelDynKey
    })


class ChannelPostInsert(processing_strip.Insert):
    """

    """
    _endpoints = deepcopy(processing_strip.Insert._endpoints)
    _endpoints.update({
        "mode": {
            "path": "/mode",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "FX": "FX",
                "AUTO_X": "AUTO-X",
                "AUTO_Y": "AUTO-Y"
            }
        },
        "autogain_weight": {
            "path": "/w",
            "class": endpoint.FloatEndpoint,
            "min": -12.0,
            "max": 12.0,
            "aliases": [ "w", "weight" ]
        }
    })


class Channel(Input):
    """

    """
    _components = deepcopy(Input._components)
    _components.update({
        "filter": {
            "path": "/flt",
            "class": ChannelFilter,
            "aliases": [ "flt" ]
        },
        "presend_eq": {
            "path": "/peq",
            "class": ChannelPreSendEQ,
            "aliases": [ "peq" ]
        },
        "gate": {
            "path": "/gate",
            "class": ChannelGate
        },
        "eq": {
            "path": "/eq",
            "class": ChannelEQ,
            "aliases": [ "equalizer" ]
        },
        "dynamics": {
            "path": "/dyn",
            "class": ChannelDyn,
            "aliases": [ "dyn", "compressor" ]
        },
        "post_insert": {
            "path": "/postins",
            "class": ChannelPostInsert,
            "aliases": [ "postins" ]
        }
    })

    _endpoints = deepcopy(Input._endpoints)
    _endpoints.update({
        "process_order": {
            "path": "/proc",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "GEDI", "GEID", "GIED", "IGED", "GDEI", "GDIE", "GIDE", "IGDE", "EGDI", "EGID",
                "EIGD", "IEGD", "EDGI", "EDIG", "EIDG", "IEDG", "DEGI", "DEIG", "DIEG", "IDEG",
                "DGEI", "DGIE", "DIGE", "IDGE"
            ],
            "aliases": [ "proc" ]
        },
        "pretap": {
            "path": "/ptap",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "IN", "FILT", "3", "4", "5", "PFL", "AFL", "POST"
            ],
            "aliases": [ "ptap" ]
        },
        "presolo": {
            "path": "/$presolo",
            "class": endpoint.BoolEndpoint
        },
        "tap_width": {
            "path": "/tapwid",
            "class": endpoint.FloatEndpoint,
            "min": -150.0,
            "max": 150.0,
            "aliases": [ "tapwid" ]
        }
    })


class AuxEQ(processing_strip.EQ):
    """

    """
    _models = [
        eq.Standard6BandEQ,
        eq.SoulAnalogEQ,
        eq.Even88FormantEQ,
        eq.Even84EQ,
        eq.FocusriteISA110EQ,
        eq.PulsarP1aM5EQ,
    ]


class AuxDyn(multi_purpose.PSELACombo):
    """

    """
    _endpoints = deepcopy(multi_purpose.PSELACombo._endpoints)
    _endpoints.update({
        "power": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "ON",
                False: "OFF"
            },
            "aliases": [ "enable", "on" ]
        }
    })


class Aux(Input):
    """

    """
    _components = deepcopy(Input._components)
    _components.update({
        "eq": {
            "path": "/eq",
            "class": AuxEQ,
            "aliases": [ "equalizer" ]
        },
        "dynamics": {
            "path": "/dyn",
            "class": AuxDyn,
            "aliases": [ "dyn", "compressor" ]
        },
    })

    _endpoints = deepcopy(Input._endpoints)
    _endpoints.update({
        "power": {
            "path": "/on",
            "class": endpoint.BoolEndpoint,
            "name_mapping": {
                True: "ON",
                False: "OFF"
            },
            "aliases": [ "on" ]
        }
    })
