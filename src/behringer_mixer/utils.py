"""

"""
_colors = [
    "OFF",
    "RD",
    "GN",
    "YE",
    "BL",
    "MG",
    "CY",
    "WH",
    "OFFi",
    "RDi",
    "GNi",
    "YEi",
    "BLi",
    "MGi",
    "CYi",
    "WHi",
]


def color_name_to_index(color_name: str, config) -> int:
    """Convert color name to color index"""
    return _colors.index(color_name)


def color_index_to_name(color_index: int, config) -> str:
    """Convert color index to color name"""
    return _colors[color_index]


def linf_to_db(value, config):
    """Convert linear fader value to dB"""
    max = 0
    min = 0
    if config and config.get("data_type_config"):
        min = config["data_type_config"].get("min")
        max = config["data_type_config"].get("max")
    return min + (max - min) * value


def db_to_linf(value, config):
    """Convert dB to linear fader value"""
    max = 0
    min = 0
    if config and config.get("data_type_config"):
        min = config["data_type_config"].get("min")
        max = config["data_type_config"].get("max")
    return (value - min) / (max - min)
