"""

"""
from behringer_mixer.component import Component

from . import endpoint
from .component import EQBand, EQShelf

class MonitorDelay(Component):
    """

    """
    _components = {}

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
        "meters": {
            "path": "/m",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 100.0
        }
    }


class MonitorSource(Component):
    """

    """
    _components = {}

    _endpoints = {
        "level": {
            "path": "/srclvl",
            "class": endpoint.FaderEndpoint
        },
        "mix": {
            "path": "/srcmix",
            "class": endpoint.FaderEndpoint
        },
        "source": {
            "path": "/src",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "OFF",
                "MAIN.1", "MAIN.2", "MAIN.3", "MAIN.4",
                "MTX.1", "MTX.2", "MTX.3", "MTX.4", "MTX.5", "MTX.6", "MTX.7", "MTX.8",
                "BUS.1", "BUS.2", "BUS.3", "BUS.4", "BUS.5", "BUS.6", "BUS.7", "BUS.8",
                "BUS.9", "BUS.10", "BUS.11", "BUS.12", "BUS.13", "BUS.14", "BUS.15", "BUS.16",
                "AUX.1", "AUX.2", "AUX.3", "AUX.4", "AUX.5", "AUX.6", "AUX.7", "AUX.8"
            ]
        }
    }


class MonitorEQLowShelf(EQShelf):
    """

    """
    _frequency_max = 2000.0


class MonitorEQHighShelf(EQShelf):
    """

    """
    _frequency_min = 50.0


class Monitor6BandEQ(Component):
    """

    """
    _components = {
        "band": {
            "path": "",
            "class": EQBand,
            "count": 6
        },
        "low_shelf": {
            "path": "/l",
            "class": MonitorEQLowShelf
        },
        "high_shelf": {
            "path": "/h",
            "class": MonitorEQHighShelf
        }
    }

    _endpoints = {
        "on": {
            "path": "/on",
            "class": endpoint.BoolEndpoint
        },
    }


class MonitorConfiguration(Component):
    """

    """
    _components = {
        "eq": {
            "path": "/eq",
            "class": Monitor6BandEQ
        },
        "delay": {
            "path": "/dly",
            "class": MonitorDelay
        },
        "source": {
            "path": "",
            "class": MonitorSource
        }
    }

    _endpoints = {
        "level": {
            "variants": {
                "fullsize": {
                    "path": "/$lvl",
                    "class": endpoint.FaderEndpoint,
                    "read_only": True
                },
                "compact": {
                    "path": "/$lvl",
                    "class": endpoint.FaderEndpoint,
                },
                "rack": {
                    "path": "/$lvl",
                    "class": endpoint.FaderEndpoint,
                }
            }
        },
        "invert_polarity": {
            "path": "/inv",
            "class": endpoint.BoolEndpoint
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
            "max": 150.0
        },
        "limiter": {
            "path": "/lim",
            "class": endpoint.FloatEndpoint,
            "min": -40.0,
            "max": 0.0
        },
        "dim": {
            "path": "/dim",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 40.0
        },
        "pfl_dim": {
            "path": "/pfldim",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 40.0
        },
        "band_solo_trim": {
            "path": "/eqbdtrim",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 24.0
        },
        "fader_level": {
            "path": "/$lvlact",
            "class": endpoint.FaderEndpoint,
            "read_only": True
        },
        "tags": {
            "path": "/tags",
            "class": endpoint.StringEndpoint,
            "max_chars": 80
        }
    }


class SourceSoloConfiguration(Component):
    """

    """
    _components = {}

    _endpoints = {
        "mode": {
            "path": "/srcsolo",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["OFF", "CH39", "AUX7"]
        },
        "solo": {
            "path": "/$srcsolo",
            "class": endpoint.BoolEndpoint
        },
        "source_group": {
            "path": "/$srcsgrp",
            "class": endpoint.SourceSoloGroupEndpoint
        },
        "source_index": {
            "path": "/$srcsin",
            "class": endpoint.IntEndpoint,
            "min": 1,
            "max": 64,
            "read_offset": 1
        }
    }


class SoloConfiguration(Component):
    """

    """
    _components = {
        "source_solo": {
            "path": "",
            "class": SourceSoloConfiguration
        }
    }

    _endpoints = {
        "mode": {
            "path": "/mode",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["LIVE", "STUDIO", "SIP"]
        },
        "monitor": {
            "path": "/mon",
            "class": endpoint.StringEnumEndpoint,

            # Documentation says ["A", "B", "A+B"], but my desk actually
            # outputs ["PH", "SPK", "PH+SPK"]. Documentation seems to be wrong here.
            "valid_strings": ["PH", "SPK", "PH+SPK"]
        },
        "mute": {
            "path": "/mute",
            "class": endpoint.BoolEndpoint
        },
        "dim": {
            "path": "/$dim",
            "class": endpoint.BoolEndpoint
        },
        "mono": {
            "path": "/$mono",
            "class": endpoint.BoolEndpoint
        },
        "flip": {
            "path": "/$flip",
            "class": endpoint.BoolEndpoint
        },
        "channel_tap": {
            "path": "/chtap",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["PFL", "AFL"]
        },
        "bus_tap": {
            "path": "/bustap",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["PFL", "AFL"]
        },
        "main_tap": {
            "path": "/maintap",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["PFL", "AFL"]
        },
        "matrix_tap": {
            "path": "/mtxtap",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["PFL", "AFL"]
        },
    }


class RTAEQConfiguration(Component):
    """

    """
    _components = {}

    _endpoints = {
        "decay": {
            "path": "decay",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "SLOW", "MED", "FAST" ]
        },
        "detector": {
            "path": "det",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "PEAK", "RMS", "AVG" ]
        },
        "range": {
            "path": "range",
            "class": endpoint.FloatEndpoint,
            "valid_values": [ 30.0, 60.0 ]
        },
        "gain": {
            "path": "gain",
            "class": endpoint.FloatEndpoint,
            "min": -5.0,
            "max": 50.0
        },
        "autogain": {
            "path": "auto",
            "class": endpoint.BoolEndpoint
        }
    }


class RTAConfiguration(Component):
    """

    """
    _components = {
        "eq": {
            "path": "/eq",
            "class": RTAEQConfiguration,
        }
    }

    _endpoints = {
        "source": {
            "path": "/rtasrc",
            "read_path": "/$src",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "read_min": 1,
            "max": 76
        },
        "tap": {
            "path": "/rtatap",
            "read_path": "/$tap",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "IN", "POST", "FILT", "PREEQ", "POSTEQ", "PREFDR", "GATEK", "DYNK", "DYNXO",
                "PRETAP", "SOLO", "MON.A", "MON.B"
            ],
            "valid_read_strings": [
                "IN", "POST", "FILT", "PREEQ", "POSTEQ", "PREFDR", "GATEK", "DYNK", "DYNXO",
                "PRETAP", "SOLO", "MON.A", "MON.B", "FXIN", "FXOUT"
            ]
        },
        "decay": {
            "path": "/rtadecay",
            "read_path": "/$dec",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "SLOW", "MED", "FAST" ]
        },
        "detector": {
            "path": "/rtadet",
            "read_path": "/$det",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "PEAK", "RMS", "AVG" ],
            "valid_read_strings": [ "PEAK", "RMS" ]
        },
        "range": {
            "path": "/rtarange",
            "class": endpoint.FloatEndpoint,
            "valid_values": [ 30.0, 60.0 ]
        },
        "gain": {
            "path": "/rtagain",
            "class": endpoint.FloatEndpoint,
            "min": -5.0,
            "max": 50.0
        },
        "autogain": {
            "path": "/rtaauto",
            "class": endpoint.BoolEndpoint
        },
    }


class MetersTappingConfiguration(Component):
    """

    """
    _components = {}

    _endpoints = {
        "channel_tap": {
            "path": "/in",
            "class": endpoint.PrePostEndpoint
        },
        "bus_tap": {
            "path": "/bus",
            "class": endpoint.PrePostEndpoint
        },
        "main_tap": {
            "path": "/main",
            "class": endpoint.PrePostEndpoint
        },
        "matrix_tap": {
            "path": "/mtx",
            "class": endpoint.PrePostEndpoint
        },
        "dca_tap": {
            "path": "/dca",
            "class": endpoint.PrePostEndpoint
        }
    }


class MetersConfiguration(Component):
    """

    """
    _components = {
        "fader_section": {
            "path": "/mtrsfc",
            "class": MetersTappingConfiguration
        },
        "page": {
            "path": "/mtrpage",
            "class": MetersTappingConfiguration
        }
    }

    _endpoints = {
        "scope_source": {
            "path": "/scopesrc",
            "read_path": "/$scopesrc",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 76
        },
        "scope_tap": {
            "path": "/scopetap",
            "read_path": "/$scopetap",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "IN", "POST", "FILT", "PREEQ", "POSTEQ", "PREFDR", "GATEK", "DYNK", "DYNXO",
                "PRETAP", "SOLO", "MON.PH", "MON.SPK"
            ],
            "valid_read_strings": [
                "IN", "POST", "FILT", "PREEQ", "POSTEQ", "PREFDR", "GATEK", "DYNK", "DYNXO",
                "PRETAP", "SOLO", "MON.PH", "MON.SPK", "FXIN", "FXOUT"
            ]
        },
        "main_meter": {
            "path": "/mainmtr",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "SEL_CH", "MAIN.1", "MAIN.2", "MAIN.3", "MAIN.4",
                "MTX.1", "MTX.2", "MTX.3", "MTX.4", "MTX.5", "MTX.6", "MTX.7", "MTX.8",
            ]
        },
        "main_position": {
            "path": "/mainpos",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "AUTO", "PRE", "POST" ]
        }
    }


class TalkbackChannel(Component):
    """

    """
    _components = {}

    _endpoints = {
        "on": {
            "path": "/$on",
            "class": endpoint.BoolEndpoint
        },
        "mode": {
            "path": "/mode",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "AUTO", "PUSH", "LATCH" ]
        },
        "monitor_dim": {
            "path": "/mondim",
            # Documentation says this is an Integer on Talkback A, though the actual
            # value is a float, just like busdim. Documentation is wrong here!
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 40.0
        },
        "bus_dim": {
            "path": "/busdim",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 40.0
        },
        "use_send_levels": {
            "path": "/indiv",
            "class": endpoint.BoolEndpoint
        },
        "bus_assign": {
            "path": "",
            "class": endpoint.BoolEndpoint,
            "count": 16,
            "index_format_string": "/B{index}"
        },
        "matrix_assign": {
            "path": "",
            "class": endpoint.BoolEndpoint,
            "count": 8,
            "index_format_string": "/MX{index}"
        },
        "main_assign": {
            "path": "",
            "class": endpoint.BoolEndpoint,
            "count": 4,
            "index_format_string": "/M{index}"
        }
    }


class TalkbackConfiguration(Component):
    """

    """
    _components = {
        "channel": {
            "path": "",
            "class": TalkbackChannel,
            "count": 2,
            "alphabet_indexed": True
        },
    }

    _endpoints = {
        "assign": {
            "path": "/assign",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "OFF", "CH40", "AUX8" ]
        },
        "level": {
            "path": "/$lvl",
            "class": endpoint.FaderEndpoint,
            "read_only": True
        }
    }


class AutomixingConfiguration(Component):
    """

    """
    _components = {}

    _endpoints = {
        "x": {
            "path": "/x",
            "class": endpoint.BoolEndpoint,
        },
        "y": {
            "path": "/y",
            "class": endpoint.BoolEndpoint
        }
    }


class GeneralConfiguration(Component):
    """

    """
    _components = {
        "monitor_bus": {
            "path": "/mon",
            "class": MonitorConfiguration,
            "count": 2
        },
        "solo": {
            "path": "/solo",
            "class": SoloConfiguration
        },
        "rta": {
            "path": "/rta",
            "class": RTAConfiguration
        },
        "meters": {
            "path": "/mtr",
            "class": MetersConfiguration
        },
        "talkback": {
            "path": "/talk",
            "class": TalkbackConfiguration
        },
        "automix": {
            "path": "/amix",
            "class": AutomixingConfiguration
        }
    }

    _endpoints = {
        "main_link": {
            "path": "/mainlink",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": ["OFF", "2", "2-3", "2-4"]
        },
        "dca_mutegroups": {
            "path": "/dcamgrp",
            "class": endpoint.BoolEndpoint
        }
    }
