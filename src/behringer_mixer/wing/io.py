"""

"""
from copy import deepcopy

from behringer_mixer.component import Component
from .endpoint import (
    BoolEndpoint, IntEndpoint, StringEndpoint, FloatEndpoint, StringEnumEndpoint,
    InputModeEndpoint, PrePostEndpoint, OutSourceGroupEndpoint
)
from .utils import Icon, Color


class IOBusInput(Component):
    """

    """
    _components = {}

    _endpoints = {
        "mode": {
            "path": "/mode",
            "class": InputModeEndpoint,
            "read_only": True
        },
        "color": {
            "path": "/col",
            "class": IntEndpoint,
            "values": Color,
            "read_offset": 1,
            "read_only": True
        },
        "name": {
            "path": "/name",
            "class": StringEndpoint,
            "max_chars": 16,
            "read_only": True
        },
        "icon": {
            "path": "/icon",
            "class": IntEndpoint,
            "values": Icon,
            "read_only": True
        },
        "tags": {
            "path": "/tags",
            "class": StringEndpoint,
            "max_chars": 80,
            "read_only": True
        }
    }


class IOStandardInput(Component):
    """

    """
    _components = {}

    _endpoints = {
        "mode": {
            "path": "/mode",
            "class": InputModeEndpoint
        },
        "mute": {
            "path": "/mute",
            "class": BoolEndpoint
        },
        "invert_polarity": {
            "path": "/pol",
            "class": BoolEndpoint
        },
        "color": {
            "path": "/col",
            "class": IntEndpoint,
            "values": Color,
            "read_offset": 1
        },
        "name": {
            "path": "/name",
            "class": StringEndpoint,
            "max_chars": 16
        },
        "icon": {
            "path": "/icon",
            "class": IntEndpoint,
            "values": Icon
        },
        "tags": {
            "path": "/tags",
            "class": StringEndpoint,
            "max_chars": 80
        },
        "mute_value": {  # Whatever these 3 mute-states are...
            "path": "/$mute",
            "class": IntEndpoint,
            "read_only": True,
            "min": 0,
            "max": 2
        }
    }


class InputRemote(Component):
    """

    """
    _components = {}

    _endpoints = {
        "control": {
            "path": "/rmt",
            "class": StringEnumEndpoint,
            "valid_strings": [ "OFF", "AES A", "AES B", "AES C" ]
        },
        "active": {
            "path": "/$ract",
            "class": BoolEndpoint,
            "read_only": True
        },
        "destination": {
            "path": "/$rdest",
            "class": StringEndpoint,
            "read_only": True,
            "max_chars": 7
        },
        "customizations_sync": {
            "path": "/rcvc",
            "class": BoolEndpoint
        }
    }


class IOPreampedInput(IOStandardInput):
    """

    """
    _components = deepcopy(IOStandardInput._components)
    _components.update({
        "remote": {
            "path": "",
            "class": InputRemote
        }
    })

    _endpoints = deepcopy(IOStandardInput._endpoints)
    _endpoints.update({
        "gain": {
            "path": "/g",
            "class": FloatEndpoint,
            "min": -3.0,
            "max": 45.5
        },
        "phantom": {
            "path": "/vph",
            "class": BoolEndpoint
        },
        "ha_type": {  # Whatever this is
            "path": "/$ha",
            "class": IntEndpoint,
            "read_only": True,
            "min": 0,
            "max": 5
        }
    })

class IOInputAES50(Component):
    """

    """
    _components = {
        "a": {
            "path": "/A",
            "class": IOPreampedInput,
            "count": 48
        },
        "b": {
            "path": "/B",
            "class": IOPreampedInput,
            "count": 48
        },
        "c": {
            "path": "/C",
            "class": IOPreampedInput,
            "count": 48
        }
    }

    _endpoints = {}


class IOInputUSB(Component):
    """

    """
    _components = {
        "audio": {
            "path": "/USB",
            "class": IOStandardInput,
            "count": 48
        },
        "player": {
            "path": "/PLAY",
            "class": IOStandardInput,
            "count": 4
        }
    }

    _endpoints = {}


class IOUserSignalInputSource(Component):
    """

    """
    _components = {}

    _endpoints = {
        "group": {
            "path": "/grp",
            "class": StringEnumEndpoint,
            "valid_strings": [ "OFF", "CH", "AUX", "BUS", "MAIN", "MTX" ]
        },
        "index": {
            "path": "/in",
            "class": IntEndpoint,
            "min": 0,
            "max": 40,
            "read_offset": 1
        },
        "tap_point": {
            "path": "/tap",
            "class": PrePostEndpoint
        },
        "mode": {
            "path": "/lr",
            "class": StringEnumEndpoint,
            "valid_strings": [ "L+R", "L", "R" ]
        }
    }


class IOUserSignalInput(IOStandardInput):
    """

    """
    _components = deepcopy(IOStandardInput._components)
    _components.update({
        "source": {
            "path": "/user",
            "class": IOUserSignalInputSource
        }
    })


class IOOscillatorInputSource(Component):
    """

    """
    _components = {}

    _endpoints = {
        "level": {
            "path": "/lvl",
            "class": FloatEndpoint,
            "min": -40.0,
            "max": 6.0
        },
        "mode": {
            "path": "/mode",
            "class": StringEnumEndpoint,
            "valid_strings": [ "SINE", "PINK", "WHITE" ]
        },
        "frequency": {
            "path": "/f",
            "class": FloatEndpoint,
            "min": 20.0,
            "max": 20000.0
        }
    }


class IOOscillatorInput(Component):
    """

    """
    _components = {
        "source": {
            "path": "/osc",
            "class": IOOscillatorInputSource
        }
    }

    _endpoints = {
        "mode": {
            "path": "/mode",
            "class": InputModeEndpoint
        },
        "mute": {
            "path": "/mute",
            "class": BoolEndpoint
        },
        "color": {
            "path": "/col",
            "class": IntEndpoint,
            "values": Color,
            "read_offset": 1
        },
        "name": {
            "path": "/name",
            "class": StringEndpoint,
            "max_chars": 16
        },
        "icon": {
            "path": "/icon",
            "class": IntEndpoint,
            "values": Icon
        },
        "tags": {
            "path": "/tags",
            "class": StringEndpoint,
            "max_chars": 80
        },
        "mute_value": {  # Whatever these 3 mute-states are...
            "path": "/$mute",
            "class": IntEndpoint,
            "read_only": True,
            "min": 0,
            "max": 2
        }
    }


class IOInput(Component):
    """

    """

    _components = {
        "local": {
            "path": "/LCL",
            "class": IOPreampedInput,
            # Even though not all variants have 24 physical inputs they are still all addressable
            # and routable in the UI
            "count": 24
        },
        "aux": {
            "path": "/AUX",
            "class": IOStandardInput,
            "count": 8
        },
        "aes50": {
            "path": "",
            "class": IOInputAES50
        },
        "stage_connect": {
            "path": "/SC",
            "class": IOStandardInput,
            "count": 32
        },
        "usb": {
            "path": "",
            "class": IOInputUSB,
        },
        "card": {
            "path": "/CRD",
            "class": IOStandardInput,
            "count": 64
        },
        "module": {
            "path": "/MOD",
            "class": IOStandardInput,
            "count": 64
        },
        "aes": {
            "path": "/AES",
            "class": IOStandardInput,
            "count": 2
        },
        "user": {
            "path": "/USR",
            "class": IOUserSignalInput,
            "count": 48
        },
        "oscillator": {
            "path": "/OSC",
            "class": IOOscillatorInput,
            "count": 2
        },
        "bus": {
            "path": "/$BUS",
            "class": IOBusInput,
            "count": 32
        },
        "main": {
            "path": "/$MAIN",
            "class": IOBusInput,
            "count": 8
        },
        "matrix": {
            "path": "/$MTX",
            "class": IOBusInput,
            "count": 16
        },
        "fx_send": {
            "path": "/$SEND",
            "class": IOBusInput,
            "count": 32
        },
        "monitor": {
            "path": "/$MON",
            "class": IOBusInput,
            "count": 4
        }
    }
    _endpoints = {}


class IOStandardOutput(Component):
    """

    """
    _components = {}

    _endpoints = {
        "source_group": {
            "path": "/grp",
            "class": OutSourceGroupEndpoint
        },
        "source_index": {
            "path": "/in",
            "class": IntEndpoint,
            "min": 0,
            "max": 64,
            "read_offset": 1
        }
    }


class IOOutputAES50(Component):
    """

    """
    _components = {
        "a": {
            "path": "/A",
            "class": IOStandardOutput,
            "count": 48
        },
        "b": {
            "path": "/B",
            "class": IOStandardOutput,
            "count": 48
        },
        "c": {
            "path": "/C",
            "class": IOStandardOutput,
            "count": 48
        },
    }

    _endpoints = {}


class IOOutputUSB(Component):
    """

    """
    _components = {
        "audio": {
            "path": "/USB",
            "class": IOStandardOutput,
            "count": 48
        },
        "recorder": {
            "path": "/REC",
            "class": IOStandardOutput,
            "count": 4
        }
    }

    _endpoints = {}


class IOOutput(Component):
    """

    """
    _components = {
        "local": {
            "path": "/LCL",
            "class": IOStandardOutput,
            "count": 8
        },
        "aux": {
            "path": "/AUX",
            "class": IOStandardOutput,
            "count": 8
        },
        "aes50": {
            "path": "",
            "class": IOOutputAES50
        },
        "stage_connect": {
            "path": "/SC",
            "class": IOStandardOutput,
            "count": 32
        },
        "usb": {
            "path": "",
            "class": IOOutputUSB
        },
        "card": {
            "path": "/CRD",
            "class": IOStandardOutput,
            "count": 64
        },
        "module": {
            "path": "/MOD",
            "class": IOStandardOutput,
            "count": 64
        },
        "aes": {
            "path": "/AES",
            "class": IOStandardOutput,
            "count": 2
        }
    }

    _endpoints = {}


class IO(Component):
    """

    """
    _components = {
        "input": {
            "path": "/in",
            "class": IOInput
        },
        "output": {
            "path": "/out",
            "class": IOOutput
        }
    }

    _endpoints = {
        "global_alt_switch": {
            "path": "/altsw",
            "class": BoolEndpoint,
            "name_mapping": {
                True: "Alt",
                False: "Main"
            }
        },
        "global_input_select_override": {
            "path": "/autoaltovr",
            "class": BoolEndpoint
        }
    }
