"""

"""
import re

from behringer_mixer.component import Component
from behringer_mixer.exceptions import QueryException

from behringer_mixer.wing import endpoint


class SongListEndpoint(endpoint.StringEndpoint):
    """

    """
    _raw_query = b"/play\x00\x00\x00,s\x00\x00\x3F\x00\x00\x00"

    __song_list_regex = re.compile(r"\$songs\s*list\s\[(?P<songlist>.*?)\]")

    @property
    def read_only(self) -> bool:
        return True

    @property
    def allow_bulk_queries(self) -> bool:
        """

        :return:
        """
        return False

    async def get(self):
        """

        :return:
        """
        response = await self._client.raw_query(message=self._raw_query)
        return self._parse_response(response=response)

    def _parse_response(self, response) -> list:
        """

        :param response:
        :return:
        """
        response = super()._parse_response(response=response)
        response_match = self.__song_list_regex.search(response)
        if not response_match:
            raise QueryException(f"Invalid Response for Song List Query: '{response}'")
        return [ song.strip() for song in response_match["songlist"].split(",") ]


class USBPlayerSong(Component):
    """

    """
    _components = {}

    _endpoints = {
        "name": {
            "path": "/$song",
            "class": endpoint.StringEndpoint,
            "max_chars": 64,
            "read_only": True,
            "aliases": [ "song" ]
        },
        "album": {
            "path": "/$album",
            "class": endpoint.StringEndpoint,
            "max_chars": 64,
            "read_only": True
        },
        "artist": {
            "path": "/$artist",
            "class": endpoint.StringEndpoint,
            "max_chars": 64,
            "read_only": True
        },
        "position": {
            "path": "/$pos",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 35999.0,
            "aliases": [ "pos" ]
        },
        "duration": {
            "path": "/$total",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 35999.0,
            "read_only": True,
            "aliases": [ "total", "total_time" ]
        }
    }


class USBPlayer(Component):
    """

    """
    _components = {
        "song": {
            "path": "",
            "class": USBPlayerSong
        }
    }

    _endpoints = {
        "songs": {
            "path": "/$songs",
            "class": SongListEndpoint,
            "read_only": True
        },
        "active_path": {
            "path": "/$actlist",
            "class": endpoint.StringEndpoint,
            "max_chars": 256,
            "read_only": True,
            "aliases": [ "actlist", "path_to_usb_files" ]
        },
        "active_entry": {
            "path": "/$actidx",
            "class": endpoint.IntEndpoint,
            "aliases": [ "actidx", "active_index", "current_active_entry_in_the_playlist" ]
        },
        "action_index": {
            "path": "/$actionidx",
            "class": endpoint.IntEndpoint,
            "read_only": True,
            "aliases": [ "actionidx" ]
        },
        "play_file": {
            "path": "/$playfile",
            "class": endpoint.StringEndpoint,
            "max_chars": 256,
            "aliases": [ "playfile" ]
        },
        "action": {
            "path": "/$action",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "IDLE", "STOP", "PLAY", "PAUSE", "NEXT", "PREV", "PLAYFILE" ]
        },
        "active_state": {
            "path": "/$actstate",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "STOP", "PLAY", "PAUSE", "ERROR" ],
            "read_only": True,
            "aliases": [ "actstate", "act_state" ]
        },
        "active_file": {
            "path": "/$actfile",
            "class": endpoint.StringEndpoint,
            "max_chars": 256,
            "read_only": True,
            "aliases": [ "actfile", "act_file" ]
        },
        "resolution": {
            "path": "/$resolution",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "16": 16,
                "24": 24
            },
            "read_only": True
        },
        "channels": {
            "path": "/$channels",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4
            },
            "read_only": True
        },
        "rate": {
            "path": "/$rate",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "44.1": 44100,
                "48": 48000
            },
            "read_only": True,
            "aliases": [ "sample_rate" ]
        },
        "file_format": {
            "path": "/$format",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "WAV", "MP3", "FLAC" ],
            "read_only": True,
            "aliases": [ "format" ]
        },
        "repeat": {
            "path": "/repeat",
            "class": endpoint.BoolEndpoint
        }
    }


class USBRecorder(Component):
    """

    """
    _components = {}

    _endpoints = {
        "active_state": {
            "path": "/$actstate",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "STOP", "REC", "PAUSE", "ERROR" ],
            "aliases": [ "actstate", "act_state" ]
        },
        "active_filename": {
            "path": "/$actfile",
            "class": endpoint.StringEndpoint,
            "aliases": [ "actfile", "act_file", "active_file" ]
        },
        "action": {
            "path": "/$action",
            "class": endpoint.StringEnumEndpoint,
            # Option 'IDLE' is not documented but yielded by the console!
            "valid_strings": [ "IDLE", "STOP", "REC", "PAUSE", "NEWFILE" ]
        },
        "path": {
            "path": "/$path", # Documentation states it's "/path" but it actually needs the $
            "class": endpoint.StringEndpoint,
            "aliases": [ "filename_path" ]
        },
        "resolution": {
            "path": "/resolution",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "16": 16,
                "24": 24
            },
        },
        "channels": {
            "path": "/channels",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4
            }
        },
        "time": {
            "path": "/$time",
            "class": endpoint.FloatEndpoint
        }
    }


class USB(Component):
    """

    """
    _components = {
        "player": {
            "path": "/play",
            "class": USBPlayer,
            "aliases": [ "play" ]
        },
        "recorder": {
            "path": "/rec",
            "class": USBRecorder,
            "aliases": [ "rec" ]
        }
    }

    _endpoints = {}
