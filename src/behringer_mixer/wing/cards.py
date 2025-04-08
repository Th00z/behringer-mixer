"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint


class WLiveCardControl(Component):
    """

    """
    _components = {}

    _endpoints = {
        "control": {
            "path": "/control",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "STOP", "PAUSE", "PLAY", "REC" ]
        },
        "open_session": {
            "path": "/opensession",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "opensessikon" ]
        },
        "edit_marker": {
            "path": "/editmarker",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "editmarker" ]
        },
        "goto_marker": {
            "path": "/gotomarker",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 101,
            "aliases": [ "gotomarker" ]
        },
        "delete_marker": {
            "path": "/deletemarker",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "deletemarker" ]
        },
        "delete_session": {
            "path": "/deletesession",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "deletesession" ]
        },
        "stime": {
            "path": "/stime",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 36000000.0
        },
        "name_session": {
            "path": "/namesession",
            "class": endpoint.StringEndpoint,
            "max_chars": 19,
            "aliases": [ "namesession", "session_name" ]
        },
        "set_marker": {
            "path": "/setmarker",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "setmarker" ]
        },
        "format_sd_card": {
            "path": "/formatsdcard",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "formatsdcard" ]
        }
    }


class WLiveCardConfig(Component):
    """

    """
    _components = {}

    _endpoints = {
        "rec_tracks": {
            "path": "/rectracks",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "32": 32,
                "16": 16,
                "8": 8
            },
            "aliases": [ "rectracks", "recording_tracks" ]
        },
        "play_mode": {
            "path": "/playmode",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "PLAY", "A->B", "LOOP" ],
            "aliases": [ "playmode" ]
        }
    }


class WLiveCardSDStatus(Component):
    """

    """
    _components = {}

    _endpoints = {
        "free_space": {
            "path": "free",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 36000000.0,
            "aliases": [ "sdfree", "free" ]
        },
        "size": {
            "path": "size",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 1024,
            "aliases": [ "sdsize" ]
        },
        "state": {
            "path": "state",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "NONE", "READY", "PROTECT", "ERASE", "ERROR" ],
            "aliases": [ "sdstate" ]
        }
    }


class WLiveCardError(Component):
    """

    """
    _components = {}

    _endpoints = {
        "message": {
            "path": "message",
            "class": endpoint.StringEndpoint,
            "max_chars": 32,
            "aliases": [ "errormessage" ]
        },
        "code": {
            "path": "code",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 34,
            "aliases": [ "errorcode" ]
        }
    }


class WLiveCardStatus(Component):
    """

    """
    _components = {
        "sd": {
            "path": "/sd",
            "class": WLiveCardSDStatus,
            "aliases": [ "sd_card" ]
        },
        "error": {
            "path": "/error",
            "class": WLiveCardError
        }
    }

    _endpoints = {
        "state": {
            "path": "/state",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "STOP", "PAUSE", "PLAY", "REC" ],
            "read_only": True
        },
        "current_time": {
            "path": "/etime",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 36000000.0,
            "aliases": [ "etime", "e_time" ]
        },
        "session_list": {
            "path": "/sessionlist",
            "class": endpoint.StringEndpoint,
            "aliases": [ "sessionlist" ]
        },
        "marker_list": {
            "path": "/markerlist",
            "class": endpoint.StringEndpoint,
            "aliases": [ "markerlist", "current_marker_time" ]
        },
        "session_name_list": {
            "path": "/snamelist",
            "class": endpoint.StringEndpoint,
            "aliases": [ "snamelist", "s_name_list", "session_names_list" ]
        },
        "sessions": {
            "path": "/sessions",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "read_only": True,
            "aliases": [ "total_sessions" ]
        },
        "markers": {
            "path": "/markers",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "read_only": True,
            "aliases": [ "total_markers" ]
        },
        "session_length": {
            "path": "/sessionlen",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 36000000.0,
            "read_only": True,
            "aliases": [ "sessionlen", "session_len" ]
        },
        "session_position": {
            "path": "/sessionpos",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "sessionpos", "session_pos" ]
        },
        "marker_position": {
            "path": "/markerpos",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "markerpos", "marker_pos" ]
        },
        "track_number": {
            "path": "/tracks",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "32": 32,
                "16": 16,
                "8": 8
            },
            "aliases": [ "tracks", "track_number_in_current_session" ]
        },
        "sample_rate": {
            "path": "/rate",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "44.1": 44100,
                "48": 48000
            },
            "read_only": True,
            "aliases": [ "rate" ]
        },
        "linked_session_position": {
            "path": "/linkedpos",
            "class": endpoint.IntEndpoint,
            "min": 0,
            "max": 100,
            "aliases": [ "linkedpos", "linked_pos", "linked_position", "session_link_position" ]
        },
        "start": {
            "path": "/start",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 36000000.0
        },
        "stop": {
            "path": "/stop",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 36000000.0
        }
    }


class WLiveCard(Component):
    """

    """
    _components = {
        "control": {
            "path": "/$ctl",
            "class": WLiveCardControl,
            "aliases": [ "ctl" ]
        },
        "config": {
            "path": "/cfg",
            "class": WLiveCardConfig,
            "aliases": [ "cfg" ]
        },
        "status": {
            "path": "/$stat",
            "class": WLiveCardStatus,
            "aliases": [ "stat" ]
        }
    }

    _endpoints = {}


class WLive(Component):
    """

    """
    _cards = {}

    def __getitem__(self, key: int) -> WLiveCard:
        """

        :param item:
        :return:
        """
        if not isinstance(key, int):
            raise TypeError("Card Key must be of type integer!")
        if key not in [1, 2]:
            raise IndexError("Card Key must be either 1 or 2!")
        if key not in self._cards:
            self._cards.update({
                key: WLiveCard(
                    client=self._client, path=self._path, variant=self._variant, index=key
                )
            })
        return self._cards[key]

    _components = {}

    _endpoints = {
        "sd_link": {
            "path": "/sdlink",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "IND": "INDIPENDENT",
                "PAR": "PARALLEL"
            },
            "aliases": [ "sd_parallel_mode" ]
        },
        "act_link": {
            "path": "/$actlink",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "IND": "INDIPENDENT",
                "PAR": "PARALLEL"
            },
            "read_only": True,
            "aliases": [ "actlink" ]
        },
        "battery_status": {
            "path": "/$battstate",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "NONE", "GOOD", "LOW" ],
            "read_only": True,
            "aliases": [ "battstate" ]
        },
        "auto_input": {
            "path": "/autoin",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "OFF", "1", "2" ],
            "aliases": [ "autoin" ]
        },
        "show_meters": {
            "path": "/meters",
            "class": endpoint.BoolEndpoint,
            "aliases": [ "meters" ]
        },
        "auto_stop": {
            "path": "/auto_stop",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "KEEP", "MAIN", "ALT" ],
            "aliases": [ "settings_when_stop" ]
        },
        "auto_play": {
            "path": "/auto_play",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "KEEP", "MAIN", "ALT" ],
            "aliases": [ "settings_when_play" ]
        },
        "auto_record": {
            "path": "/auto_rec",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "KEEP", "MAIN", "ALT" ],
            "aliases": [ "auto_rec", "settings_when_rec", "settings_when_record" ]
        }
    }


class Cards(Component):
    """

    """
    _components = {
        "w_live": {
            "path": "/wlive",
            "class": WLive,
            "aliases": [ "wlive" ]
        }
    }

    _endpoints = {
        "type": {
            "path": "/$type",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "NONE", "WLIVE", "WDANTE", "WLINK" ],
            "read_only": True
        },
        "version": {
            "path": "/$ver",
            "class": endpoint.StringEndpoint,
            "max_chars": 32,
            "read_only": True,
            "aliases": [ "ver" ]
        }
    }
