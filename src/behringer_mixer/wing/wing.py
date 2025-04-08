"""

"""
from __future__ import annotations

from behringer_mixer.client import OSCClient
from behringer_mixer.component import MixingConsole, Component
from behringer_mixer.exceptions import BehringerMixerException
from behringer_mixer.types import dB

from .status import Status
from .general_configuration import GeneralConfiguration
from .system_settings import SystemConfiguration
from .io import IO
from .input import Channel, Aux
from .output import Bus, Main, Matrix
from .channel_group import DCA, MuteGroup
from .fx import FX
from .cards import Cards
from .usb import USB
from .control import Control


class WING(MixingConsole):
    """

    """
    _components = {
        "status": {
            "path": "/$stat",
            "class": Status
        },
        "general_configuration": {
            "path": "/cfg",
            "class": GeneralConfiguration
        },
        "system_configuration": {
            "path": "/$syscfg",
            "class": SystemConfiguration
        },
        "io": {
            "path": "/io",
            "class": IO
        },
        "channel": {
            "path": "/ch",
            "class": Channel,
            "count": 40,
            "aliases": [ "ch" ]
        },
        "aux": {
            "path": "/aux",
            "class": Aux,
            "count": 8
        },
        "bus": {
            "path": "/bus",
            "class": Bus,
            "count": 16,
            "aliases": [ "bus_send", "send" ]
        },
        "main": {
            "variants": {
                "fullsize": {
                    "path": "/main",
                    "class": Main,
                    "count": 4
                },
                "compact": {
                    "path": "/main",
                    "class": Main,
                    "count": 4
                },
                "rack": {
                    "path": "/main",
                    "class": Main,
                    "count": 8
                }
            },
            "aliases": [ "main_send" ]
        },
        "matrix": {
            "path": "/mtx",
            "class": Matrix,
            "count": 8,
            "aliases": [ "matrix_send", "mtx", "mtx_send", "mx", "mx_send" ]
        },
        "dca": {
            "path": "/dca",
            "class": DCA,
            "count": 16
        },
        "mute_group": {
            "path": "/mgrp",
            "class": MuteGroup,
            "count": 8,
            "aliases": [ "mutegroup", "mgrp" ]
        },
        "fx": {
            "path": "/fx",
            "class": FX,
            "count": 16
        },
        "cards": {
            "path": "/cards",
            "class": Cards
        },
        "usb": {
            "path": "",
            "class": USB
        },
        "control": {
            "path": "/$ctl",
            "class": Control,
            "aliases": [ "ctl", "ctrl" ]
        }
    }

    _endpoints = {}

    def __init__(self, client: Client, variant: str = "fullsize"):
        """

        """
        super().__init__(client=client, variant=variant)

    @classmethod
    def _get_client(
            cls, host: str | IPAddress, client: Type[Client] = OSCClient, **kwargs
    ) -> Client:
        """

        :param host:
        :param client:
        :param kwargs:
        :return:
        """
        match client:
            case client if client == OSCClient:
                args_dict = {
                    "mixer_host": host,
                    "mixer_port": 2223
                }
                if "inter_message_delay" in kwargs:
                    args_dict.update({ "inter_message_delay": kwargs["inter_message_delay"] })
                if "query_response_timeout" in kwargs:
                    args_dict.update({ "query_response_timeout": kwargs["query_response_timeout"] })
                return OSCClient(**args_dict)
            case _:  # Foreshadowing: WING Binary Interface using TCP... ;)
                raise BehringerMixerException(
                    f"There is currently no implementation for client '{client.__name__}' "
                    f"for the WING console."
                )

    @classmethod
    def create(
            cls, host: str | IPAddress, client: Type[Client] = OSCClient, variant: str = "fullsize",
            **kwargs
    ) -> WING:
        """

        :param host:
        :param client:
        :param variant:
        :param kwargs:
        :return:
        """
        client = cls._get_client(host=host, client=client, **kwargs)
        return cls(client=client, variant=variant)
