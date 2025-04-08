"""

"""
from datetime import datetime

from behringer_mixer.component import Component
from .endpoint import (
    StringEnumEndpoint, StringEndpoint, BoolEndpoint, IntEndpoint,
    DatetimeEndpoint
)

class StatusAES50Port(Component):
    """

    """
    _components = {}

    _endpoints = {
        "status": {
            "path": "/stat",
            "class": StringEnumEndpoint,
            "read_only": True,
            "valid_strings": ["-", "OK", "ERR", "UPD"]
        },
        "device": {
            "path": "/dev",
            "class": StringEndpoint,
            "read_only": True,
        }
    }


class StatusClock(Component):
    """

    """
    _components = {}

    _endpoints = {
        "lock": {
            "path": "/lock",
            "class": BoolEndpoint,
            "read_only": True
        },
        "ppm": {
            "path": "/ppm",
            "class": IntEndpoint,
            "read_only": True,
            "min": -200,
            "max": 200
        },
        "real_time_error": {
            "path": "/rtcerr",
            "class": BoolEndpoint,
            "read_only": True
        },
    }


class StatusUSBPlayer(Component):
    """

    """
    _components = {}

    _endpoints = {
        "status": {
            "path": "state",
            "class": StringEnumEndpoint,
            "read_only": True,
            "valid_strings": ["-", "ERR", "IDLE", "BUSY"]
        },
        "volume_name": {
            "path": "volname",
            "class": StringEndpoint,
            "read_only": True,
            "max_chars": 20
        }
    }


class StatusStageConnect(Component):
    """

    """
    _components = {}

    _endpoints = {
        "status": {
            "path": "_stat",
            "class": StringEnumEndpoint,
            "read_only": True,

            # "-" is not a valid value according to the API documentation, though my console
            # outputs exactly that when there are no SC-Devices connected. The
            # API documentation seems to be wrong here.
            "valid_strings": ["-", "OK", "ERR"]
        },
        "devices": {
            "path": "_devices",
            "class": StringEndpoint,
            "read_only": True
        },
        "upstreams": {
            "path": "_upcnt",
            "class": IntEndpoint,
            "read_only": True,
            "min": 0,
            "max": 32
        },
        "downstreams": {
            "path": "_dncnt",
            "class": IntEndpoint,
            "read_only": True,
            "min": 0,
            "max": 32
        },
        "upstream_routing": {
            "path": "_uprout",
            "class": StringEndpoint,
            "read_only": True,
            "max_chars": 32
        }
    }


class Status(Component):
    """

    """
    _components = {
        "aes50_a": {
            "path": "/A",
            "class": StatusAES50Port
        },
        "aes50_b": {
            "path": "/B",
            "class": StatusAES50Port
        },
        "aes50_c": {
            "path": "/C",
            "class": StatusAES50Port
        },
        "clock": {
            "path": "",
            "class": StatusClock
        },
        "usb_player": {
            "path": "/usb",
            "class": StatusUSBPlayer
        },
        "stage_connect": {
            "path": "/sc",
            "class": StatusStageConnect
        }
    }

    _endpoints = {
        "solo": {
            "path": "/solo",
            "class": BoolEndpoint,
            "read_only": True
        },
        "solo_in_place": {
            "path": "/sip",
            "class": BoolEndpoint,
            "read_only": True
        },
        "current_time": {
            "path": "",
            "class": DatetimeEndpoint,
            "date_endpoint": {
                "path": "/date",
                "class": StringEndpoint,
                "read_only": True,
                "max_chars": 12
            },
            "time_endpoint": {
                "path": "/time",
                "class": StringEndpoint,
                "read_only": True,
                "max_chars": 12
            }
        },
        "remote_a": {
            "path": "/rmt_a",
            "class": StringEndpoint,
            "read_only": True,
            "max_chars": 16
        },
        "remote_b": {
            "path": "/rmt_b",
            "class": StringEndpoint,
            "read_only": True,
            "max_chars": 16
        },
        "remote_c": {
            "path": "/rmt_c",
            "class": StringEndpoint,
            "read_only": True,
            "max_chars": 16
        },
    }
