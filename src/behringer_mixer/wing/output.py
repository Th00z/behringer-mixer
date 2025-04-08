"""

"""
from copy import deepcopy

from behringer_mixer.component import Component

from . import processing_strip
from . import endpoint

from .plugins import eq


class OutputIn(Component):
    """

    """
    _components = {
        "settings": {
            "path": "/set",
            "class": processing_strip.InSettings,
            "aliases": [ "set" ]
        }
    }

    _endpoints = {}


class OutputEQ(processing_strip.EQ):
    """

    """
    _endpoints = deepcopy(processing_strip.EQ._endpoints)
    _endpoints["solo_band"].update({ "max": 7 })
    _models = [
        eq.StandardSendEQ,
        eq.SoulAnalogEQ,
        eq.Even88FormantEQ,
        eq.Even84EQ,
        eq.FocusriteISA110EQ,
        eq.PulsarP1aM5EQ,
        eq.PIA560GEQ
    ]


class OutputDynKey(processing_strip.DynKey):
    """

    """
    _endpoints = deepcopy(processing_strip.DynKey._endpoints)
    _endpoints["source"].update({
        "valid_strings": [
            "SELF", "BUS.1", "BUS.2", "BUS.3", "BUS.4", "BUS.5", "BUS.6", "BUS.7", "BUS.8",
            "BUS.9", "BUS.10", "BUS.11", "BUS.12", "BUS.13", "BUS.14", "BUS.15", "BUS.16",
            "MTX.1", "MTX.2", "MTX.3", "MTX.4", "MTX.5", "MTX.6", "MTX.7", "MTX.8",
            "AUX.1", "AUX.2", "AUX.3", "AUX.4", "AUX.5", "AUX.6", "AUX.7", "AUX.8",
            "MAIN.1", "MAIN.2", "MAIN.3", "MAIN.4"
        ]
    })
    _endpoints["tap"].update({
        "string_mapping": {
            "BUS": "BUS IN",
            "DYN": "DYNAMICS",
            "PFL": "PRE FDR",
            "AFL": "POST FDR",
            "EQ": "POST EQ",
            "INS2": "POST INS2"
        }
    })


class OutputDyn(processing_strip.Dyn):
    """

    """
    _components = deepcopy(processing_strip.Dyn._components)
    _components["key"].update({
        "class": OutputDynKey
    })


class Output(processing_strip.ProcessingStrip):
    """

    """
    _components = deepcopy(processing_strip.ProcessingStrip._components)
    _components.update({
        "input": {
            "path": "/in",
            "class": OutputIn
        },
        "eq": {
            "path": "/eq",
            "class": OutputEQ,
            "aliases": [ "equalizer" ]
        },
        "dynamics": {
            "path": "/dyn",
            "class": OutputDyn,
            "aliases": [ "dyn", "compressor" ]
        },
        "post_insert": {
            "path": "/postins",
            "class": processing_strip.Insert,
            "aliases": [ "postins" ]
        },
    })

    _endpoints = deepcopy(processing_strip.ProcessingStrip._endpoints)
    _endpoints.update({
        "mono": {
            "path": "/busmono",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "busmono" ]
        },
        "delay": {
            "path": "",
            "class": endpoint.DelayEndpoint,
            "enable_path": "/dly/on",
            "mode_path": "/dly/mode",
            "value_path": "/dly/dly",
            "aliases": [ "dly" ]
        }
    })


class MatrixDirectIn(processing_strip.SendComponent):
    """

    """
    _endpoints = deepcopy(processing_strip.SendComponent._endpoints)
    _endpoints.update({
        "invert_polarity": {
            "path": "/inv",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "inv", "phase_invert" ]
        },
        "input_source": {
            "path": "/in",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "OFF": "OFF",
                "AES": "AES",
                "MON.PH": [ "PHONES", "PH" ],  # Documentation says "MON.A" but it is "MON.PH"
                "MON.SPK": [ "SPEAKERS", "SPK" ],  # Documentation says "MON.B" but it is "MON.SPK"
                "MON.BUS": [ "SOLO BUS", "S" ]
            },
            "aliases": [ "input", "source" ]
        }
        # Documentation also lists /tap but my console does not yield it. There is also
        # no direct in tap in the console UI.
    })


class Matrix(Output):
    """

    """
    _components = deepcopy(Output._components)
    _components.update({
        "direct_input": {
            "path": "/dir",
            "class": MatrixDirectIn,
            "aliases": [ "dir", "direct_input_signal", "direct_in" ]
        }
    })


class Main(Output):
    """

    """
    _components = deepcopy(Output._components)
    _components.update({
        "matrix_send": {
            "path": "/send/MX",
            "class": processing_strip.Sends,
            "count": 8,
            "index_format_string": "{index}",
            "aliases": [ "matrix", "mtx", "mtx_send", "mx", "mx_send" ]
        }
    })


class Bus(Main):
    """

    """
    _components = deepcopy(Main._components)
    _components.update({
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
            "aliases": ["main"]
        },
        "bus_send": {
            "path": "/send",
            "class": processing_strip.Sends,
            "count": 16,
            "aliases": [ "send", "bus" ]
        }
    })
