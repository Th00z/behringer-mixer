"""

"""
from behringer_mixer.component import Component
from behringer_mixer.wing import endpoint
from behringer_mixer.wing.component import ConcretePlugin


class MainSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 20.0,
            "aliases":  [ "dcy" ]
        },
        "lo_dcy": {
            "path": "/ldcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 2.5,
            "aliases": [ "ldcy", "lo_decay", "low_decay" ]
        },
        "lomid_dcy": {
            "path": "/lmdcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 2.5,
            "aliases": [ "lmdcy", "lomid_decay", "low_mid_decay" ]
        },
        "himid_dcy": {
            "path": "/hmdcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 2.5,
            "aliases": [ "hmdcy", "himid_decay", "high_mid_decay" ]
        },
        "hi_dcy": {
            "path": "/hdcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 2.5,
            "aliases": [ "hdcy", "hi_decay", "high_decay" ]
        },
        "hi_soft": {
            "path": "/hsoft",
            "class": endpoint.FloatEndpoint,
            "min": -50.0,
            "max": 50.0,
            "aliases": [ "hsoft", "high_soft" ]
        },
        "lo_xo": {
            "path": "/lxo",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 500.0,
            "aliases": [
                "lxo", "lo_xover", "lo_crossover", "low_xover", "low_crossover"
            ]
        },
        "mid_xo": {
            "path": "/mxo",
            "class": endpoint.FloatEndpoint,
            "min": 200.0,
            "max": 2000.0,
            "aliases": [ "mxo", "mid_xover", "mid_crossover" ]
        },
        "hi_xo": {
            "path": "/hxo",
            "class": endpoint.FloatEndpoint,
            "min": 500.0,
            "max": 20000.0,
            "aliases": [
                "hxo", "hi_xover", "hi_crossover", "high_xover", "high_crossover"
            ]
        },
        "lo_shv": {
            "path": "/lshv",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 200.0,
            "aliases": [ "lshv", "lo_shelv", "low_shelv" ]
        },
        "lo_damp": {
            "path": "/lsdmp",
            "class": endpoint.FloatEndpoint,
            "min": -18.0,
            "max": 0.0,
            "aliases": [ "lsdmp", "lo_shv_damp", "low_damp", "low_shelv_damp" ]
        },
        "hi_cut": {
            "path": "/hcut",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 20000.0,
            "aliases": [ "hcut", "high_cut", "lp", "lo_pass", "low_pass" ]
        }
    }


class ERSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "pdly": {
            "path": "pdly",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 100.0,
            "aliases": [ "er_pdly", "erpdly", "pre_delay", "er_pre_delay" ]
        },
        "type":  {
            "path": "type",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [
                "ROYAL", "THEATRE", "CHURCH", "GAS", "CONCERT", "ROYAL2", "V1-NEAR", "V2-HARD",
                "V3-SPREAD", "V4-BUILD", "V5-RANDOM", "SLAP", "CAR", "PHONEBTH", "BATHROOM",
                "CONFRM9", "CONFRM30", "GARAGE", "SWIMSTDM", "AIRPORT", "STREET", "ALLEY", "PIAZA",
                "FOREST"
            ],
            "aliases": [ "er_type", "ertype" ]
        },
        "size": {
            "path": "size",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "SML": "SMALL",
                "MED": "MEDIUM",
                "LRG": "LARGE"
            },
            "aliases": [ "er_size", "ersize" ]
        },
        "pos": {
            "path": "pos",
            "class": endpoint.StringMappingEndpoint,
            "string_mapping": {
                "NEAR": "NEAR",
                "DIST": "DISTANT"
            },
            "aliases": [ "er_pos", "erpos", "position" ]
        },
        "bal": {
            "path": "bal",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "er_bal", "erbal", "balance" ]
        },
        "lcut": {
            "path": "lc",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 400.0,
            "aliases": [
                "er_lc", "erlc", "er_lcut", "lowcut", "low_cut", "hp", "highpass", "high_pass"
            ]
        },
        "col": {
            "path": "col",
            "class": endpoint.FloatEndpoint,
            "min": -40.0,
            "max": 40.0,
            "aliases": [ "er_col", "ercol", "er_color", "color" ]
        },
        "lvl": {
            "path": "lvl",
            "class": endpoint.FaderEndpoint,
            "aliases": [ "er_lvl", "erlvl", "er_level", "level" ]
        }
    }


class TailSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "type": {
            "path": "type",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "SMOOTH", "NATURAL", "ALIVE", "FAST", "X-WIDE", "ALIVE2" ],
            "aliases": [ "tail_type", "rev_type", "rv_type", "rvtype" ]
        },
        "wid": {
            "path": "wid",  # Documentation states "/rvwide", but it's "rvwid"!
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "NARROW", "NORMAL", "WIDE", "X-WIDE" ],
            "aliases": [
                "wide", "width", "tail_wid", "tail_wide", "tail_width", "rev_wid", "rev_wide",
                "rev_width", "rv_wid", "rv_wide", "rv_width", "rvwid"
            ]
        },
        "pdly": {
            "path": "pdly",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 200.0,
            "aliases": [
                "pre_delay", "tail_pdly", "tail_pre_delay", "rev_pdly", "rev_pre_delay", "rv_pdly",
                "rv_pre_delay", "rvpdly"
            ]
        },
    }


class ModSection(Component):
    """

    """
    _components = {}

    _endpoints = {
        "type": {
            "path": "type",
            "class": endpoint.StringEnumEndpoint,
            "valid_strings": [ "A", "B", "C", "D", "E", "F" ],
            "aliases": [ "mtype", "mod_type" ]
        },
        "rate": {
            "path": "rate",
            "class": endpoint.FloatEndpoint,
            "min": -100.0,
            "max": 100.0,
            "aliases": [ "mrate", "mod_rate" ]
        },
        "wid": {
            "path": "wid",
            "class": endpoint.FloatEndpoint,
            "min": 0.0,
            "max": 200.0,
            "aliases": [ "mwid", "mod_wid", "width", "mod_width" ]
        }
    }


class VSS3Reverb(ConcretePlugin):
    """

    """
    @staticmethod
    def model_key() -> str:
        return "VSS3"

    @staticmethod
    def model_name() -> str:
        return "VSS3 Reverb"

    _components = {
        "main": {
            "path": "",
            "class": MainSection
        },
        "er": {
            "path": "/er",
            "class": ERSection
        },
        "tail": {
            "path": "/rv",
            "class": TailSection,
            "aliases": [ "rv", "rev" ]
        },
        "mod": {
            "path": "/m",
            "class": ModSection,
            "aliases": [ "modulation" ]
        }
    }

    _endpoints = {
        "preset": {
            "path": "/preset",
            "class": endpoint.StringMappingEndpoint,
            # Adding a mapping here to provide some shorthands and whitespace-less variants
            # for more convenience :)
            "string_mapping": {
                "Build": [ "Build", "BUILD" ],
                "Small Booth": [ "Small Booth", "SMALLBOOTH" ],
                "Home Room": [ "Home Room", "HOMEROOM" ],
                "Dialog Alley": [ "Dialog Alley", "DIALOGALLEY" ],
                "Small Wood Room": [ "Small Wood Room", "SMALLWOODROOM" ],
                "A Small Room": [ "A Small Room", "ASMALLMROOM" ],
                "Tight & Natural": [ "Tight & Natural", "TIGHTNATURAL" ],
                "Room Conversation": [ "Room Conversation", "ROOMCONVERSATION", "ROOMCONV" ],
                "Furnished Room 2": [ "Furnished Room 2", "FURNISHEDROOM2" ],
                "Studio 20x20 ft": [ "Studio 20x20 ft", "STUDIO20X20FT", "STUDIO20X20", "S20X20" ],
                "Drew Room": [ "Drew Room", "DREWROOM" ],
                "Piano Close": [ "Piano Close", "PIANOCLOSE" ],
                "Clear Guitar Room": [ "Clear Guitar Room", "CLEARGUITARROOM", "CLEARGITROOM" ],
                "Wide Ambient Chamber": [
                    "Wide Ambient Chamber", "WIDEAMBIENTCHAMBER", "WHITEAMBCHAMB"
                ],
                "Small Dense Hall": [ "Small Dense Hall", "SMALLDENSEHALL" ],
                "Slap Hall": [ "Slap Hall", "SLAPHALL" ],
                "Acoustic Gtr Ambience": [
                    "Acoustic Gtr Ambience", "ACOUSTICGTRAMBIENCE", "ACCGITAMB"
                ],
                "Clear Room": [ "Clear Room", "CLEARROOM" ],
                "Livingroom": [ "Livingroom", "LIVINGROOM" ],
                "Band Rehearsal Room": [ "Band Rehearsal Room", "BANDREHEARSALROOM", "BANDREROOM" ],
                "The Studio": [ "The Studio", "THESTUDIO" ],
                "In The Room": [ "In The Room", "INTHEROOM" ],
                "Studio 40x40 ft": [ "Studio 40x40 ft", "STUDIO40X40FT", "STUDIO40X40", "S40X40" ],
                "Hit Room": [ "Hit Room", "HITROOM" ],
                "Ambient Hall": [ "Ambient Hall", "AMBIENTHALL" ],
                "Stage and Hall": [ "Stage and Hall", "STAGEANDHALL" ],
                "Acoustic Guitar Space": [
                    "Acoustic Guitar Space", "ACOUSTICGUITARSPACE", "ACCGITSPACE"
                ],
                "Medium Vocal Hall": [ "Medium Vocal Hall", "MEDIUMVOCALHALL" ],
                "Bright Theatre": [ "Bright Theatre", "BRIGHTTHEATRE" ],
                "Big Empty Club": [ "Big Empty Club", "BIGEMPTYCLUB" ],
                "Venue Warm 1": [ "Venue Warm 1", "VENUEWARM1" ],
                "Concert 1": [ "Concert 1", "CONCERT1" ],
                "Bright Guitar Hall": [ "Bright Guitar Hall", "BRIGHTGUITARHALL", "BRIGHTGITHALL" ],
                "Concert Arena": [ "Concert Arena", "CONCERTARENA" ],
                "Concert Piano": [ "Concert Piano", "CONCERTPIANO" ],
                "Piano Hall 1st Row": [ "Piano Hall 1st Row", "PIANOHALL1STROW" ],
                "Empty Arena": [ "Empty Arena", "EMPTYARENA" ],
                "Ballad Vocal Hall": [ "Ballad Vocal Hall", "BALLADVOCALHALL" ],
                "Grand Vocal Hall": [ "Grand Vocal Hall", "GRANDVOCALHALL" ],
                "Large Warm Hall": [ "Large Warm Hall", "LARGEWARMHALL" ],
                "Back There": [ "Back There", "BACKTHERE" ],
                "WoodHall": [ "WoodHall", "WOODHALL" ],
                "Church": [ "Church", "CHURCH" ],
                "Warm Cathedral": [ "Warm Cathedral", "WARMCATHEDRAL" ],
                "Cologne Cathedral": [ "Cologne Cathedral", "COLOGNECATHEDRAL" ],
                "Drum Plate Stuff": [ "Drum Plate Stuff", "DRUMPLATESTUFF", "DRMPLATESTUFF" ],
                "Drum Wood Plate": [ "Drum Wood Plate", "DRUMWOODPLATE" ],
                "Piano Plate": [ "Piano Plate", "PIANOPLATE" ],
                "Stairway Plate": [ "Stairway Plate", "STAIRWAYPLATE" ],
                "Slapback Plate": [ "Slapback Plate", "SLAPBACKPLATE" ],
                "Ambient Plate": [ "Ambient Plate", "AMBIENTPLATE" ],
                "Silky Gold Plate": [ "Silky Gold Plate", "SILKYGOLDPLATE" ],
                "Gold Plate": [ "Gold Plate", "GOLDPLATE" ],
                "EMT 141": [ "EMT 141", "EMT141" ],
                "Leader Of The Band": [ "Leader Of The Band", "LEADEROFTHEBAND" ],
                "VocalDry": [ "VocalDry", "VOCALDRY" ],
                "Vocal Room": [ "Vocal Room", "VOCALROOM" ],
                "VocalWet": [ "VocalWet", "VOCALWET" ],
                "Slapback Vox 1": [ "Slapback Vox 1", "SLAPBACKVOX1" ],
                "Vocal Hall 1":  [ "Vocal Hall 1", "VOCALHALL1" ],
                "Vocal Chamber": [ "Vocal Chamber", "VOCALCHAMBER" ],
                "Bright Male Vox": [ "Bright Male Vox", "BRIGHTMALEVOX" ],
                "Vocal Bright": [ "Vocal Bright", "VOCALBRIGHT" ],
                "Vocal Deep": [ "Vocal Deep", "VOCALDEEP" ],
                "Vocal Female": [ "Vocal Female", "VOCALFEMALE" ],
                "Vocal Deep Male": [ "Vocal Deep Male", "VOCALDEEPMALE" ],
                "Large Vocal Hall": [ "Large Vocal Hall", "LARGEVOCALHALL" ],
                "Kick & Bass": [ "Kick & Bass", "KICKBASS" ],
                "Ambience": [ "Ambience", "AMBIENCE" ],
                "Drum Room": [ "Drum Room", "DRUMROOM" ],
                "Small Perc Room": [ "Small Perc Room", "SMALLPERCROOM" ],
                "Drum Room Xpander": [ "Drum Room Xpander", "DRUMROOMXPANDER" ],
                "Bright Shoe Gaze Snare": [ "Bright Shoe Gaze Snare", "BRIGHTSHOEGAZESNARE" ],
                "Snare Room Bright": [ "Snare Room Bright", "SNAREROOMBRIGHT" ],
                "Tom-Tom Reverb": [ "Tom-Tom Reverb", "TOMTOMREVERB" ],
                "Bossa Nova Perc Room": [ "Bossa Nova Perc Room", "BOSSANOVAPERCROOM" ],
                "Hard Drum Space": [ "Hard Drum Space", "HARDDRUMSPACE" ],
                "Puk Drum Ambience": [ "Puk Drum Ambience", "PUKDRUMAMBIENCE" ],
                "Overhead Mics": [ "Overhead Mics", "OVERHEADMICS" ],
                "Dance Snare": [ "Dance Snare", "DANCESNARE" ],
                "Drum Perc Soft 1": [ "Drum Perc Soft 1", "DRUMPERCSOFT1" ],
                "Perc Straight Tail": [ "Perc Straight Tail", "PERCSTRAIGHTTAIL" ],
                "Store Room": [ "Store Room", "STOREROOM" ],
                "Studio Small": [ "Studio Small", "STUDIOSMALL" ],
                "The Alley": [ "The Alley", "THEALLEY" ],
                "Near The Wall": [ "Near The Wall", "NEARTHEWALL" ],
                "WoodFlr": [ "WoodFlr", "WOODFLR" ],
                "Large Office": [ "Large Office", "LARGEOFFICE" ],
                "Conference Room": [ "Conference Room", "CONFERENCEROOM" ],
                "Dance Studio": [ "Dance Studio", "DANCESTUDIO" ],
                "Forest 2": [ "Forest 2", "FOREST2" ],
                "StoneWall": [ "StoneWall", "STONEWALL" ],
                "Venue 1": [ "Venue 1", "VENUE1" ],
                "Small Stairway": [ "Small Stairway", "SMALLSTAIRWAY" ],
                "Forest 1":  [ "Forest 1", "FOREST1" ],
                "Airport PA": [ "Airport PA", "AIRPORTPA" ],
                "Small Tower Hall": [ "Small Tower Hall", "SMALLTOWERHALL" ],
                "On The Street": [ "On The Street", "ONTHESTREET" ],
                "Dark Tunnel": [ "Dark Tunnel", "DARKTUNNEL" ],
                "Empty Nightclub": [ "Empty Nightclub", "EMPTYNIGHTCLUB" ],
                "Parking Garage": [ "Parking Garage", "PARKINGGARAGE" ],
                "Parking Distant": [ "Parking Distant", "PARKINGDISTANT" ],
                "Long Swimmingpool": [ "Long Swimmingpool", "LONGSWIMMINGPOOL" ]
            }
        },
        "load": {
            "path": "/load",
            "class": endpoint.BoolEndpoint
        },
        "decay": {
            "path": "/dcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 20.0,
            "aliases":  [ "dcy" ]
        },
        "lo_damp": {
            "path": "/lsdmp",
            "class": endpoint.FloatEndpoint,
            "min": -18.0,
            "max": 0.0,
            "aliases": [ "lsdmp", "lo_shv_damp", "low_damp", "low_shelv_damp" ]
        },
        "hi_dcy": {
            "path": "/hdcy",
            "class": endpoint.FloatEndpoint,
            "min": 0.1,
            "max": 2.5,
            "aliases": [ "hdcy", "hi_decay", "high_decay" ]
        },
        "hi_cut": {
            "path": "/hcut",
            "class": endpoint.FloatEndpoint,
            "min": 20.0,
            "max": 20000.0,
            "aliases": [ "hcut", "high_cut", "lp", "lo_pass", "low_pass" ]
        },
        "rev_lvl": {
            "path": "/rvlvl",
            "class": endpoint.FaderEndpoint,
            "aliases": [ "rvlvl", "rev_level" ]
        },
        "er_lvl": {
            "path": "/erlvl",
            "class": endpoint.FaderEndpoint,
            "aliases": [ "erlvl", "er_level" ]
        },
        "view": {
            "path": "/view",
            "class": endpoint.BoolEndpoint
        }
    }
