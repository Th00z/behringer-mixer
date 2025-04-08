"""

"""
from netaddr import IPAddress

from behringer_mixer.component import Component
from .endpoint import StringEndpoint, StringEnumEndpoint, BoolEndpoint, IPv4Endpoint


class SystemConsoleConfiguration(Component):
    """

    """
    _components = {}

    _endpoints = {
        "name": {
            "path": "/consolename",
            "class": StringEndpoint,
            "max_chars": 16
        },
        "variant": {
            "path": "/$cnscfg",
            "class": StringEndpoint,
            "max_chars": 64,
            "read_only": True
        },
        "model": {
            "path": "/$cnsmdl",
            "class": StringEndpoint,
            "max_chars": 32,
            "read_only": True
        }
    }


class SystemIPConfiguration(Component):
    """

    """
    _components = {}

    _endpoints = {
        "mode": {
            "path": "/ipmode",
            "class": StringEnumEndpoint,
            "valid_strings": [ "DHCP", "STATIC" ]
        },
        "address": {
            "path": "/ip",
            "class": IPv4Endpoint,
            "read_only": False
        },
        "netmask": {
            "path": "/msk",
            "class": IPv4Endpoint,
            "read_only": False
        },
        "gateway": {
            "path": "/gw",
            "class": IPv4Endpoint,
            "read_only": False
        },
        "apply": {
            "path": "/$ipapply",
            "class": BoolEndpoint,
            "read_only": False
        }
    }


class SystemModuleConfiguration(Component):
    """

    """
    _components = {}

    _endpoints = {
        "ethernet_mode": {
            "path": "/eth_cfg",  # Documentation says '/etc/cfg'. This is a typo.
            "class": StringEnumEndpoint,
            "valid_strings": [
                "SEPARATED",  # Documentation says 'SEPARATE'. This is a typo.
                "SWITCHED"
            ]
        },
        "installed": {
            "path": "/opt_mod",
            "class": StringEnumEndpoint,
            "valid_strings": [ "NONE", "DANTE", "WSG" ],
            "read_only": True
        }
    }


class SystemConfiguration(Component):
    """

    """
    _components = {
        "console": {
            "path": "",
            "class": SystemConsoleConfiguration
        },
        "ip": {
            "path": "",
            "class": SystemIPConfiguration
        },
        "optional_module": {
            "path": "",
            "class": SystemModuleConfiguration
        }
    }

    _endpoints = {
        "log_flags": {
            "path": "/logflags",
            "class": StringEndpoint,
            "max_chars": 256
        },
        "firmware_version": {
            "path": "/$firmware",
            "class": StringEndpoint,
            "max_chars": 64,
            "read_only": True
        },
        "serial": {
            "path": "/$serial",
            "class": StringEndpoint,
            "max_chars": 32,
            "read_only": True
        },
        "mainboard_hardware_version": {
            "path": "/$hwversion",  # Documentation says $chwversion, this must be a typo!
            "class": StringEndpoint,
            "max_chars": 32,
            "read_only": True
        },
        "tcp_lock": {
            "path": "/tcplock",
            "class": BoolEndpoint,
        },
        "usb_driver_speed": {
            "path": "/usbh_spd",
            "class": StringEnumEndpoint,
            "read_path": "/$usbspd_act",
            "valid_strings": [ "FS", "HS" ]
        }
    }
