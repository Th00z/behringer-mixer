"""

"""
from __future__ import annotations

from abc import ABC, abstractmethod


class dB(float):
    """

    """
    def __repr__(self):
        """

        :return:
        """
        return f"dB({float(self)})"

    def to_fader(self) -> float:
        """

        :return:
        """
        value = float(self)
        if value >= 10.0:
            return 1.0
        elif value >= -10.0:
            return (value + 30) / 40.0
        elif value >= -30.0:
            return (value + 50) / 80.0
        elif value >= -60.0:
            return (value + 70) / 160.0
        elif value >= -90.0:
            return (value + 90) / 480.0
        return 0.0

    @classmethod
    def from_fader(cls, value: float) -> dB:
        """

        :param value:
        :return:
        """
        if value >= 1:
            return dB(10.0)
        elif value >= 0.5:
            return dB(round((40 * value) - 30, 2))
        elif value >= 0.25:
            return dB(round((80 * value) - 50, 2))
        elif value >= 0.0625:
            return dB(round((160 * value) - 70, 2))
        elif value >= 0:
            return dB(round((480 * value) - 90, 2))
        else:
            return db(-90.0)


class DelayUnit(float):
    """

    """
    @property
    @abstractmethod
    def unit(self) -> str:
        """

        :return:
        """

    def __repr__(self):
        """

        :return:
        """
        return f"{float(self)}{self.unit}"


class Meters(DelayUnit):
    """

    """
    unit = "m"


class Feet(DelayUnit):
    """

    """
    unit = "ft"


class Milliseconds(DelayUnit):
    """

    """
    unit = "ms"


class Samples(DelayUnit):
    """

    """
    unit = "smp"
