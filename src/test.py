import asyncio

from dataclasses import dataclass

from behringer_mixer import OSCClient, WING
from behringer_mixer.types import dB, Meters, Feet, Milliseconds, Samples

from pprint import pprint


class Multi:
    """

    """
    def __init__(self):
        """

        """

    @staticmethod
    async def wave(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :param sleep:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.sust:")
        pprint(await plugin.sust.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.sustain:")
        pprint(await plugin.sustain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.output_gain:")
        pprint(await plugin.output_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.g:")
        pprint(await plugin.g.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def la76(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.input:")
        pprint(await plugin.input.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.output:")
        pprint(await plugin.output.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.out:")
        pprint(await plugin.out.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def la(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.power:")
        pprint(await plugin.power.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ingain:")
        pprint(await plugin.ingain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak_reduction:")
        pprint(await plugin.peak_reduction.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak:")
        pprint(await plugin.peak.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limit:")
        pprint(await plugin.limit.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress:")
        pprint(await plugin.compress.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def ride(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.target:")
        pprint(await plugin.target.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tgt:")
        pprint(await plugin.tgt.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.speed:")
        pprint(await plugin.speed.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.spd:")
        pprint(await plugin.spd.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hold:")
        pprint(await plugin.hold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hld:")
        pprint(await plugin.hld.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.range:")
        pprint(await plugin.range.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def pse(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.depth:")
        pprint(await plugin.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.fast:")
        pprint(await plugin.fast.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak:")
        pprint(await plugin.peak.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def cmb(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.depth:")
        pprint(await plugin.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.fast:")
        pprint(await plugin.fast.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak:")
        pprint(await plugin.peak.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ingain:")
        pprint(await plugin.ingain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak_reduction:")
        pprint(await plugin.peak_reduction.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)


class Filter:
    """

    """
    def __init__(self):
        """

        """

    @staticmethod
    async def tilt(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.tilt:")
        pprint(await plugin.tilt.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def max(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.low_contour:")
        pprint(await plugin.low_contour.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low:")
        pprint(await plugin.low.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_process:")
        pprint(await plugin.high_process.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.proc:")
        pprint(await plugin.proc.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def ap1(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.frequency:")
        pprint(await plugin.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.freq:")
        pprint(await plugin.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.f:")
        pprint(await plugin.f.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def ap2(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.frequency:")
        pprint(await plugin.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.f:")
        pprint(await plugin.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.q:")
        pprint(await plugin.q.get())
        await asyncio.sleep(sleep)


class Gate:
    """

    """
    def __init__(self):
        """

        """

    @staticmethod
    async def gate(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.range:")
        pprint(await plugin.range.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hold:")
        pprint(await plugin.hold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hld:")
        pprint(await plugin.hld.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.accent:")
        pprint(await plugin.accent.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.acc:")
        pprint(await plugin.acc.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def duck(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.range:")
        pprint(await plugin.range.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hold:")
        pprint(await plugin.hold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hld:")
        pprint(await plugin.hld.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def e88(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hysteresis:")
        pprint(await plugin.hysteresis.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hyst:")
        pprint(await plugin.hyst.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.range:")
        pprint(await plugin.range.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.fast:")
        pprint(await plugin.fast.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attenuation:")
        pprint(await plugin.attenuation.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.m40:")
        pprint(await plugin.m40.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def g9000(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.range:")
        pprint(await plugin.range.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hold:")
        pprint(await plugin.hold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hld:")
        pprint(await plugin.hld.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.fast:")
        pprint(await plugin.fast.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.expand:")
        pprint(await plugin.expand.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def d241(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.bypass:")
        pprint(await plugin.bypass.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.slow:")
        pprint(await plugin.slow.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def ds902(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.solo:")
        pprint(await plugin.solo.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hf_only:")
        pprint(await plugin.hf_only.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.frequency:")
        pprint(await plugin.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.freq:")
        pprint(await plugin.freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.f:")
        pprint(await plugin.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.range:")
        pprint(await plugin.range.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def deq(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter_types:")
        pprint(await plugin.filter_types.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filt:")
        pprint(await plugin.filt.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.g:")
        pprint(await plugin.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.freq:")
        pprint(await plugin.freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.f:")
        pprint(await plugin.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.frequency:")
        pprint(await plugin.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.q:")
        pprint(await plugin.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.above:")
        pprint(await plugin.above.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.below:")
        pprint(await plugin.below.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def warm(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.drive:")
        pprint(await plugin.drive.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.drv:")
        pprint(await plugin.drv.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.harmonics:")
        pprint(await plugin.harmonics.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hrm:")
        pprint(await plugin.hrm.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.color:")
        pprint(await plugin.color.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.col:")
        pprint(await plugin.col.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.trim:")
        pprint(await plugin.trim.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)


class EQ:
    """

    """
    def __init__(self):
        """

        """

    @staticmethod
    async def std(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.l:")
        pprint(plugin.l)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low:")
        channel_std_eq_low = plugin.low
        pprint(channel_std_eq_low)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.gain:")
        pprint(await channel_std_eq_low.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.g:")
        pprint(await channel_std_eq_low.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.frequency:")
        pprint(await channel_std_eq_low.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.f:")
        pprint(await channel_std_eq_low.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.q:")
        pprint(await channel_std_eq_low.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.type:")
        pprint(await channel_std_eq_low.type.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.eq:")
        pprint(await channel_std_eq_low.eq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band:")
        channel_std_eq_band = plugin.band
        pprint(channel_std_eq_band)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1]:")
        pprint(channel_std_eq_band[1])
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1].gain:")
        pprint(await channel_std_eq_band[1].gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1].g:")
        pprint(await channel_std_eq_band[1].g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1].frequency:")
        pprint(await channel_std_eq_band[1].frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1].f:")
        pprint(await channel_std_eq_band[1].f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1].q:")
        pprint(await channel_std_eq_band[1].q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.h:")
        pprint(plugin.h)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high:")
        channel_std_eq_high = plugin.high
        pprint(channel_std_eq_high)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.gain:")
        pprint(await channel_std_eq_high.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.g:")
        pprint(await channel_std_eq_high.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.frequency:")
        pprint(await channel_std_eq_high.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.f:")
        pprint(await channel_std_eq_high.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.q:")
        pprint(await channel_std_eq_high.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.type:")
        pprint(await channel_std_eq_high.type.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.eq:")
        pprint(await channel_std_eq_high.eq.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def soul(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lf:")
        pprint(plugin.lf)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low:")
        channel_soul_eq_low = plugin.low
        pprint(channel_soul_eq_low)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.frequency:")
        pprint(await channel_soul_eq_low.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.f:")
        pprint(await channel_soul_eq_low.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.hz:")
        pprint(await channel_soul_eq_low.hz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.gain:")
        pprint(await channel_soul_eq_low.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.g:")
        pprint(await channel_soul_eq_low.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.db:")
        pprint(await channel_soul_eq_low.db.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lmf:")
        pprint(plugin.lmf)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid:")
        channel_soul_eq_low_mid = plugin.low_mid
        pprint(channel_soul_eq_low_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.frequency:")
        pprint(await channel_soul_eq_low_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.f:")
        pprint(await channel_soul_eq_low_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.khz:")
        pprint(await channel_soul_eq_low_mid.khz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.gain:")
        pprint(await channel_soul_eq_low_mid.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.g:")
        pprint(await channel_soul_eq_low_mid.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.db:")
        pprint(await channel_soul_eq_low_mid.db.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.q:")
        pprint(await channel_soul_eq_low_mid.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.by_3:")
        pprint(await channel_soul_eq_low_mid.by_3.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hmf:")
        pprint(plugin.hmf)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid:")
        channel_soul_eq_high_mid = plugin.high_mid
        pprint(channel_soul_eq_high_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.frequency:")
        pprint(await channel_soul_eq_high_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.f:")
        pprint(await channel_soul_eq_high_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.khz:")
        pprint(await channel_soul_eq_high_mid.khz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.gain:")
        pprint(await channel_soul_eq_high_mid.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.g:")
        pprint(await channel_soul_eq_high_mid.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.db:")
        pprint(await channel_soul_eq_high_mid.db.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.q:")
        pprint(await channel_soul_eq_high_mid.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.times_3:")
        pprint(await channel_soul_eq_high_mid.times_3.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hf:")
        pprint(plugin.hf)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high:")
        channel_soul_eq_high = plugin.high
        pprint(channel_soul_eq_high)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.frequency:")
        pprint(await channel_soul_eq_high.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.f:")
        pprint(await channel_soul_eq_high.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.khz:")
        pprint(await channel_soul_eq_high.khz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.gain:")
        pprint(await channel_soul_eq_high.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.g:")
        pprint(await channel_soul_eq_high.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.db:")
        pprint(await channel_soul_eq_high.db.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def e88(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.l:")
        pprint(plugin.l)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low:")
        channel_e88_eq_low = plugin.low
        pprint(channel_e88_eq_low)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.frequency:")
        pprint(await channel_e88_eq_low.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.f:")
        pprint(await channel_e88_eq_low.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.hz:")
        pprint(await channel_e88_eq_low.hz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.gain:")
        pprint(await channel_e88_eq_low.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.g:")
        pprint(await channel_e88_eq_low.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.db:")
        pprint(await channel_e88_eq_low.db.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.q:")
        pprint(await channel_e88_eq_low.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.type:")
        pprint(await channel_e88_eq_low.type.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.hi_q:")
        pprint(await channel_e88_eq_low.hi_q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lm:")
        pprint(plugin.lm)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid:")
        channel_e88_eq_low_mid = plugin.low_mid
        pprint(channel_e88_eq_low_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.frequency:")
        pprint(await channel_e88_eq_low_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.f:")
        pprint(await channel_e88_eq_low_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.hz:")
        pprint(await channel_e88_eq_low_mid.hz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.gain:")
        pprint(await channel_e88_eq_low_mid.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.g:")
        pprint(await channel_e88_eq_low_mid.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.db:")
        pprint(await channel_e88_eq_low_mid.db.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.q:")
        pprint(await channel_e88_eq_low_mid.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hm:")
        pprint(plugin.hm)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid:")
        channel_e88_eq_high_mid = plugin.high_mid
        pprint(channel_e88_eq_high_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.frequency:")
        pprint(await channel_e88_eq_high_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.f:")
        pprint(await channel_e88_eq_high_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.khz:")
        pprint(await channel_e88_eq_high_mid.khz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.gain:")
        pprint(await channel_e88_eq_high_mid.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.g:")
        pprint(await channel_e88_eq_high_mid.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.db")
        pprint(await channel_e88_eq_high_mid.db.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.q:")
        pprint(await channel_e88_eq_high_mid.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.h:")
        pprint(plugin.h)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high:")
        channel_e88_eq_high = plugin.high
        pprint(channel_e88_eq_high)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.frequency:")
        pprint(await channel_e88_eq_high.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.f:")
        pprint(await channel_e88_eq_high.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.khz:")
        pprint(await channel_e88_eq_high.khz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.gain:")
        pprint(await channel_e88_eq_high.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.g:")
        pprint(await channel_e88_eq_high.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.db:")
        pprint(await channel_e88_eq_high.db.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.q:")
        pprint(await channel_e88_eq_high.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.hi_q:")
        pprint(await channel_e88_eq_high.hi_q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.type:")
        pprint(await channel_e88_eq_high.type.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def e84(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.g:")
        pprint(await plugin.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.db:")
        pprint(await plugin.db.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.l:")
        pprint(plugin.l)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low:")
        channel_e84_eq_low = plugin.low
        pprint(channel_e84_eq_low)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.frequency:")
        pprint(await channel_e84_eq_low.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.f:")
        pprint(await channel_e84_eq_low.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.hz:")
        pprint(await channel_e84_eq_low.hz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.gain:")
        pprint(await channel_e84_eq_low.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.m:")
        pprint(plugin.m)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid:")
        channel_e84_eq_mid = plugin.mid
        pprint(channel_e84_eq_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.frequency:")
        pprint(await channel_e84_eq_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.f:")
        pprint(await channel_e84_eq_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.khz:")
        pprint(await channel_e84_eq_mid.khz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.q:")
        pprint(await channel_e84_eq_mid.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.hi_q:")
        pprint(await channel_e84_eq_mid.hi_q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.h:")
        pprint(plugin.h)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high:")
        channel_e84_eq_high = plugin.high
        pprint(channel_e84_eq_high)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.frequency:")
        pprint(await channel_e84_eq_high.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.f:")
        pprint(await channel_e84_eq_high.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.khz:")
        pprint(await channel_e84_eq_high.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.gain:")
        pprint(await channel_e84_eq_high.gain.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def f110(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.g:")
        pprint(await plugin.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peq_in:")
        pprint(await plugin.peq_in.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peq:")
        pprint(await plugin.peq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.sheq_in:")
        pprint(await plugin.sheq_in.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.shv:")
        pprint(await plugin.shv.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.l:")
        pprint(plugin.l)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_shelf:")
        channel_f110_eq_low_shelf = plugin.low_shelf
        pprint(channel_f110_eq_low_shelf)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_shelf.frequency:")
        pprint(await channel_f110_eq_low_shelf.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_shelf.f:")
        pprint(await channel_f110_eq_low_shelf.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_shelf.gain:")
        pprint(await channel_f110_eq_low_shelf.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_shelf.g:")
        pprint(await channel_f110_eq_low_shelf.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lm:")
        pprint(plugin.lm)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid:")
        channel_f110_eq_low_mid = plugin.low_mid
        pprint(channel_f110_eq_low_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.frequency:")
        pprint(await channel_f110_eq_low_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.f:")
        pprint(await channel_f110_eq_low_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.gain:")
        pprint(await channel_f110_eq_low_mid.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.g:")
        pprint(await channel_f110_eq_low_mid.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.q:")
        pprint(await channel_f110_eq_low_mid.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.by_3:")
        pprint(await channel_f110_eq_low_mid.by_3.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hm:")
        pprint(plugin.hm)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid:")
        channel_f110_eq_high_mid = plugin.high_mid
        pprint(channel_f110_eq_high_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.frequency:")
        pprint(await channel_f110_eq_high_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.f:")
        pprint(await channel_f110_eq_high_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.gain:")
        pprint(await channel_f110_eq_high_mid.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.g:")
        pprint(await channel_f110_eq_high_mid.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.q:")
        pprint(await channel_f110_eq_high_mid.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.times_3:")
        pprint(await channel_f110_eq_high_mid.times_3.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.h:")
        pprint(plugin.h)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_shelf:")
        channel_f110_eq_high_shelf = plugin.high_shelf
        pprint(channel_f110_eq_high_shelf)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_shelf.frequency:")
        pprint(await channel_f110_eq_high_shelf.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_shelf.f:")
        pprint(await channel_f110_eq_high_shelf.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_shelf.gain:")
        pprint(await channel_f110_eq_high_shelf.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_shelf.g:")
        pprint(await channel_f110_eq_high_shelf.g.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def pulsar(plugin, pathstr, sleep):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.hi_lo_eq1_in:")
        pprint(await plugin.hi_lo_eq1_in.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hi_lo_eq1:")
        pprint(await plugin.hi_lo_eq1.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.eq1:")
        pprint(await plugin.eq1.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid_eq5_in:")
        pprint(await plugin.mid_eq5_in.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid_eq5:")
        pprint(await plugin.mid_eq5.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.eq5:")
        pprint(await plugin.eq5.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.l1:")
        pprint(plugin.l1)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low:")
        channel_pulsar_eq_low = plugin.low
        pprint(channel_pulsar_eq_low)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.frequency:")
        pprint(await channel_pulsar_eq_low.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.f:")
        pprint(await channel_pulsar_eq_low.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.lo_freq:")
        pprint(await channel_pulsar_eq_low.lo_freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.boost:")
        pprint(await channel_pulsar_eq_low.boost.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.b:")
        pprint(await channel_pulsar_eq_low.b.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.lo_boost:")
        pprint(await channel_pulsar_eq_low.lo_boost.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.attenuation:")
        pprint(await channel_pulsar_eq_low.attenuation.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.att:")
        pprint(await channel_pulsar_eq_low.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low.lo_att:")
        pprint(await channel_pulsar_eq_low.lo_att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.l5:")
        pprint(plugin.l5)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid:")
        channel_pulsar_eq_low_mid = plugin.low_mid
        pprint(channel_pulsar_eq_low_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.frequency:")
        pprint(await channel_pulsar_eq_low_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.f:")
        pprint(await channel_pulsar_eq_low_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.lo_mid_freq:")
        pprint(await channel_pulsar_eq_low_mid.lo_mid_freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.boost:")
        pprint(await channel_pulsar_eq_low_mid.boost.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.b:")
        pprint(await channel_pulsar_eq_low_mid.b.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_mid.lo_mid_boost:")
        pprint(await channel_pulsar_eq_low_mid.lo_mid_boost.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.m5:")
        pprint(plugin.m5)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid:")
        channel_pulsar_eq_mid = plugin.mid
        pprint(channel_pulsar_eq_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.frequency:")
        pprint(await channel_pulsar_eq_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.f:")
        pprint(await channel_pulsar_eq_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.mid_freq:")
        pprint(await channel_pulsar_eq_mid.mid_freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.dip:")
        pprint(await channel_pulsar_eq_mid.dip.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.d:")
        pprint(await channel_pulsar_eq_mid.d.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.mid_dip:")
        pprint(await channel_pulsar_eq_mid.mid_dip.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.h5:")
        pprint(plugin.h5)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid:")
        channel_pulsar_eq_high_mid = plugin.high_mid
        pprint(channel_pulsar_eq_high_mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.frequency:")
        pprint(await channel_pulsar_eq_high_mid.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.f:")
        pprint(await channel_pulsar_eq_high_mid.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.hi_mid_freq:")
        pprint(await channel_pulsar_eq_high_mid.hi_mid_freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.boost:")
        pprint(await channel_pulsar_eq_high_mid.boost.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.b:")
        pprint(await channel_pulsar_eq_high_mid.b.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_mid.hi_mid_boost:")
        pprint(await channel_pulsar_eq_high_mid.hi_mid_boost.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.h1:")
        pprint(plugin.h1)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high:")
        channel_pulsar_eq_high = plugin.high
        pprint(channel_pulsar_eq_high)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.frequency:")
        pprint(await channel_pulsar_eq_high.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.f:")
        pprint(await channel_pulsar_eq_high.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.hi_freq:")
        pprint(await channel_pulsar_eq_high.hi_freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.boost:")
        pprint(await channel_pulsar_eq_high.boost.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.b:")
        pprint(await channel_pulsar_eq_high.b.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.hi_boost:")
        pprint(await channel_pulsar_eq_high.hi_boost.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.attenuation:")
        pprint(await channel_pulsar_eq_high.attenuation.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.att:")
        pprint(await channel_pulsar_eq_high.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.hi_att:")
        pprint(await channel_pulsar_eq_high.hi_att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.width:")
        pprint(await channel_pulsar_eq_high.width.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.w:")
        pprint(await channel_pulsar_eq_high.w.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.hi_width:")
        pprint(await channel_pulsar_eq_high.hi_width.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.attenuation_frequency:")
        pprint(await channel_pulsar_eq_high.attenuation_frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.attf:")
        pprint(await channel_pulsar_eq_high.attf.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.hi_att_freq:")
        pprint(await channel_pulsar_eq_high.hi_att_freq.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def mach4(plugin, pathstr, sleep, noauto=False):
        """

        :param plugin:
        :return:
        """
        print(f"{pathstr}.sub:")
        pprint(await plugin.sub.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz40:")
        pprint(await plugin.hz40.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz160:")
        pprint(await plugin.hz160.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz650:")
        pprint(await plugin.hz650.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz2k5:")
        pprint(await plugin.hz2k5.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.air_gain:")
        pprint(await plugin.air_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.air_freq:")
        pprint(await plugin.air_freq.get())
        await asyncio.sleep(sleep)
        if not noauto:
            print(f"{pathstr}.auto:")
            pprint(await plugin.auto.get())
            await asyncio.sleep(sleep)
            print(f"{pathstr}.again:")
            pprint(await plugin.again.get())
            await asyncio.sleep(sleep)

    @staticmethod
    async def pia(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.g:")
        pprint(await plugin.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz31:")
        pprint(await plugin.hz31.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz63:")
        pprint(await plugin.hz63.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz125:")
        pprint(await plugin.hz125.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz250:")
        pprint(await plugin.hz250.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz500:")
        pprint(await plugin.hz500.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz1:")
        pprint(await plugin.khz1.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz2:")
        pprint(await plugin.khz2.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz4:")
        pprint(await plugin.khz4.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz8:")
        pprint(await plugin.khz8.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz16:")
        pprint(await plugin.khz16.get())
        await asyncio.sleep(sleep)


class Dyn:
    """

    """
    def __init__(self):
        """

        """

    @staticmethod
    async def compexp(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.knee:")
        pprint(await plugin.knee.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.detector:")
        pprint(await plugin.detector.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.det:")
        pprint(await plugin.det.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hold:")
        pprint(await plugin.hold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hld:")
        pprint(await plugin.hld.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.envelope:")
        pprint(await plugin.envelope.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.env:")
        pprint(await plugin.env.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.auto_envelope:")
        pprint(await plugin.auto_envelope.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.auto:")
        pprint(await plugin.auto.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def b160(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.power:")
        pprint(await plugin.power.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compression:")
        pprint(await plugin.compression.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.output_gain:")
        pprint(await plugin.output_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def b560(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.bypass:")
        pprint(await plugin.bypass.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compression_ratio:")
        pprint(await plugin.compression_ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.output_gain:")
        pprint(await plugin.output_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.easy:")
        pprint(await plugin.easy.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.auto:")
        pprint(await plugin.auto.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def d241(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.bypass:")
        pprint(await plugin.bypass.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.auto:")
        pprint(await plugin.auto.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.l:")
        pprint(plugin.l)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak:")
        peak = plugin.peak
        pprint(peak)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak.threshold:")
        pprint(await peak.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak.lim:")
        pprint(await peak.lim.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak.release:")
        pprint(await peak.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak.lrel:")
        pprint(await peak.lrel.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def ecl33(plugin, pathstr, sleep, powerless=False):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        if not powerless:
            print(f"{pathstr}.power:")
            pprint(await plugin.power.get())
            await asyncio.sleep(sleep)
            print(f"{pathstr}.on:")
            pprint(await plugin.on.get())
            await asyncio.sleep(sleep)
        print(f"{pathstr}.limit:")
        limiter = plugin.limit
        pprint(limiter)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limit.limit:")
        pprint(await limiter.limit.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limit.lon:")
        pprint(await limiter.lon.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limit.threshold:")
        pprint(await limiter.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limit.lthr:")
        pprint(await limiter.lthr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limit.recovery:")
        pprint(await limiter.recovery.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limit.lrec:")
        pprint(await limiter.lrec.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limit.attack:")
        pprint(await limiter.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limit.lfast:")
        pprint(await limiter.lfast.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress:")
        compressor = plugin.compress
        pprint(compressor)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.compress:")
        pprint(await compressor.compress.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.con:")
        pprint(await compressor.con.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.threshold:")
        pprint(await compressor.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.cthr:")
        pprint(await compressor.cthr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.ratio:")
        pprint(await compressor.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.recovery:")
        pprint(await compressor.recovery.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.crec:")
        pprint(await compressor.crec.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.gain:")
        pprint(await compressor.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.cgain:")
        pprint(await compressor.cgain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.attack:")
        pprint(await compressor.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.compress.cfast:")
        pprint(await compressor.cfast.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def c9000(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.fast:")
        pprint(await plugin.fast.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak:")
        pprint(await plugin.peak.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def sbus(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.makeup:")
        pprint(await plugin.makeup.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def red3(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.make_up_gain:")
        pprint(await plugin.make_up_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.auto:")
        pprint(await plugin.auto.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def f670(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.out_gain:")
        pprint(await plugin.out_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.input_gain:")
        pprint(await plugin.input_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.time_constant:")
        pprint(await plugin.time_constant.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.time:")
        pprint(await plugin.time.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.dc_bias:")
        pprint(await plugin.dc_bias.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.bias:")
        pprint(await plugin.bias.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def bliss(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.thr:")
        pprint(await plugin.thr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.auto_fast:")
        pprint(await plugin.auto_fast.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.afast:")
        pprint(await plugin.afast.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.anti_log:")
        pprint(await plugin.anti_log.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.alog:")
        pprint(await plugin.alog.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.glon:")
        pprint(await plugin.glon.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gr_limit:")
        pprint(await plugin.gr_limit.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.glim:")
        pprint(await plugin.glim.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def nstr(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.bypass:")
        pprint(await plugin.bypass.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.input:")
        pprint(await plugin.input.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.output:")
        pprint(await plugin.output.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.out:")
        pprint(await plugin.out.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def p2250(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.on:")
        pprint(await plugin.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tresh:")
        pprint(await plugin.tresh.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.threshold:")
        pprint(await plugin.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.knee:")
        pprint(await plugin.knee.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.type:")
        pprint(await plugin.type.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def l100(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ingain:")
        pprint(await plugin.ingain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain_reduction:")
        pprint(await plugin.gain_reduction.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gr:")
        pprint(await plugin.gr.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.att:")
        pprint(await plugin.att.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rel:")
        pprint(await plugin.rel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.dry_wet:")
        pprint(await plugin.dry_wet.get())
        await asyncio.sleep(sleep)


class FX:
    """

    """
    def __init__(self):
        """

        """

    @staticmethod
    async def none(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """

    @staticmethod
    async def ext(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.source_group:")
        pprint(await plugin.source_group.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.group:")
        pprint(await plugin.group.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.external_source_group:")
        pprint(await plugin.external_source_group.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.external_group:")
        pprint(await plugin.external_group.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.egrp:")
        pprint(await plugin.egrp.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.source_index:")
        pprint(await plugin.source_index.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.latency:")
        pprint(await plugin.latency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.trim:")
        pprint(await plugin.trim.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def base_reverb(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.pre_dly:")
        pprint(await plugin.pre_dly.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.size:")
        pprint(await plugin.size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.damping:")
        pprint(await plugin.damping.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lo_cut:")
        pprint(await plugin.lo_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hi_cut:")
        pprint(await plugin.hi_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.diffusion:")
        pprint(await plugin.diffusion.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def base_bm_reverb(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.base_reverb(plugin, pathstr, sleep)
        print(f"{pathstr}.bass_mult:")
        pprint(await plugin.bass_mult.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.spread:")
        pprint(await plugin.spread.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def base_shaped_reverb(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.base_bm_reverb(plugin, pathstr, sleep)
        print(f"{pathstr}.shape:")
        pprint(await plugin.shape.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def hall(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.base_shaped_reverb(plugin, pathstr, sleep)
        print(f"{pathstr}.mod_spd:")
        pprint(await plugin.mod_spd.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def room_echo(plugin, pathstr, sleep, side):
        print(f"{pathstr}.echo_{side}:")
        echo = getattr(plugin, f"echo_{side}")
        pprint(echo)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.echo_{side}.depth:")
        pprint(await echo.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.echo_{side}.feed:")
        pprint(await echo.feed.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def room(plugin, pathstr, sleep, shapeless=False):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        if shapeless:
            await FX.base_bm_reverb(plugin, pathstr, sleep)
        else:
            await FX.base_shaped_reverb(plugin, pathstr, sleep)
        print(f"{pathstr}.spin:")
        pprint(await plugin.spin.get())
        await asyncio.sleep(sleep)
        await FX.room_echo(plugin, pathstr, sleep, "l")
        await FX.room_echo(plugin, pathstr, sleep, "r")

    @staticmethod
    async def chamber_echo(plugin, pathstr, side, sleep):
        print(f"{pathstr}.echo_{side}:")
        echo = getattr(plugin, f"echo_{side}")
        pprint(echo)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.echo_{side}.depth:")
        pprint(await echo.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.echo_{side}.level:")
        pprint(await echo.level.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def chamber(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.base_shaped_reverb(plugin, pathstr, sleep)
        print(f"{pathstr}.spin:")
        pprint(await plugin.spin.get())
        await asyncio.sleep(sleep)
        await FX.chamber_echo(plugin, pathstr, "l", sleep)
        await FX.chamber_echo(plugin, pathstr, "r", sleep)

    @staticmethod
    async def plate(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.room(plugin, pathstr, shapeless=True, sleep=sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def concert_refl(plugin, pathstr, side, sleep):
        print(f"{pathstr}.refl_{side}:")
        refl = getattr(plugin, f"refl_{side}")
        pprint(refl)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.refl_{side}.depth:")
        pprint(await refl.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.refl_{side}.level:")
        pprint(await refl.level.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def concert(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.base_shaped_reverb(plugin, pathstr, sleep)
        print(f"{pathstr}.depth:")
        pprint(await plugin.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.spin:")
        pprint(await plugin.spin.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.chorus:")
        pprint(await plugin.chorus.get())
        await asyncio.sleep(sleep)
        await FX.concert_refl(plugin, pathstr, "l", sleep)
        await FX.concert_refl(plugin, pathstr, "r", sleep)

    @staticmethod
    async def ambi(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.base_reverb(plugin, pathstr, sleep)
        print(f"{pathstr}.tail_gain:")
        pprint(await plugin.tail_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mod_spd:")
        pprint(await plugin.mod_spd.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def vroom(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.rcv_delay:")
        pprint(await plugin.rcv_delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.room_size:")
        pprint(await plugin.room_size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.density:")
        pprint(await plugin.density.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er_level:")
        pprint(await plugin.er_level.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_multiply:")
        pprint(await plugin.low_multiply.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_multiply:")
        pprint(await plugin.high_multiply.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_cut:")
        pprint(await plugin.low_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_cut:")
        pprint(await plugin.high_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.freeze:")
        pprint(await plugin.freeze.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er_delay_l:")
        pprint(await plugin.er_delay_l.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er_delay_r:")
        pprint(await plugin.er_delay_r.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.add:")
        pprint(await plugin.add.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.level:")
        pprint(await plugin.level.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def vrev(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.predelay:")
        pprint(await plugin.predelay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lo_multi:")
        pprint(await plugin.lo_multi.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hi_multi:")
        pprint(await plugin.hi_multi.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.modulate:")
        pprint(await plugin.modulate.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lo_cut:")
        pprint(await plugin.lo_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hi_cut:")
        pprint(await plugin.hi_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.output:")
        pprint(await plugin.output.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.transformer:")
        pprint(await plugin.transformer.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def vplate(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.pre_delay:")
        pprint(await plugin.pre_delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter:")
        pprint(await plugin.filter.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.colour:")
        pprint(await plugin.colour.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def digital_reverb(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.pre_delay:")
        pprint(await plugin.pre_delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.diffuse:")
        pprint(await plugin.diffuse.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.spread:")
        pprint(await plugin.spread.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lo_cut:")
        pprint(await plugin.lo_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_shelv:")
        shelv = plugin.high_shelv
        pprint(shelv)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_shelv.freq:")
        pprint(await shelv.freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_shelv.gain:")
        pprint(await shelv.gain.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def gated(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.digital_reverb(plugin, pathstr, sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.density:")
        pprint(await plugin.density.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def reverse(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.digital_reverb(plugin, pathstr, sleep)
        print(f"{pathstr}.rise:")
        pprint(await plugin.rise.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def del_section(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.time:")
        pprint(await plugin.time.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.feedback:")
        pprint(await plugin.feedback.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hicut:")
        pprint(await plugin.hicut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.level:")
        pprint(await plugin.level.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def rev_section(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.delay:")
        pprint(await plugin.delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.predel:")
        pprint(await plugin.predel.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.size:")
        pprint(await plugin.size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.damping:")
        pprint(await plugin.damping.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.locut:")
        pprint(await plugin.locut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.direct:")
        pprint(await plugin.direct.get())
        await asyncio.sleep(sleep)


    @staticmethod
    async def delrev(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.delay:")
        delay = plugin.delay
        pprint(delay)
        await asyncio.sleep(sleep)
        await FX.del_section(delay, f"{pathstr}.delay", sleep)
        print(f"{pathstr}.reverb:")
        reverb = plugin.reverb
        pprint(reverb)
        await asyncio.sleep(sleep)
        await FX.rev_section(reverb, f"{pathstr}.reverb", sleep)

    @staticmethod
    async def shimmer(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.pre_delay:")
        pprint(await plugin.pre_delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.size:")
        pprint(await plugin.size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lo_cut:")
        pprint(await plugin.lo_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hi_cut:")
        pprint(await plugin.hi_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.damping:")
        pprint(await plugin.damping.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.shimmer:")
        pprint(await plugin.shimmer.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.shine:")
        pprint(await plugin.shine.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def spring(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.density:")
        pprint(await plugin.density.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.bass:")
        pprint(await plugin.bass.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.treble:")
        pprint(await plugin.treble.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def dimcrs(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.preset_1:")
        pprint(await plugin.preset_1.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.preset_2:")
        pprint(await plugin.preset_2.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.preset_3:")
        pprint(await plugin.preset_3.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.preset_4:")
        pprint(await plugin.preset_4.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.stereo:")
        pprint(await plugin.stereo.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mono:")
        pprint(await plugin.mono.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.dry:")
        pprint(await plugin.dry.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def filter_section(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.lo_cut:")
        pprint(await plugin.lo_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hi_cut:")
        pprint(await plugin.hi_cut.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def chorus(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.modulator:")
        modulator = plugin.modulator
        pprint(modulator)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.modulator.wave:")
        pprint(await modulator.wave.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.modulator.phase:")
        pprint(await modulator.phase.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.modulator.spread:")
        pprint(await modulator.spread.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.modulator.speed:")
        pprint(await modulator.speed.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_left:")
        delay_left = plugin.delay_left
        pprint(delay_left)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_left.size:")
        pprint(await delay_left.size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_left.depth:")
        pprint(await delay_left.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_right:")
        delay_right = plugin.delay_right
        pprint(delay_right)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_right.size:")
        pprint(await delay_right.size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_right.depth:")
        pprint(await delay_right.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter_wing:")
        filter_wing = plugin.filter_wing
        pprint(filter_wing)
        await asyncio.sleep(sleep)
        await FX.filter_section(filter_wing, f"{pathstr}.filter_wing", sleep)

    @staticmethod
    async def flanger(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.phase:")
        pprint(await plugin.phase.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.speed:")
        pprint(await plugin.speed.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.feedback:")
        feedback = plugin.feedback
        pprint(feedback)
        await asyncio.sleep(sleep)
        await FX.filter_section(feedback, f"{pathstr}.feedback", sleep)
        print(f"{pathstr}.feedback.feedback:")
        pprint(await feedback.feedback.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_left:")
        delay_left = plugin.delay_left
        pprint(delay_left)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_left.size:")
        pprint(await delay_left.size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_left.depth:")
        pprint(await delay_left.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_right:")
        delay_right = plugin.delay_right
        pprint(delay_right)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_right.size:")
        pprint(await delay_right.size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay_right.depth:")
        pprint(await delay_right.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.twin_filter:")
        twin_filter = plugin.twin_filter
        pprint(twin_filter)
        await asyncio.sleep(sleep)
        await FX.filter_section(twin_filter, f"{pathstr}.twin_filter", sleep)

    @staticmethod
    async def stdl(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.time:")
        pprint(await plugin.time.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.stereo:")
        pprint(await plugin.stereo.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.cross:")
        pprint(await plugin.cross.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mono:")
        pprint(await plugin.mono.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.factor:")
        pprint(await plugin.factor.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.pattern:")
        pprint(await plugin.pattern.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.offset:")
        pprint(await plugin.offset.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.feedback:")
        pprint(await plugin.feedback.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.fb_locut:")
        pprint(await plugin.fb_locut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.fb_hicut:")
        pprint(await plugin.fb_hicut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_cut:")
        pprint(await plugin.low_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_cut:")
        pprint(await plugin.high_cut.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def tapdl_stereo(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.width:")
        pprint(await plugin.width.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.diffusion:")
        pprint(await plugin.diffusion.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def tapdl_delay(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.time:")
        pprint(await plugin.time.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.factor:")
        pprint(await plugin.factor.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.pre_delay:")
        pprint(await plugin.pre_delay.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def tapdl_tb(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.repeats:")
        pprint(await plugin.repeats.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.slope:")
        pprint(await plugin.slope.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def tapdl(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.stereo:")
        stereo = plugin.stereo
        pprint(stereo)
        await asyncio.sleep(sleep)
        await FX.tapdl_stereo(stereo, f"{pathstr}.stereo", sleep)
        print(f"{pathstr}.filter:")
        filter = plugin.filter
        pprint(filter)
        await asyncio.sleep(sleep)
        await FX.filter_section(filter, f"{pathstr}.filter", sleep)
        print(f"{pathstr}.delay:")
        delay = plugin.delay
        pprint(delay)
        await asyncio.sleep(sleep)
        await FX.tapdl_delay(delay, f"{pathstr}.delay", sleep)
        print(f"{pathstr}.trim_balance:")
        trim_balance = plugin.trim_balance
        pprint(trim_balance)
        await asyncio.sleep(sleep)
        await FX.tapdl_tb(trim_balance, f"{pathstr}.trim_balance", sleep)

    @staticmethod
    async def tapedl(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.time:")
        pprint(await plugin.time.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.sustain:")
        pprint(await plugin.sustain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.drive:")
        pprint(await plugin.drive.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.flutter:")
        pprint(await plugin.flutter.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def oilcan(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.time:")
        pprint(await plugin.time.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.sustain:")
        pprint(await plugin.sustain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.wobble:")
        pprint(await plugin.wobble.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tone:")
        pprint(await plugin.tone.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def bbddl(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.delay:")
        pprint(await plugin.delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.feedback:")
        pprint(await plugin.feedback.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def pitch(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.semi:")
        pprint(await plugin.semi.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.cents:")
        pprint(await plugin.cents.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.delay:")
        pprint(await plugin.delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.locut:")
        pprint(await plugin.locut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hicut:")
        pprint(await plugin.hicut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def dpitch(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.locut:")
        pprint(await plugin.locut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hicut:")
        pprint(await plugin.hicut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a:")
        a = plugin.a
        pprint(a)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a.semitones:")
        pprint(await a.semitones.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a.cents:")
        pprint(await a.cents.get())
        await asyncio.sleep(sleep)
        await a.cents.set(-50)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a.cents:")
        pprint(await a.cents.get())
        await asyncio.sleep(sleep)
        await a.cents.set(0)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a.cents:")
        pprint(await a.cents.get())
        await asyncio.sleep(sleep)
        await a.cents.set(50)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a.cents:")
        pprint(await a.cents.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a.delay:")
        pprint(await a.delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a.pan:")
        pprint(await a.pan.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a.level:")
        pprint(await a.level.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.b:")
        b = plugin.b
        pprint(b)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.b.semitones:")
        pprint(await b.semitones.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.b.cents:")
        pprint(await b.cents.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.b.delay:")
        pprint(await b.delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.b.pan:")
        pprint(await b.pan.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.b.level:")
        pprint(await b.level.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def vss3(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.preset:")
        pprint(await plugin.preset.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.load:")
        pprint(await plugin.load.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lo_damp:")
        pprint(await plugin.lo_damp.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hi_dcy:")
        pprint(await plugin.hi_dcy.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hi_cut:")
        pprint(await plugin.hi_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.rev_lvl:")
        pprint(await plugin.rev_lvl.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er_lvl:")
        pprint(await plugin.er_lvl.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.view:")
        pprint(await plugin.view.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main:")
        mainsec = plugin.main
        pprint(mainsec)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.decay:")
        pprint(await mainsec.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.lo_dcy:")
        pprint(await mainsec.lo_dcy.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.lomid_dcy:")
        pprint(await mainsec.lomid_dcy.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.himid_dcy:")
        pprint(await mainsec.himid_dcy.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.hi_dcy:")
        pprint(await mainsec.hi_dcy.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.hi_soft:")
        pprint(await mainsec.hi_soft.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.lo_xo:")
        pprint(await mainsec.lo_xo.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.mid_xo:")
        pprint(await mainsec.mid_xo.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.hi_xo:")
        pprint(await mainsec.hi_xo.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.lo_shv:")
        pprint(await mainsec.lo_shv.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.lo_damp:")
        pprint(await mainsec.lo_damp.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.main.hi_cut:")
        pprint(await mainsec.hi_cut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er:")
        er = plugin.er
        pprint(er)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er.pdly:")
        pprint(await er.pdly.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er.type:")
        pprint(await er.type.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er.size:")
        pprint(await er.size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er.pos:")
        pprint(await er.pos.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er.bal:")
        pprint(await er.bal.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er.lcut:")
        pprint(await er.lcut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er.col:")
        pprint(await er.col.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.er.lvl:")
        pprint(await er.lvl.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tail:")
        tail = plugin.tail
        pprint(tail)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tail.type:")
        pprint(await tail.type.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tail.wid:")
        pprint(await tail.wid.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tail.pdly:")
        pprint(await tail.pdly.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mod:")
        mod = plugin.mod
        pprint(mod)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mod.type:")
        pprint(await mod.type.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mod.rate:")
        pprint(await mod.rate.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mod.wid:")
        pprint(await mod.wid.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def bplate(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.predelay:")
        pprint(await plugin.predelay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.size:")
        pprint(await plugin.size.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.decay:")
        pprint(await plugin.decay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.bassmult:")
        pprint(await plugin.bassmult.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.damping:")
        pprint(await plugin.damping.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.locut:")
        pprint(await plugin.locut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hicut:")
        pprint(await plugin.hicut.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.xover:")
        pprint(await plugin.xover.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mod:")
        pprint(await plugin.mod.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.spd:")
        pprint(await plugin.spd.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.diff:")
        pprint(await plugin.diff.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def geq(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.true_curve:")
        pprint(await plugin.true_curve.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.type:")
        pprint(await plugin.type.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz20:")
        pprint(await plugin.hz20.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz25:")
        pprint(await plugin.hz25.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz31:")
        pprint(await plugin.hz31.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz40:")
        pprint(await plugin.hz40.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz50:")
        pprint(await plugin.hz50.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz63:")
        pprint(await plugin.hz63.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz80:")
        pprint(await plugin.hz80.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz100:")
        pprint(await plugin.hz100.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz125:")
        pprint(await plugin.hz125.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz160:")
        pprint(await plugin.hz160.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz200:")
        pprint(await plugin.hz200.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz250:")
        pprint(await plugin.hz250.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz315:")
        pprint(await plugin.hz315.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz400:")
        pprint(await plugin.hz400.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz500:")
        pprint(await plugin.hz500.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz630:")
        pprint(await plugin.hz630.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz800:")
        pprint(await plugin.hz800.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz1k:")
        pprint(await plugin.hz1k.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz1k25:")
        pprint(await plugin.hz1k25.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz1k6:")
        pprint(await plugin.hz1k6.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz2k:")
        pprint(await plugin.hz2k.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz2k5:")
        pprint(await plugin.hz2k5.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz3k15:")
        pprint(await plugin.hz3k15.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz4k:")
        pprint(await plugin.hz4k.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz5k:")
        pprint(await plugin.hz5k.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz6k3:")
        pprint(await plugin.hz6k3.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz8k:")
        pprint(await plugin.hz8k.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz10k:")
        pprint(await plugin.hz10k.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz12k5:")
        pprint(await plugin.hz12k5.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz16k:")
        pprint(await plugin.hz16k.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz20k:")
        pprint(await plugin.hz20k.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.trim:")
        pprint(await plugin.trim.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def pia(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz31:")
        pprint(await plugin.hz31.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz63:")
        pprint(await plugin.hz63.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz125:")
        pprint(await plugin.hz125.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz250:")
        pprint(await plugin.hz250.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hz500:")
        pprint(await plugin.hz500.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz1:")
        pprint(await plugin.khz1.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz2:")
        pprint(await plugin.khz2.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz4:")
        pprint(await plugin.khz4.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz8:")
        pprint(await plugin.khz8.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.khz16:")
        pprint(await plugin.khz16.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def double(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.spread:")
        pprint(await plugin.spread.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def pcorr(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.speed:")
        pprint(await plugin.speed.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.amount:")
        pprint(await plugin.amount.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a4_pitch:")
        pprint(await plugin.a4_pitch.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.c:")
        pprint(await plugin.c.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.d_flat:")
        pprint(await plugin.d_flat.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.d:")
        pprint(await plugin.d.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.e_flat:")
        pprint(await plugin.e_flat.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.e:")
        pprint(await plugin.e.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.f:")
        pprint(await plugin.f.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.g_flat:")
        pprint(await plugin.g_flat.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.g:")
        pprint(await plugin.g.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a_flat:")
        pprint(await plugin.a_flat.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.a:")
        pprint(await plugin.a.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.b_flat:")
        pprint(await plugin.b_flat.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.b:")
        pprint(await plugin.b.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def limiter(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.in_gain:")
        pprint(await plugin.in_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.out_gain:")
        pprint(await plugin.out_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.squeeze:")
        pprint(await plugin.squeeze.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.knee:")
        pprint(await plugin.knee.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.auto_gain:")
        pprint(await plugin.auto_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def des2(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.low:")
        pprint(await plugin.low.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high:")
        pprint(await plugin.high.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_side:")
        pprint(await plugin.low_side.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_side:")
        pprint(await plugin.high_side.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gender:")
        pprint(await plugin.gender.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.female:")
        pprint(await plugin.female.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.male:")
        pprint(await plugin.male.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.m_s_mode:")
        pprint(await plugin.m_s_mode.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def enhance(plugin, pathstr, sleep, mastersection=False):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        if not mastersection:
            print(f"{pathstr}.gain:")
            pprint(await plugin.gain.get())
            await asyncio.sleep(sleep)
            print(f"{pathstr}.solo:")
            pprint(await plugin.solo.get())
            await asyncio.sleep(sleep)
        print(f"{pathstr}.bass:")
        bass = plugin.bass
        pprint(bass)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.bass.gain:")
        pprint(await bass.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.bass.freq:")
        pprint(await bass.freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid:")
        mid = plugin.mid
        pprint(mid)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.gain:")
        pprint(await mid.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid.q:")
        pprint(await mid.q.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high:")
        high = plugin.high
        pprint(high)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.gain:")
        pprint(await high.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high.freq:")
        pprint(await high.freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.stereo:")
        stereo = plugin.stereo
        pprint(stereo)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.stereo.lmf_spread:")
        pprint(await stereo.lmf_spread.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.stereo.level:")
        pprint(await stereo.level.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.stereo.pan:")
        pprint(await stereo.pan.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mono:")
        mono = plugin.mono
        pprint(mono)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mono.level:")
        pprint(await mono.level.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mono.pan:")
        pprint(await mono.pan.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def exciter(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.tune:")
        pprint(await plugin.tune.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.peak:")
        pprint(await plugin.peak.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.zero_fill:")
        pprint(await plugin.zero_fill.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.timbre:")
        pprint(await plugin.timbre.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.harmonics:")
        pprint(await plugin.harmonics.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.dry:")
        pprint(await plugin.dry.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def pbass(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.intensity:")
        pprint(await plugin.intensity.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.bass_gain:")
        pprint(await plugin.bass_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.x_o_frequency:")
        pprint(await plugin.x_o_frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.solo:")
        pprint(await plugin.solo.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def rotary(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.balance:")
        pprint(await plugin.balance.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.distance:")
        pprint(await plugin.distance.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.speed_control:")
        speed_control = plugin.speed_control
        pprint(speed_control)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.speed_control.leslie_switch:")
        pprint(await speed_control.leslie_switch.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.speed_control.slow_rate:")
        pprint(await speed_control.slow_rate.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.speed_control.fast_rate:")
        pprint(await speed_control.fast_rate.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.acceleration:")
        acceleration = plugin.acceleration
        pprint(acceleration)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.acceleration.bass:")
        pprint(await acceleration.bass.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.acceleration.horn:")
        pprint(await acceleration.horn.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def lfo_section(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.speed:")
        pprint(await plugin.speed.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.phase:")
        pprint(await plugin.phase.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.shape:")
        pprint(await plugin.shape.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def envelope_section(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.hold:")
        pprint(await plugin.hold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def phaser(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.multi_phaser:")
        multi_phaser = plugin.multi_phaser
        pprint(multi_phaser)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.multi_phaser.range:")
        pprint(await multi_phaser.range.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.multi_phaser.depth:")
        pprint(await multi_phaser.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.multi_phaser.env_mod:")
        pprint(await multi_phaser.env_mod.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.multi_phaser.mix:")
        pprint(await multi_phaser.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.multi_phaser.stages:")
        pprint(await multi_phaser.stages.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.multi_phaser.resonance:")
        pprint(await multi_phaser.resonance.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lfo:")
        lfo = plugin.lfo
        pprint(lfo)
        await asyncio.sleep(sleep)
        await FX.lfo_section(lfo, f"{pathstr}.lfo", sleep)
        print(f"{pathstr}.envelope:")
        envelope = plugin.envelope
        pprint(envelope)
        await asyncio.sleep(sleep)
        await FX.envelope_section(envelope, f"{pathstr}.envelope", sleep)

    @staticmethod
    async def panner(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.tremolo:")
        tremolo = plugin.tremolo
        pprint(tremolo)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tremolo.depth:")
        pprint(await tremolo.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tremolo.envelope_modulation:")
        envelope_modulation = tremolo.envelope_modulation
        pprint(envelope_modulation)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tremolo.envelope_modulation.speed:")
        pprint(await envelope_modulation.speed.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tremolo.envelope_modulation.depth:")
        pprint(await envelope_modulation.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lfo:")
        lfo = plugin.lfo
        pprint(lfo)
        await asyncio.sleep(sleep)
        await FX.lfo_section(lfo, f"{pathstr}.lfo", sleep)
        print(f"{pathstr}.envelope:")
        envelope = plugin.envelope
        pprint(envelope)
        await asyncio.sleep(sleep)
        await FX.envelope_section(envelope, f"{pathstr}.envelope", sleep)

    @staticmethod
    async def tape(plugin, pathstr, sleep, no_outgain=False):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.drive:")
        pprint(await plugin.drive.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.speed:")
        pprint(await plugin.speed.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.low_bump:")
        pprint(await plugin.low_bump.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.high_shelv:")
        pprint(await plugin.high_shelv.get())
        await asyncio.sleep(sleep)
        if not no_outgain:
            print(f"{pathstr}.out_gain:")
            pprint(await plugin.out_gain.get())
            await asyncio.sleep(sleep)

    @staticmethod
    async def mood(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.drive:")
        pprint(await plugin.drive.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.envelope:")
        envelope = plugin.envelope
        pprint(envelope)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.envelope.depth:")
        pprint(await envelope.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.envelope.attack:")
        pprint(await envelope.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.envelope.hold:")
        pprint(await envelope.hold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.envelope.release:")
        pprint(await envelope.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter:")
        filter = plugin.filter
        pprint(filter)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.base_freq:")
        pprint(await filter.base_freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.type:")
        pprint(await filter.type.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.slope:")
        pprint(await filter.slope.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.resonance:")
        pprint(await filter.resonance.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lfo:")
        lfo = plugin.lfo
        pprint(lfo)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lfo.depth:")
        pprint(await lfo.depth.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lfo.speed:")
        pprint(await lfo.speed.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lfo.phase:")
        pprint(await lfo.phase.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lfo.wave:")
        pprint(await lfo.wave.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def sub(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.range:")
        pprint(await plugin.range.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.octave_1:")
        pprint(await plugin.octave_1.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.octave_2:")
        pprint(await plugin.octave_2.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def rackamp(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.pre_amp:")
        pprint(await plugin.pre_amp.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.buzz:")
        pprint(await plugin.buzz.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.punch:")
        pprint(await plugin.punch.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.crunch:")
        pprint(await plugin.crunch.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.drive:")
        pprint(await plugin.drive.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.out_gain:")
        pprint(await plugin.out_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.cabinet_simulation:")
        pprint(await plugin.cabinet_simulation.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.colour:")
        colour = plugin.colour
        pprint(colour)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.colour.lo_eq:")
        pprint(await colour.lo_eq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.colour.hi_eq:")
        pprint(await colour.hi_eq.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def amp_base(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.bass:")
        pprint(await plugin.bass.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.treble:")
        pprint(await plugin.treble.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.output_gain:")
        pprint(await plugin.output_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.cabinet:")
        pprint(await plugin.cabinet.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def mid_amp_base(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.amp_base(plugin, pathstr, sleep)
        print(f"{pathstr}.middle:")
        pprint(await plugin.middle.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def ukrock(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.mid_amp_base(plugin, pathstr, sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.presence:")
        pprint(await plugin.presence.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.master:")
        pprint(await plugin.master.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.sag:")
        pprint(await plugin.sag.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def angel(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.ukrock(plugin, pathstr, sleep)
        print(f"{pathstr}.clean_gain:")
        pprint(await plugin.clean_gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mid_boost:")
        pprint(await plugin.mid_boost.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.bright:")
        pprint(await plugin.bright.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.bottom:")
        pprint(await plugin.bottom.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def jazzc(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.mid_amp_base(plugin, pathstr, sleep)
        print(f"{pathstr}.volume:")
        pprint(await plugin.volume.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.bri:")
        pprint(await plugin.bri.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def deluxe(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        await FX.amp_base(plugin, pathstr, sleep)
        print(f"{pathstr}.volume:")
        pprint(await plugin.volume.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.sag:")
        pprint(await plugin.sag.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def body(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.body:")
        pprint(await plugin.body.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def c5cmb(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.thresh:")
        pprint(await plugin.thresh.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.ratio:")
        pprint(await plugin.ratio.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.slope:")
        pprint(await plugin.slope.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.selected_band:")
        pprint(await plugin.selected_band.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.attack:")
        pprint(await plugin.attack.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.release:")
        pprint(await plugin.release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.auto_release:")
        pprint(await plugin.auto_release.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.sbc:")
        pprint(await plugin.sbc.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.sbc_on:")
        pprint(await plugin.sbc_on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band_solo:")
        pprint(await plugin.band_solo.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band:")
        pprint(plugin.band)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1]:")
        band = plugin.band[1]
        pprint(band)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1].thresh:")
        pprint(await band.thresh.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1].gain:")
        pprint(await band.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1].bypass:")
        pprint(await band.bypass.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1].width:")
        pprint(await band.width.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def subm(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.mix:")
        pprint(await plugin.mix.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tune:")
        pprint(await plugin.tune.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band:")
        pprint(plugin.band)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1]:")
        pprint(await plugin.band[1].get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def vimg(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.ms_width:")
        pprint(await plugin.ms_width.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.stereoize:")
        pprint(await plugin.stereoize.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.gain:")
        pprint(await plugin.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.mode:")
        pprint(await plugin.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.k_stereo:")
        pprint(await plugin.k_stereo.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.velvet:")
        pprint(await plugin.velvet.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.deep:")
        pprint(await plugin.deep.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def spkman(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.filter:")
        filter = plugin.filter
        pprint(filter)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.phase:")
        pprint(await filter.phase.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.polarity:")
        pprint(await filter.polarity.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.precision_delay:")
        pprint(await filter.precision_delay.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.position:")
        pprint(await filter.position.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.high_pass:")
        high_pass = filter.high_pass
        pprint(high_pass)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.high_pass.frequency:")
        pprint(await high_pass.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.high_pass.type:")
        pprint(await high_pass.type.get())
        print(f"{pathstr}.filter.tilt_eq:")
        tilt_eq = filter.tilt_eq
        pprint(tilt_eq)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.tilt_eq.freq:")
        pprint(await tilt_eq.freq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.tilt_eq.gain:")
        pprint(await tilt_eq.gain.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.low_pass:")
        low_pass = filter.low_pass
        pprint(low_pass)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.low_pass.frequency:")
        pprint(await low_pass.frequency.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.filter.low_pass.type:")
        pprint(await low_pass.type.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.dyn_eq:")
        dyn_eq = plugin.dyn_eq
        pprint(dyn_eq)
        await asyncio.sleep(sleep)
        await Gate.deq(dyn_eq, f"{pathstr}.dyn_eq", sleep)
        print(f"{pathstr}.dyn_eq.dyn_eq:")
        pprint(await dyn_eq.dyn_eq.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.dyn_eq.on:")
        pprint(await dyn_eq.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limiter:")
        limiter = plugin.limiter
        pprint(limiter)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limiter.active:")
        pprint(await limiter.active.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limiter.threshold:")
        pprint(await limiter.threshold.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limiter.mode:")
        pprint(await limiter.mode.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limiter.rms:")
        pprint(await limiter.rms.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.limiter.peak:")
        pprint(await limiter.peak.get())
        await asyncio.sleep(sleep)

    @staticmethod
    async def deq3(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.band:")
        pprint(plugin.band)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.band[1]:")
        band = plugin.band[1]
        pprint(band)
        await asyncio.sleep(sleep)
        await Gate.deq(band, f"{pathstr}.band[1]", sleep)
        print(f"{pathstr}.band[2]:")
        band = plugin.band[2]
        pprint(band)
        await asyncio.sleep(sleep)
        await Gate.deq(band, f"{pathstr}.band[2]", sleep)
        print(f"{pathstr}.band[3]:")
        band = plugin.band[3]
        pprint(band)
        await asyncio.sleep(sleep)
        await Gate.deq(band, f"{pathstr}.band[3]", sleep)

    @staticmethod
    async def even(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.gate:")
        gate = plugin.gate
        pprint(gate)
        await asyncio.sleep(sleep)
        await Gate.e88(gate, f"{pathstr}.gate", sleep)
        print(f"{pathstr}.eq:")
        eq = plugin.eq
        pprint(eq)
        await asyncio.sleep(sleep)
        await EQ.e88(eq, f"{pathstr}.eq", sleep)
        print(f"{pathstr}.eq.on:")
        pprint(await eq.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.dyn:")
        dyn = plugin.dyn
        pprint(dyn)
        await asyncio.sleep(sleep)
        await Dyn.ecl33(dyn, f"{pathstr}.dyn", powerless=True, sleep=sleep)

    @staticmethod
    async def soulch(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.gate:")
        gate = plugin.gate
        pprint(gate)
        await asyncio.sleep(sleep)
        await Gate.g9000(gate, f"{pathstr}.gate", sleep)
        print(f"{pathstr}.eq:")
        eq = plugin.eq
        pprint(eq)
        await asyncio.sleep(sleep)
        await EQ.soul(eq, f"{pathstr}.eq", sleep)
        print(f"{pathstr}.eq.on:")
        pprint(await eq.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.dyn:")
        dyn = plugin.dyn
        pprint(dyn)
        await asyncio.sleep(sleep)
        await Dyn.c9000(dyn, f"{pathstr}.dyn", sleep)

    @staticmethod
    async def vintage(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.dyn:")
        dyn = plugin.dyn
        pprint(dyn)
        await asyncio.sleep(sleep)
        await Multi.la76(dyn, f"{pathstr}.dyn", sleep)
        print(f"{pathstr}.dyn.on:")
        pprint(await dyn.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.eq:")
        eq = plugin.eq
        pprint(eq)
        await asyncio.sleep(sleep)
        await EQ.pulsar(eq, f"{pathstr}.eq", sleep)
        print(f"{pathstr}.lvl:")
        lvl = plugin.lvl
        pprint(lvl)
        await asyncio.sleep(sleep)
        await Multi.la(lvl, f"{pathstr}.lvl", sleep)

    @staticmethod
    async def bus(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.warm:")
        warm = plugin.warm
        pprint(warm)
        await asyncio.sleep(sleep)
        await Gate.warm(warm, f"{pathstr}.warm", sleep)
        print(f"{pathstr}.eq:")
        eq = plugin.eq
        pprint(eq)
        await asyncio.sleep(sleep)
        await EQ.e84(eq, f"{pathstr}.eq", sleep)
        print(f"{pathstr}.eq.on:")
        pprint(await eq.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.dyn:")
        dyn = plugin.dyn
        pprint(dyn)
        await asyncio.sleep(sleep)
        await Dyn.sbus(dyn, f"{pathstr}.dyn", sleep)

    @staticmethod
    async def master(plugin, pathstr, sleep):
        """

        :param plugin:
        :param pathstr:
        :return:
        """
        print(f"{pathstr}.tape:")
        tape = plugin.tape
        pprint(tape)
        await asyncio.sleep(sleep)
        await FX.tape(tape, f"{pathstr}.tape", no_outgain=True, sleep=sleep)
        print(f"{pathstr}.tape.power:")
        pprint(await tape.power.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.tape.on:")
        pprint(await tape.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.eq:")
        eq = plugin.eq
        pprint(eq)
        await asyncio.sleep(sleep)
        await EQ.mach4(eq, f"{pathstr}.eq", noauto=True, sleep=sleep)
        print(f"{pathstr}.eq.on:")
        pprint(await eq.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.enh:")
        enh = plugin.enh
        pprint(enh)
        await asyncio.sleep(sleep)
        await FX.enhance(enh, f"{pathstr}.enh", mastersection=True, sleep=sleep)
        print(f"{pathstr}.enh.on:")
        pprint(await enh.on.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.lim:")
        lim = plugin.lim
        pprint(lim)
        await asyncio.sleep(sleep)
        await FX.limiter(lim, f"{pathstr}.lim", sleep)
        print(f"{pathstr}.lim.on:")
        pprint(await lim.on.get())
        await asyncio.sleep(sleep)


async def print_plugins(base_component, plugin_map, pathstr, sleep):
    """

    :param base_component:
    :param plugin_map:
    :param pathstr:
    :return:
    """
    for name, method in plugin_map.items():
        print("\n----------------------------")
        await base_component.model.set(name)
        await asyncio.sleep(sleep)
        print(f"{pathstr}.model:")
        pprint(await base_component.model.get())
        await asyncio.sleep(sleep)
        print(f"{pathstr}.plugin:")
        plugin = await base_component.plugin()
        pprint(plugin)
        await asyncio.sleep(sleep)
        await method(plugin=plugin, pathstr=f"{pathstr}.plugin", sleep=sleep)
        print("----------------------------\n")


async def mixer_status(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    status = mixer.status
    print(f"mixer.status:")
    pprint(status)
    await asyncio.sleep(sleep)
    aes50_a = status.aes50_a
    print(f"mixer.status.aes50_a: ")
    pprint(aes50_a)
    await asyncio.sleep(sleep)
    print("mixer.status.aes50_a.status:")
    pprint(await aes50_a.status.get())
    await asyncio.sleep(sleep)
    print("mixer.status.aes50_a.device:")
    pprint(await aes50_a.device.get())
    await asyncio.sleep(sleep)
    aes50_b = status.aes50_b
    print(f"mixer.status.aes50_b: ")
    pprint(aes50_b)
    await asyncio.sleep(sleep)
    print("mixer.status.aes50_b.status:")
    pprint(await aes50_b.status.get())
    await asyncio.sleep(sleep)
    print("mixer.status.aes50_b.device:")
    pprint(await aes50_b.device.get())
    await asyncio.sleep(sleep)
    aes50_c = status.aes50_c
    print(f"mixer.status.aes50_c: ")
    pprint(aes50_c)
    await asyncio.sleep(sleep)
    print("mixer.status.aes50_c.status:")
    pprint(await aes50_c.status.get())
    await asyncio.sleep(sleep)
    print("mixer.status.aes50_c.device:")
    pprint(await aes50_c.device.get())
    await asyncio.sleep(sleep)
    print("mixer.status.clock.lock:")
    pprint(await status.clock.lock.get())
    await asyncio.sleep(sleep)
    print("mixer.status.clock.ppm:")
    pprint(await status.clock.ppm.get())
    await asyncio.sleep(sleep)
    print("mixer.status.clock.real_time_error:")
    pprint(await status.clock.real_time_error.get())
    await asyncio.sleep(sleep)
    print("mixer.status.solo:")
    pprint(await status.solo.get())
    await asyncio.sleep(sleep)
    print("mixer.status.solo_in_place:")
    pprint(await status.solo_in_place.get())
    await asyncio.sleep(sleep)
    print("mixer.status.current_time:")
    pprint(await status.current_time.get())
    await asyncio.sleep(sleep)
    usb_player = status.usb_player
    print(f"mixer.status.usb_player: ")
    pprint(usb_player)
    await asyncio.sleep(sleep)
    print("mixer.status.usb_player.status:")
    pprint(await usb_player.status.get())
    await asyncio.sleep(sleep)
    print("mixer.status.usb_player.volume_name:")
    pprint(await usb_player.volume_name.get())
    await asyncio.sleep(sleep)
    sc = status.stage_connect
    print(f"mixer.status.stage_connect: ")
    pprint(sc)
    await asyncio.sleep(sleep)
    print("mixer.status.stage_connect.status:")
    pprint(await sc.status.get())
    await asyncio.sleep(sleep)
    print("mixer.status.stage_connect.devices:")
    pprint(await sc.devices.get())
    await asyncio.sleep(sleep)
    print("mixer.status.stage_connect.upstreams:")
    pprint(await sc.upstreams.get())
    await asyncio.sleep(sleep)
    print("mixer.status.stage_connect.downstreams:")
    pprint(await sc.downstreams.get())
    await asyncio.sleep(sleep)
    print("mixer.status.stage_connect.upstream_routing:")
    pprint(await sc.upstream_routing.get())
    await asyncio.sleep(sleep)
    print("mixer.status.remote_a:")
    pprint(await status.remote_a.get())
    await asyncio.sleep(sleep)
    print("mixer.status.remote_b:")
    pprint(await status.remote_b.get())
    await asyncio.sleep(sleep)
    print("mixer.status.remote_c:")
    pprint(await status.remote_c.get())
    await asyncio.sleep(sleep)


async def mixer_general_configuration(mixer: WING, sleep):
    """

    :return:
    """
    gconf = mixer.general_configuration
    print(f"mixer.general_configuration:")
    pprint(gconf)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.main_link:")
    pprint(await gconf.main_link.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.dca_mutegroups:")
    pprint(await gconf.dca_mutegroups.get())
    await asyncio.sleep(sleep)

    await gconf_monitor_bus(gconf=gconf, sleep=sleep)
    await gconf_solo(gconf=gconf, sleep=sleep)
    await gconf_rta(gconf=gconf, sleep=sleep)
    await gconf_meters(gconf=gconf, sleep=sleep)
    await gconf_talkback(gconf=gconf, sleep=sleep)

    automix = gconf.automix
    print("mixer.general_configuration.automix:")
    pprint(automix)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.automix.x:")
    pprint(await automix.x.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.automix.y:")
    pprint(await automix.y.get())
    await asyncio.sleep(sleep)


async def gconf_monitor_bus(gconf, sleep):
    """

    :param general_configuration:
    :return:
    """
    monitor_bus = gconf.monitor_bus
    print("mixer.general_configuration.monitor_bus:")
    pprint(monitor_bus)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1]:")
    pprint(monitor_bus[1])
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].level:")
    pprint(await monitor_bus[1].level.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].invert_polarity:")
    pprint(await monitor_bus[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].pan:")
    pprint(await monitor_bus[1].pan.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].width:")
    pprint(await monitor_bus[1].width.get())
    await asyncio.sleep(sleep)
    eq = monitor_bus[1].eq
    print("mixer.general_configuration.monitor_bus[1].eq:")
    pprint(eq)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].eq.on:")
    pprint(await eq.on.get())
    await asyncio.sleep(sleep)
    low_shelf = eq.low_shelf
    print("mixer.general_configuration.monitor_bus[1].eq.low_shelf:")
    pprint(low_shelf)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].eq.low_shelf.gain:")
    pprint(await low_shelf.gain.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].eq.low_shelf.frequency:")
    pprint(await low_shelf.frequency.get())
    await asyncio.sleep(sleep)
    band = eq.band
    print("mixer.general_configuration.monitor_bus[1].eq.band:")
    pprint(band)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].eq.band[1].gain:")
    pprint(await band[1].gain.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].eq.band[1].frequency:")
    pprint(await band[1].frequency.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].eq.band[1].q:")
    pprint(await band[1].q.get())
    await asyncio.sleep(sleep)
    high_shelf = eq.high_shelf
    print("mixer.general_configuration.monitor_bus[1].eq.high_shelf:")
    pprint(high_shelf)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].eq.high_shelf.gain:")
    pprint(await high_shelf.gain.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].eq.high_shelf.frequency:")
    pprint(await high_shelf.frequency.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].limiter:")
    pprint(await monitor_bus[1].limiter.get())
    await asyncio.sleep(sleep)
    delay = monitor_bus[1].delay
    print("mixer.general_configuration.monitor_bus[1].delay:")
    pprint(delay)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].delay.on:")
    pprint(await delay.on.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].delay.meters:")
    pprint(await delay.meters.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].dim:")
    pprint(await monitor_bus[1].dim.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].pfl_dim:")
    pprint(await monitor_bus[1].pfl_dim.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].band_solo_trim:")
    pprint(await monitor_bus[1].band_solo_trim.get())
    await asyncio.sleep(sleep)
    source = monitor_bus[1].source
    print("mixer.general_configuration.monitor_bus[1].source:")
    pprint(source)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].source.level:")
    pprint(await source.level.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].source.mix:")
    pprint(await source.mix.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].source.source:")
    pprint(await source.source.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].fader_level:")
    pprint(await monitor_bus[1].fader_level.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.monitor_bus[1].tags:")
    pprint(await monitor_bus[1].tags.get())
    await asyncio.sleep(sleep)


async def gconf_solo(gconf, sleep):
    """

    :param gconf:
    :return:
    """
    solo = gconf.solo
    print("mixer.general_configuration.solo:")
    pprint(solo)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.mode:")
    pprint(await solo.mode.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.monitor:")
    pprint(await solo.monitor.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.mute:")
    pprint(await solo.mute.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.dim:")
    pprint(await solo.dim.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.mono:")
    pprint(await solo.mono.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.flip:")
    pprint(await solo.flip.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.channel_tap:")
    pprint(await solo.channel_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.bus_tap:")
    pprint(await solo.bus_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.main_tap:")
    pprint(await solo.main_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.matrix_tap:")
    pprint(await solo.matrix_tap.get())
    await asyncio.sleep(sleep)
    source_solo = solo.source_solo
    print("mixer.general_configuration.solo.source_solo:")
    pprint(source_solo)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.source_solo.mode:")
    pprint(await source_solo.mode.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.source_solo.solo:")
    pprint(await source_solo.solo.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.source_solo.source_group:")
    pprint(await source_solo.source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.solo.source_solo.source_index:")
    pprint(await source_solo.source_index.get())
    await asyncio.sleep(sleep)


async def gconf_rta(gconf, sleep):
    """

    :param gconf:
    :return:
    """
    rta = gconf.rta
    print("mixer.general_configuration.rta:")
    pprint(rta)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.source:")
    pprint(await rta.source.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.tap:")
    pprint(await rta.tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.decay:")
    pprint(await rta.decay.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.detector:")
    pprint(await rta.detector.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.range:")
    pprint(await rta.range.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.gain:")
    pprint(await rta.gain.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.autogain:")
    pprint(await rta.autogain.get())
    await asyncio.sleep(sleep)
    rtaeq = rta.eq
    print("mixer.general_configuration.rta.eq:")
    pprint(rtaeq)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.eq.decay:")
    pprint(await rtaeq.decay.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.eq.detector:")
    pprint(await rtaeq.detector.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.eq.range:")
    pprint(await rtaeq.range.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.eq.gain:")
    pprint(await rtaeq.gain.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.rta.eq.autogain:")
    pprint(await rtaeq.autogain.get())
    await asyncio.sleep(sleep)


async def gconf_meters(gconf, sleep):
    """

    :param gconf:
    :return:
    """
    meters = gconf.meters
    print("mixer.general_configuration.meters:")
    pprint(meters)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.scope_source:")
    pprint(await meters.scope_source.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.scope_tap:")
    pprint(await meters.scope_tap.get())
    await asyncio.sleep(sleep)
    fader_section = meters.fader_section
    print("mixer.general_configuration.meters.fader_section:")
    pprint(fader_section)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.fader_section.channel_tap:")
    pprint(await fader_section.channel_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.fader_section.bus_tap:")
    pprint(await fader_section.bus_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.fader_section.main_tap:")
    pprint(await fader_section.main_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.fader_section.matrix_tap:")
    pprint(await fader_section.matrix_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.fader_section.dca_tap:")
    pprint(await fader_section.dca_tap.get())
    await asyncio.sleep(sleep)
    meters_page = meters.page
    print("mixer.general_configuration.meters.page:")
    pprint(meters_page)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.page.channel_tap:")
    pprint(await meters_page.channel_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.page.bus_tap:")
    pprint(await meters_page.bus_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.page.main_tap:")
    pprint(await meters_page.main_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.page.matrix_tap:")
    pprint(await meters_page.matrix_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.page.dca_tap:")
    pprint(await meters_page.dca_tap.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.main_meter:")
    pprint(await meters.main_meter.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.meters.main_position:")
    pprint(await meters.main_position.get())
    await asyncio.sleep(sleep)


async def gconf_talkback(gconf, sleep):
    """

    :param gconf:
    :return:
    """
    talkback = gconf.talkback
    print("mixer.general_configuration.talkback:")
    pprint(talkback)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.assign:")
    pprint(await talkback.assign.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.level:")
    pprint(await talkback.level.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel:")
    pprint(talkback.channel)
    await asyncio.sleep(sleep)
    tb_channel = talkback.channel["A"]
    print("mixer.general_configuration.talkback.channel['A']:")
    pprint(tb_channel)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].on:")
    pprint(await tb_channel.on.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].mode:")
    pprint(await tb_channel.mode.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].monitor_dim:")
    pprint(await tb_channel.monitor_dim.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].bus_dim:")
    pprint(await tb_channel.bus_dim.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].use_send_levels:")
    pprint(await tb_channel.use_send_levels.get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].bus_assign:")
    pprint(tb_channel.bus_assign)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].bus_assign[1-7]:")
    pprint(await tb_channel.bus_assign[1].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.bus_assign[2].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.bus_assign[3].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.bus_assign[4].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.bus_assign[5].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.bus_assign[6].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.bus_assign[7].get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].matrix_assign[1-8]:")
    pprint(await tb_channel.matrix_assign[1].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.matrix_assign[2].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.matrix_assign[3].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.matrix_assign[4].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.matrix_assign[5].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.matrix_assign[6].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.matrix_assign[7].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.matrix_assign[8].get())
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].main_assign:")
    pprint(tb_channel.main_assign)
    await asyncio.sleep(sleep)
    print("mixer.general_configuration.talkback.channel['A'].main_assign[1-4]:")
    pprint(await tb_channel.main_assign[1].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.main_assign[2].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.main_assign[3].get())
    await asyncio.sleep(sleep)
    pprint(await tb_channel.main_assign[4].get())
    await asyncio.sleep(sleep)


async def mixer_system_configuration(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    sysconf = mixer.system_configuration
    print("mixer.system_configuration:")
    pprint(sysconf)
    await asyncio.sleep(sleep)
    consoleconf = mixer.system_configuration.console
    print("mixer.system_configuration.console:")
    pprint(consoleconf)
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.console.name:")
    pprint(await consoleconf.name.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.console.variant:")
    pprint(await consoleconf.variant.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.console.model:")
    pprint(await consoleconf.model.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.log_flags:")
    pprint(await sysconf.log_flags.get())
    await asyncio.sleep(sleep)
    ipconf = sysconf.ip
    print("mixer.system_configuration.ip:")
    pprint(ipconf)
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.ip.mode:")
    pprint(await ipconf.mode.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.ip.address:")
    pprint(await ipconf.address.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.ip.netmask:")
    pprint(await ipconf.netmask.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.ip.gateway:")
    pprint(await ipconf.gateway.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.ip.apply:")
    pprint(await ipconf.apply.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.firmware_version:")
    pprint(await sysconf.firmware_version.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.serial:")
    pprint(await sysconf.serial.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.tcp_lock:")
    pprint(await sysconf.serial.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.mainboard_hardware_version:")
    pprint(await sysconf.mainboard_hardware_version.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.usb_driver_speed:")
    pprint(await sysconf.serial.get())
    await asyncio.sleep(sleep)
    modconf = sysconf.optional_module
    print("mixer.system_configuration.optional_module:")
    pprint(modconf)
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.optional_module.ethernet_mode:")
    pprint(await modconf.ethernet_mode.get())
    await asyncio.sleep(sleep)
    print("mixer.system_configuration.optional_module.installed:")
    pprint(await modconf.installed.get())
    await asyncio.sleep(sleep)


async def mixer_io(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    io = mixer.io
    print("mixer.io:")
    pprint(io)
    await asyncio.sleep(sleep)
    print("mixer.io.global_alt_switch:")
    pprint(await io.global_alt_switch.get())
    await asyncio.sleep(sleep)
    print("mixer.io.global_input_select_override:")
    pprint(await io.global_input_select_override.get())
    await asyncio.sleep(sleep)
    io_input = io.input
    print("mixer.io.input:")
    pprint(io_input)
    await asyncio.sleep(sleep)
    local_in = io.input.local
    print("mixer.io.input.local:")
    pprint(local_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].mode:")
    pprint(await local_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].gain:")
    pprint(await local_in[1].gain.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].phantom:")
    pprint(await local_in[1].phantom.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].mute:")
    pprint(await local_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].invert_polarity:")
    pprint(await local_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].color:")
    pprint(await local_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].name:")
    pprint(await local_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].icon:")
    pprint(await local_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].tags:")
    pprint(await local_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].ha_type:")
    pprint(await local_in[1].ha_type.get())
    await asyncio.sleep(sleep)
    local_in_remote = local_in[1].remote
    print("mixer.io.input.local[1].remote:")
    pprint(local_in_remote)
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].remote.control:")
    pprint(await local_in_remote.control.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].remote.active:")
    pprint(await local_in_remote.active.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].remote.destination:")
    pprint(await local_in_remote.destination.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].remote.customizations_sync:")
    pprint(await local_in_remote.customizations_sync.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.local[1].mute_value:")
    pprint(await local_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    aux_in = io.input.aux
    print("mixer.io.input.aux:")
    pprint(aux_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.aux[1].mode:")
    pprint(await aux_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aux[1].mute:")
    pprint(await aux_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aux[1].invert_polarity:")
    pprint(await aux_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aux[1].color:")
    pprint(await aux_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aux[1].name:")
    pprint(await aux_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aux[1].icon:")
    pprint(await aux_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aux[1].tags:")
    pprint(await aux_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aux[1].mute_value:")
    pprint(await aux_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    aes50_in = io.input.aes50
    print("mixer.io.input.aes50:")
    pprint(aes50_in)
    await asyncio.sleep(sleep)
    aes50_a_in = aes50_in.a
    print("mixer.io.input.aes50.a:")
    pprint(aes50_a_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].mode:")
    pprint(await aes50_a_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].gain:")
    pprint(await aes50_a_in[1].gain.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].phantom:")
    pprint(await aes50_a_in[1].phantom.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].mute:")
    pprint(await aes50_a_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].invert_polarity:")
    pprint(await aes50_a_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].color:")
    pprint(await aes50_a_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].name:")
    pprint(await aes50_a_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].icon:")
    pprint(await aes50_a_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].tags:")
    pprint(await aes50_a_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].ha_type:")
    pprint(await aes50_a_in[1].ha_type.get())
    await asyncio.sleep(sleep)
    aes50_a_in_remote = aes50_a_in[1].remote
    print("mixer.io.input.aes50.a[1].remote:")
    pprint(aes50_a_in_remote)
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].remote.control:")
    pprint(await aes50_a_in_remote.control.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].remote.active:")
    pprint(await aes50_a_in_remote.active.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].remote.destination:")
    pprint(await aes50_a_in_remote.destination.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].remote.customizations_sync:")
    pprint(await aes50_a_in_remote.customizations_sync.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.a[1].mute_value:")
    pprint(await aes50_a_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    aes50_b_in = aes50_in.b
    print("mixer.io.input.aes50.b:")
    pprint(aes50_b_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].mode:")
    pprint(await aes50_b_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].gain:")
    pprint(await aes50_b_in[1].gain.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].phantom:")
    pprint(await aes50_b_in[1].phantom.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].mute:")
    pprint(await aes50_b_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].invert_polarity:")
    pprint(await aes50_b_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].color:")
    pprint(await aes50_b_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].name:")
    pprint(await aes50_b_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].icon:")
    pprint(await aes50_b_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].tags:")
    pprint(await aes50_b_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].ha_type:")
    pprint(await aes50_b_in[1].ha_type.get())
    await asyncio.sleep(sleep)
    aes50_b_in_remote = aes50_b_in[1].remote
    print("mixer.io.input.aes50.b[1].remote:")
    pprint(aes50_b_in_remote)
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].remote.control:")
    pprint(await aes50_b_in_remote.control.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].remote.active:")
    pprint(await aes50_b_in_remote.active.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].remote.destination:")
    pprint(await aes50_b_in_remote.destination.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].remote.customizations_sync:")
    pprint(await aes50_b_in_remote.customizations_sync.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.b[1].mute_value:")
    pprint(await aes50_b_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    aes50_c_in = aes50_in.c
    print("mixer.io.input.aes50.c:")
    pprint(aes50_c_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].mode:")
    pprint(await aes50_c_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].gain:")
    pprint(await aes50_c_in[1].gain.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].phantom:")
    pprint(await aes50_c_in[1].phantom.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].mute:")
    pprint(await aes50_c_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].invert_polarity:")
    pprint(await aes50_c_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].color:")
    pprint(await aes50_c_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].name:")
    pprint(await aes50_c_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].icon:")
    pprint(await aes50_c_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].tags:")
    pprint(await aes50_c_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].ha_type:")
    pprint(await aes50_c_in[1].ha_type.get())
    await asyncio.sleep(sleep)
    aes50_c_in_remote = aes50_c_in[1].remote
    print("mixer.io.input.aes50.c[1].remote:")
    pprint(aes50_c_in_remote)
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].remote.control:")
    pprint(await aes50_c_in_remote.control.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].remote.active:")
    pprint(await aes50_c_in_remote.active.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].remote.destination:")
    pprint(await aes50_c_in_remote.destination.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].remote.customizations_sync:")
    pprint(await aes50_c_in_remote.customizations_sync.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes50.c[1].mute_value:")
    pprint(await aes50_c_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    stage_connect_in = io.input.stage_connect
    print("mixer.io.input.stage_connect:")
    pprint(stage_connect_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.stage_connect[1].mode:")
    pprint(await stage_connect_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.stage_connect[1].mute:")
    pprint(await stage_connect_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.stage_connect[1].invert_polarity:")
    pprint(await stage_connect_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.stage_connect[1].color:")
    pprint(await stage_connect_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.stage_connect[1].name:")
    pprint(await stage_connect_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.stage_connect[1].icon:")
    pprint(await stage_connect_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.stage_connect[1].tags:")
    pprint(await stage_connect_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.stage_connect[1].mute_value:")
    pprint(await stage_connect_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    usb_in = io.input.usb
    print("mixer.io.input.usb:")
    pprint(usb_in)
    await asyncio.sleep(sleep)
    usb_audio_in = usb_in.audio
    print("mixer.io.input.usb.audio:")
    pprint(usb_audio_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.audio[1].mode:")
    pprint(await usb_audio_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.audio[1].mute:")
    pprint(await usb_audio_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.audio[1].invert_polarity:")
    pprint(await usb_audio_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.audio[1].color:")
    pprint(await usb_audio_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.audio[1].name:")
    pprint(await usb_audio_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.audio[1].icon:")
    pprint(await usb_audio_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.audio[1].tags:")
    pprint(await usb_audio_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.audio[1].mute_value:")
    pprint(await usb_audio_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    usb_player_in = usb_in.player
    print("mixer.io.input.usb.player:")
    pprint(usb_player_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.player[1].mode:")
    pprint(await usb_player_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.player[1].mute:")
    pprint(await usb_player_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.player[1].invert_polarity:")
    pprint(await usb_player_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.player[1].color:")
    pprint(await usb_player_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.player[1].name:")
    pprint(await usb_player_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.player[1].icon:")
    pprint(await usb_player_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.player[1].tags:")
    pprint(await usb_player_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.usb.player[1].mute_value:")
    pprint(await usb_player_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    card_in = io.input.card
    print("mixer.io.input.card:")
    pprint(card_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.card[1].mode:")
    pprint(await card_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.card[1].mute:")
    pprint(await card_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.card[1].invert_polarity:")
    pprint(await card_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.card[1].color:")
    pprint(await card_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.card[1].name:")
    pprint(await card_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.card[1].icon:")
    pprint(await card_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.card[1].tags:")
    pprint(await card_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.card[1].mute_value:")
    pprint(await card_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    module_in = io.input.module
    print("mixer.io.input.module:")
    pprint(module_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.module[1].mode:")
    pprint(await module_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.module[1].mute:")
    pprint(await module_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.module[1].invert_polarity:")
    pprint(await module_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.module[1].color:")
    pprint(await module_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.module[1].name:")
    pprint(await module_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.module[1].icon:")
    pprint(await module_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.module[1].tags:")
    pprint(await module_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.module[1].mute_value:")
    pprint(await module_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    aes_in = io.input.aes
    print("mixer.io.input.aes:")
    pprint(aes_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes[1].mode:")
    pprint(await aes_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes[1].mute:")
    pprint(await aes_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes[1].invert_polarity:")
    pprint(await aes_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes[1].color:")
    pprint(await aes_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes[1].name:")
    pprint(await aes_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes[1].icon:")
    pprint(await aes_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes[1].tags:")
    pprint(await aes_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.aes[1].mute_value:")
    pprint(await aes_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    user_in = io.input.user
    print("mixer.io.input.user:")
    pprint(user_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].mode:")
    pprint(await user_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].mute:")
    pprint(await user_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].invert_polarity:")
    pprint(await user_in[1].invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].color:")
    pprint(await user_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].name:")
    pprint(await user_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].icon:")
    pprint(await user_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].tags:")
    pprint(await user_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].mute_value:")
    pprint(await user_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    user_in_source = user_in[1].source
    print("mixer.io.input.user[1].source:")
    pprint(user_in_source)
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].source.group:")
    pprint(await user_in_source.group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].source.index:")
    pprint(await user_in_source.index.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].source.tap_point:")
    pprint(await user_in_source.tap_point.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.user[1].source.mode:")
    pprint(await user_in_source.mode.get())
    await asyncio.sleep(sleep)
    osc_in = io.input.oscillator
    print("mixer.io.input.oscillator:")
    pprint(osc_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.oscillator[1].mode:")
    pprint(await osc_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.oscillator[1].mute:")
    pprint(await osc_in[1].mute.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.oscillator[1].color:")
    pprint(await osc_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.oscillator[1].name:")
    pprint(await osc_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.oscillator[1].icon:")
    pprint(await osc_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.oscillator[1].tags:")
    pprint(await osc_in[1].tags.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.oscillator[1].mute_value:")
    pprint(await osc_in[1].mute_value.get())
    await asyncio.sleep(sleep)
    osc_in_source = osc_in[1].source
    print("mixer.io.input.osc_in[1].source:")
    pprint(osc_in_source)
    await asyncio.sleep(sleep)
    print("mixer.io.input.osc_in[1].source.level:")
    pprint(await osc_in_source.level.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.osc_in[1].source.mode:")
    pprint(await osc_in_source.mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.osc_in[1].source.frequency:")
    pprint(await osc_in_source.frequency.get())
    await asyncio.sleep(sleep)
    bus_in = io.input.bus
    print("mixer.io.input.bus:")
    pprint(bus_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.bus[1].mode:")
    pprint(await bus_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.bus[1].color:")
    pprint(await bus_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.bus[1].name:")
    pprint(await bus_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.bus[1].icon:")
    pprint(await bus_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.bus[1].tags:")
    pprint(await bus_in[1].tags.get())
    await asyncio.sleep(sleep)
    main_in = io.input.main
    print("mixer.io.input.main:")
    pprint(main_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.main[1].mode:")
    pprint(await main_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.main[1].color:")
    pprint(await main_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.main[1].name:")
    pprint(await main_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.main[1].icon:")
    pprint(await main_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.main[1].tags:")
    pprint(await main_in[1].tags.get())
    await asyncio.sleep(sleep)
    matrix_in = io.input.matrix
    print("mixer.io.input.matrix:")
    pprint(matrix_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.matrix[1].mode:")
    pprint(await matrix_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.matrix[1].color:")
    pprint(await matrix_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.matrix[1].name:")
    pprint(await matrix_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.matrix[1].icon:")
    pprint(await matrix_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.matrix[1].tags:")
    pprint(await matrix_in[1].tags.get())
    await asyncio.sleep(sleep)
    fx_send_in = io.input.fx_send
    print("mixer.io.input.fx_send:")
    pprint(fx_send_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.fx_send[1].mode:")
    pprint(await fx_send_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.fx_send[1].color:")
    pprint(await fx_send_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.fx_send[1].name:")
    pprint(await fx_send_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.fx_send[1].icon:")
    pprint(await fx_send_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.fx_send[1].tags:")
    pprint(await fx_send_in[1].tags.get())
    await asyncio.sleep(sleep)
    monitor_in = io.input.monitor
    print("mixer.io.input.monitor:")
    pprint(monitor_in)
    await asyncio.sleep(sleep)
    print("mixer.io.input.monitor[1].mode:")
    pprint(await monitor_in[1].mode.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.monitor[1].color:")
    pprint(await monitor_in[1].color.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.monitor[1].name:")
    pprint(await monitor_in[1].name.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.monitor[1].icon:")
    pprint(await monitor_in[1].icon.get())
    await asyncio.sleep(sleep)
    print("mixer.io.input.monitor[1].tags:")
    pprint(await monitor_in[1].tags.get())
    await asyncio.sleep(sleep)
    io_output = io.output
    print("mixer.io.output:")
    pprint(io_output)
    await asyncio.sleep(sleep)
    local_out = io_output.local
    print("mixer.io.output.local:")
    pprint(local_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.local[1].source_group:")
    pprint(await local_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.local[1].source_index:")
    pprint(await local_out[1].source_index.get())
    await asyncio.sleep(sleep)
    aux_out = io_output.aux
    print("mixer.io.output.aux:")
    pprint(aux_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.aux[1].source_group:")
    pprint(await aux_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.aux[1].source_index:")
    pprint(await aux_out[1].source_index.get())
    await asyncio.sleep(sleep)
    aes50_out = io_output.aes50
    print("mixer.io.output.aes50:")
    pprint(aes50_out)
    await asyncio.sleep(sleep)
    aes50_a_out = aes50_out.a
    print("mixer.io.output.aes50.a:")
    pprint(aes50_a_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.aes50.a[1].source_group:")
    pprint(await aes50_a_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.aes50.a[1].source_index:")
    pprint(await aes50_a_out[1].source_index.get())
    await asyncio.sleep(sleep)
    aes50_b_out = aes50_out.b
    print("mixer.io.output.aes50.b:")
    pprint(aes50_b_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.aes50.b[1].source_group:")
    pprint(await aes50_b_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.aes50.b[1].source_index:")
    pprint(await aes50_b_out[1].source_index.get())
    await asyncio.sleep(sleep)
    aes50_c_out = aes50_out.c
    print("mixer.io.output.aes50.c:")
    pprint(aes50_c_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.aes50.c[1].source_group:")
    pprint(await aes50_c_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.aes50.c[1].source_index:")
    pprint(await aes50_c_out[1].source_index.get())
    await asyncio.sleep(sleep)
    sc_out = io_output.stage_connect
    print("mixer.io.output.stage_connect:")
    pprint(sc_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.stage_connect[1].source_group:")
    pprint(await sc_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.stage_connect[1].source_index:")
    pprint(await sc_out[1].source_index.get())
    await asyncio.sleep(sleep)
    usb_out = io_output.usb
    print("mixer.io.output.usb:")
    pprint(usb_out)
    await asyncio.sleep(sleep)
    usb_audio_out = usb_out.audio
    print("mixer.io.output.usb.audio:")
    pprint(usb_audio_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.usb.audio[1].source_group:")
    pprint(await usb_audio_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.usb.audio[1].source_index:")
    pprint(await usb_audio_out[1].source_index.get())
    await asyncio.sleep(sleep)
    usb_rec_out = usb_out.recorder
    print("mixer.io.output.usb.recorder:")
    pprint(usb_rec_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.usb.recorder[1].source_group:")
    pprint(await usb_rec_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.usb.recorder[1].source_index:")
    pprint(await usb_rec_out[1].source_index.get())
    await asyncio.sleep(sleep)
    card_out = io_output.card
    print("mixer.io.output.card:")
    pprint(card_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.card[1].source_group:")
    pprint(await card_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.card[1].source_index:")
    pprint(await card_out[1].source_index.get())
    await asyncio.sleep(sleep)
    module_out = io_output.module
    print("mixer.io.output.module:")
    pprint(module_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.module[1].source_group:")
    pprint(await module_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.module[1].source_index:")
    pprint(await module_out[1].source_index.get())
    await asyncio.sleep(sleep)
    aes_out = io_output.aes
    print("mixer.io.output.aes:")
    pprint(aes_out)
    await asyncio.sleep(sleep)
    print("mixer.io.output.aes[1].source_group:")
    pprint(await aes_out[1].source_group.get())
    await asyncio.sleep(sleep)
    print("mixer.io.output.aes[1].source_index:")
    pprint(await aes_out[1].source_index.get())
    await asyncio.sleep(sleep)


async def processing_strip_independent(strip, pathstr, sleep):
    """

    :param strip:
    :param pathstr:
    :return:
    """
    print(f"{pathstr}.color:")
    pprint(await strip.color.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.col:")
    pprint(await strip.col.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.name:")
    pprint(await strip.name.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.icon:")
    pprint(await strip.icon.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.scribble_light:")
    pprint(await strip.scribble_light.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.led:")
    pprint(await strip.led.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.mute:")
    pprint(await strip.mute.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.fader:")
    pprint(await strip.fader.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.fdr:")
    pprint(await strip.fdr.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.pan:")
    pprint(await strip.pan.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.width:")
    pprint(await strip.width.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.wid:")
    pprint(await strip.wid.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.solo:")
    pprint(await strip.solo.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.solo_led:")
    pprint(await strip.solo_led.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.sololed:")
    pprint(await strip.sololed.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.monitor:")
    pprint(await strip.monitor.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.mon:")
    pprint(await strip.mon.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.monitor_mode:")
    pprint(await strip.monitor_mode.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.tags:")
    pprint(await strip.tags.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.post_dca_level:")
    pprint(await strip.post_dca_level.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.post_dca_fader:")
    pprint(await strip.post_dca_fader.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.post_group_mute:")
    pprint(await strip.post_group_mute.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.mute_override:")
    pprint(await strip.mute_override.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.muteovr:")
    pprint(await strip.muteovr.get())
    await asyncio.sleep(sleep)


async def processing_strip_eq(strip, pathstr, eq_map, sleep):
    """

    :param strip:
    :param pathstr:
    :param eq_map:
    :return:
    """
    print(f"{pathstr}.eq:")
    strip_eq = strip.eq
    pprint(strip_eq)
    print(f"{pathstr}.eq.enable:")
    pprint(await strip_eq.enable.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.eq.mix:")
    pprint(await strip_eq.mix.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.eq.solo:")
    pprint(await strip_eq.solo.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.eq.solo_band:")
    pprint(await strip_eq.solo_band.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.eq.model:")
    pprint(await strip_eq.model.get())
    await asyncio.sleep(sleep)

    await print_plugins(strip_eq, eq_map, f"{pathstr}.eq", sleep)


async def processing_strip_dynamics_plugin(dyn, pathstr, sleep):
    """

    :param dyn:
    :return:
    """
    print(f"{pathstr}.dynamics.model:")
    pprint(await dyn.model.get())
    await asyncio.sleep(sleep)

    dyn_map = {
        "COMP": Dyn.compexp,
        "EXP": Dyn.compexp,
        "B160": Dyn.b160,
        "B560": Dyn.b560,
        "D241": Dyn.d241,
        "ECL33": Dyn.ecl33,
        "9000C": Dyn.c9000,
        "SBUS": Dyn.sbus,
        "RED3": Dyn.red3,
        "76LA": Multi.la76,
        "LA": Multi.la,
        "F670": Dyn.f670,
        "BLISS": Dyn.bliss,
        "NSTR": Dyn.nstr,
        "WAVE": Multi.wave,
        "RIDE": Multi.ride,
        "2250": Dyn.p2250,
        "L100": Dyn.l100,
        "CMB": Multi.cmb
    }
    await print_plugins(dyn, dyn_map, f"{pathstr}.dynamics", sleep)


async def processing_strip_dynamics(strip, pathstr, sleep):
    """

    :param channel:
    :return:
    """
    print(f"{pathstr}.dynamics:")
    dyn = strip.dynamics
    pprint(dyn)
    print(f"{pathstr}.dynamics.enable:")
    pprint(await dyn.enable.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.on:")
    pprint(await dyn.on.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.mix:")
    pprint(await dyn.mix.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.gain:")
    pprint(await dyn.gain.get())
    await asyncio.sleep(sleep)

    await processing_strip_dynamics_plugin(dyn=dyn, pathstr=pathstr, sleep=sleep)
    await processing_strip_dynamics_xover(dyn=dyn, pathstr=pathstr, sleep=sleep)
    await processing_strip_dynamics_xover(dyn=dyn, pathstr=pathstr, alias=True, sleep=sleep)
    await processing_strip_dynamics_key(dyn=dyn, pathstr=pathstr, sleep=sleep)
    await processing_strip_dynamics_key(dyn=dyn, pathstr=pathstr, alias=True, sleep=sleep)


async def processing_strip_dynamics_xover(dyn, pathstr, sleep, alias=False):
    """

    :param dyn:
    :param pathstr:
    :return:
    """
    if alias:
        print(f"{pathstr}.dynamics.crossover:")
        xover = dyn.crossover
        pprint(xover)
    else:
        print(f"{pathstr}.dynamics.xover:")
        xover = dyn.xover
        pprint(xover)
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.xover.depth:")
    pprint(await xover.depth.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.xover.mode:")
    pprint(await xover.mode.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.xover.freq:")
    pprint(await xover.freq.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.xover.frequency:")
    pprint(await xover.frequency.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.xover.solo:")
    pprint(await xover.solo.get())
    await asyncio.sleep(sleep)


async def processing_strip_dynamics_key(dyn, pathstr, sleep, alias=False):
    """

    :param dyn:
    :param pathstr:
    :return:
    """
    if alias:
        print(f"{pathstr}.dynamics.key:")
        key = dyn.key
        pprint(key)
    else:
        print(f"{pathstr}.dynamics.sidechain:")
        key = dyn.sidechain
        pprint(key)
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.key.filter:")
    filter = key.filter
    pprint(filter)
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.key.filter.type:")
    pprint(await filter.type.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.key.filter.freq:")
    pprint(await filter.freq.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.key.filter.frequency:")
    pprint(await filter.frequency.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.key.filter.q:")
    pprint(await filter.q.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.key.source:")
    pprint(await key.source.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.key.tap:")
    pprint(await key.tap.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dynamics.key.solo:")
    pprint(await key.solo.get())
    await asyncio.sleep(sleep)


async def processing_strip_insert(strip, pathstr, sleep, path="pre", alias=False):
    if alias:
        print(f"{pathstr}.{path}ins:")
        pre = strip.preins
        pprint(pre)
        await asyncio.sleep(sleep)
    else:
        print(f"{pathstr}.{path}_insert:")
        pre = strip.pre_insert
        pprint(pre)
        await asyncio.sleep(sleep)
    print(f"{pathstr}.{path}_insert.on:")
    pprint(await pre.on.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{path}_insert.enable:")
    pprint(await pre.enable.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{path}_insert.fx_processor:")
    pprint(await pre.fx_processor.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{path}_insert.ins:")
    pprint(await pre.ins.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{path}_insert.insert:")
    pprint(await pre.insert.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{path}_insert.status:")
    pprint(await pre.status.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{path}_insert.stat:")
    pprint(await pre.stat.get())
    await asyncio.sleep(sleep)


async def mixer_channel(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    channel = mixer.channel
    print("mixer.channel:")
    pprint(channel)
    await asyncio.sleep(sleep)

    await channel_input(channel=channel[1], sleep=sleep)
    await channel_filter(channel=channel[39], sleep=sleep)

    print("mixer.channel[39].custom_link:")
    pprint(await channel[39].custom_link.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].clink:")
    pprint(await channel[39].clink.get())
    await asyncio.sleep(sleep)

    await processing_strip_independent(channel[39], "mixer.channel[39]", sleep)

    print("mixer.channel[39].solo_safe:")
    pprint(await channel[39].solo_safe.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].solosafe:")
    pprint(await channel[39].solosafe.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].process_order:")
    pprint(await channel[39].process_order.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].proc:")
    pprint(await channel[39].proc.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].pretap:")
    pprint(await channel[39].pretap.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].ptap:")
    pprint(await channel[39].ptap.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presolo:")
    pprint(await channel[39].presolo.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].peq:")
    pprint(channel[39].peq)
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq:")
    channel_presend_eq = channel[39].presend_eq
    pprint(channel_presend_eq)
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq.enable:")
    pprint(await channel_presend_eq.enable.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq.on:")
    pprint(await channel_presend_eq.on.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq.band:")
    channel_presend_eq_band = channel_presend_eq.band
    pprint(channel_presend_eq_band)
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq.band[1]:")
    pprint(channel_presend_eq_band[1])
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq.band[1].gain:")
    pprint(await channel_presend_eq_band[1].gain.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq.band[1].g:")
    pprint(await channel_presend_eq_band[1].g.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq.band[1].frequency:")
    pprint(await channel_presend_eq_band[1].frequency.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq.band[1].f:")
    pprint(await channel_presend_eq_band[1].f.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].presend_eq.band[1].q:")
    pprint(await channel_presend_eq_band[1].q.get())
    await asyncio.sleep(sleep)
    await channel_gate(channel=channel, sleep=sleep)
    await channel_eq(channel=channel, sleep=sleep)
    await processing_strip_dynamics(strip=channel[39], pathstr="mixer.channel[39]", sleep=sleep)
    await processing_strip_insert(strip=channel[39], pathstr="mixer.channel[39]", sleep=sleep)
    await processing_strip_insert(
        strip=channel[39], pathstr="mixer.channel[39]", alias=True, sleep=sleep
    )
    await channel_mains(channel=channel[39], sleep=sleep)
    await channel_mains(channel=channel[39], alias=True, sleep=sleep)
    await channel_sends(channel=channel[39], endpoint="bus_send", sleep=sleep)
    await channel_sends(channel=channel[39], endpoint="send", sleep=sleep)
    await channel_sends(channel=channel[39], endpoint="bus", sleep=sleep)
    await channel_sends(channel=channel[39], endpoint="matrix_send", sleep=sleep)
    await channel_sends(channel=channel[39], endpoint="matrix", sleep=sleep)
    await channel_sends(channel=channel[39], endpoint="mtx", sleep=sleep)
    await channel_sends(channel=channel[39], endpoint="mx", sleep=sleep)
    await channel_sends(channel=channel[39], endpoint="mx", sleep=sleep)
    print("mixer.channel[39].tap_width:")
    pprint(await channel[39].tap_width.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].tapwid:")
    pprint(await channel[39].tapwid.get())
    await asyncio.sleep(sleep)
    await channel_postinsert(channel=channel, sleep=sleep)
    await channel_postinsert(channel=channel, alias=True, sleep=sleep)


async def channel_input(channel, sleep, type_path="channel[1]"):
    """

    :param channel:
    :return:
    """
    channel_in = channel.input
    print(f"mixer.{type_path}.input:")
    pprint(channel_in)
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.set:")
    pprint(channel_in.set)
    await asyncio.sleep(sleep)
    channel_in_set = channel_in.settings
    print(f"mixer.{type_path}.input.settings:")
    pprint(channel_in_set)
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.mode:")
    pprint(await channel_in_set.mode.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.input_mode:")
    pprint(await channel_in_set.input_mode.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.alt_switch_source:")
    pprint(await channel_in_set.alt_switch_source.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.auto_source:")
    pprint(await channel_in_set.auto_source.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.srcauto:")
    pprint(await channel_in_set.srcauto.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.alt_switch:")
    pprint(await channel_in_set.alt_switch.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.alt_source:")
    pprint(await channel_in_set.alt_source.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.alt_src:")
    pprint(await channel_in_set.alt_src.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.altsrc:")
    pprint(await channel_in_set.altsrc.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.invert_polarity:")
    pprint(await channel_in_set.invert_polarity.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.phase_invert:")
    pprint(await channel_in_set.phase_invert.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.inv:")
    pprint(await channel_in_set.inv.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.trim:")
    pprint(await channel_in_set.trim.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.input_trim:")
    pprint(await channel_in_set.input_trim.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.balance:")
    pprint(await channel_in_set.balance.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.input_balance:")
    pprint(await channel_in_set.input_balance.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.bal:")
    pprint(await channel_in_set.bal.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.gain:")
    pprint(await channel_in_set.gain.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.input_gain:")
    pprint(await channel_in_set.input_gain.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.g:")
    pprint(await channel_in_set.g.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.phantom:")
    pprint(await channel_in_set.phantom.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.phantom_power:")
    pprint(await channel_in_set.phantom_power.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.input_phantom_power:")
    pprint(await channel_in_set.input_phantom_power.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.vph:")
    pprint(await channel_in_set.vph.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.delay:")
    pprint(await channel_in_set.delay.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.settings.input_delay:")
    pprint(await channel_in_set.input_delay.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source:")
    channel_in_src = channel_in.source
    pprint(channel_in_src)
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.conn:")
    pprint(channel_in.conn)
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.con:")
    pprint(channel_in.con)
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.connection:")
    pprint(channel_in.connection)
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.main:")
    channel_in_src_main = channel_in_src.main
    pprint(channel_in_src_main)
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.main.group:")
    pprint(await channel_in_src_main.group.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.main.grp:")
    pprint(await channel_in_src_main.grp.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.main.index:")
    pprint(await channel_in_src_main.index.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.main.group_index:")
    pprint(await channel_in_src_main.group_index.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.main.input:")
    pprint(await channel_in_src_main.input.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.alt:")
    channel_in_src_alt = channel_in_src.alt
    pprint(channel_in_src_alt)
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.alt.group:")
    pprint(await channel_in_src_alt.group.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.alt.grp:")
    pprint(await channel_in_src_alt.grp.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.alt.index:")
    pprint(await channel_in_src_alt.index.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.alt.group_index:")
    pprint(await channel_in_src_alt.group_index.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.input.source.alt.input:")
    pprint(await channel_in_src_alt.input.get())
    await asyncio.sleep(sleep)


async def channel_filter(channel, sleep):
    """

    :param channel:
    :return:
    """
    print("mixer.channel[39].flt:")
    pprint(channel.flt)
    await asyncio.sleep(sleep)
    print("mixer.channel[39].filter:")
    channel_flt = channel.filter
    pprint(channel_flt)
    await asyncio.sleep(sleep)
    print("mixer.channel[39].filter.model:")
    pprint(await channel_flt.model.get())
    await asyncio.sleep(sleep)
    await channel_flt.model.set("TILT")
    await asyncio.sleep(sleep)
    print("mixer.channel[39].filter.model:")
    pprint(await channel_flt.model.get())
    await asyncio.sleep(sleep)

    filter_map = {
        "Tilt Filter": Filter.tilt,
        "Maxer Filter": Filter.max,
        "AP1": Filter.ap1,
        "AP2": Filter.ap2
    }
    await print_plugins(channel_flt, filter_map, "mixer.channel[39].filter", sleep=sleep)


async def channel_gate(channel, sleep):
    """

    :param channel:
    :return:
    """
    print("mixer.channel[39].gate:")
    channel_gate = channel[39].gate
    pprint(channel_gate)
    await asyncio.sleep(sleep)
    print("mixer.channel[39].gate.enable:")
    pprint(await channel_gate.enable.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].gate.on:")
    pprint(await channel_gate.on.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].gate.model:")
    pprint(await channel_gate.model.get())
    await asyncio.sleep(sleep)

    gate_map = {
        "GATE": Gate.gate,
        "DUCK": Gate.duck,
        "E88": Gate.e88,
        "9000G": Gate.g9000,
        "D241": Gate.d241,
        "DS902": Gate.ds902,
        "WAVE": Multi.wave,
        "DEQ": Gate.deq,
        "WARM": Gate.warm,
        "76LA": Multi.la76,
        "LA": Multi.la,
        "RIDE": Multi.ride,
        "PSE": Multi.pse,
        "CMB": Multi.cmb
    }
    await print_plugins(channel_gate, gate_map, "mixer.channel[39].gate", sleep=sleep)

    await channel_gate_sidechain(channel_gate=channel_gate, sleep=sleep)


async def channel_gate_sidechain(channel_gate, sleep):
    """

    :param channel_gate:
    :return:
    """
    print("mixer.channel[39].gate.sidechain")
    channel_gate_sc = channel_gate.sidechain
    pprint(channel_gate_sc)
    await asyncio.sleep(sleep)
    print("mixer.channel[39].gate.sidechain.type:")
    pprint(await channel_gate_sc.type.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].gate.sidechain.frequency:")
    pprint(await channel_gate_sc.frequency.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].gate.sidechain.q:")
    pprint(await channel_gate_sc.q.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].gate.sidechain.source:")
    pprint(await channel_gate_sc.source.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].gate.sidechain.solo:")
    pprint(await channel_gate_sc.solo.get())
    await asyncio.sleep(sleep)


async def channel_eq(channel, sleep):
    """

    :param channel:
    :return:
    """
    eq_map = {
        "STD": EQ.std,
        "SOUL": EQ.soul,
        "E88": EQ.e88,
        "E84": EQ.e84,
        "F110": EQ.f110,
        "PULSAR": EQ.pulsar,
        "MACH4": EQ.mach4
    }
    await processing_strip_eq(channel[39], "mixer.channel[39]", eq_map, sleep=sleep)


async def channel_mains(channel, sleep, type_path="channel[39]", alias=False):
    """

    :param channel:
    :return:
    """

    if alias:
        print(f"mixer.{type_path}.main_send:")
        pprint(channel.main_send)
        await asyncio.sleep(sleep)
        print(f"mixer.{type_path}.main_send[1]:")
        main_send = channel.main_send[1]
        pprint(main_send)
        await asyncio.sleep(sleep)
    else:
        print(f"mixer.{type_path}.main:")
        pprint(channel.main)
        await asyncio.sleep(sleep)
        print(f"mixer.{type_path}.main[1]:")
        main_send = channel.main[1]
        pprint(main_send)
        await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.main_send[1].on:")
    pprint(await main_send.on.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.main_send[1].enable:")
    pprint(await main_send.enable.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.main_send[1].level:")
    pprint(await main_send.level.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.main_send[1].lvl:")
    pprint(await main_send.lvl.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.main_send[1].pre:")
    pprint(await main_send.pre.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.main_send[1].pre_fader:")
    pprint(await main_send.pre_fader.get())
    await asyncio.sleep(sleep)


async def channel_sends(channel, endpoint: str, sleep, type_path="channel[39]"):
    """

    :param channel:
    :param endpoint:
    :return:
    """
    print(f"mixer.{type_path}.{endpoint}:")
    pprint(getattr(channel, endpoint))
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1]:")
    send = getattr(channel, endpoint)[1]
    pprint(send)
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].on:")
    pprint(await send.on.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].enable:")
    pprint(await send.enable.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].level:")
    pprint(await send.level.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].lvl:")
    pprint(await send.lvl.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].ignore_channel_mute:")
    pprint(await send.ignore_channel_mute.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].pon:")
    pprint(await send.pon.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].pre_always_on:")
    pprint(await send.pre_always_on.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].mode:")
    pprint(await send.mode.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].link_send_pan_to_channel_pan:")
    pprint(await send.link_send_pan_to_channel_pan.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].plink:")
    pprint(await send.plink.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].pan_link:")
    pprint(await send.pan_link.get())
    await asyncio.sleep(sleep)
    print(f"mixer.{type_path}.{endpoint}[1].pan:")
    pprint(await send.pan.get())
    await asyncio.sleep(sleep)


async def channel_postinsert(channel, sleep, alias=False):
    """

    :param channel_dyn:
    :return:
    """
    if alias:
        print("mixer.channel[39].postins:")
        post = channel[39].postins
        pprint(post)
        await asyncio.sleep(sleep)
    else:
        print("mixer.channel[39].post_insert:")
        post = channel[39].post_insert
        pprint(post)
        await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.on:")
    pprint(await post.on.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.enable:")
    pprint(await post.enable.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.mode:")
    pprint(await post.mode.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.fx_processor:")
    pprint(await post.fx_processor.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.ins:")
    pprint(await post.ins.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.insert:")
    pprint(await post.insert.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.autogain_weight:")
    pprint(await post.autogain_weight.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.w:")
    pprint(await post.w.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.weight:")
    pprint(await post.weight.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.status:")
    pprint(await post.status.get())
    await asyncio.sleep(sleep)
    print("mixer.channel[39].post_insert.stat:")
    pprint(await post.stat.get())
    await asyncio.sleep(sleep)


async def mixer_aux(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    aux = mixer.aux
    print("mixer.aux:")
    pprint(aux)
    await asyncio.sleep(sleep)

    await channel_input(channel=aux[1], type_path="aux[1]", sleep=sleep)

    print("mixer.aux[1].custom_link:")
    pprint(await aux[1].custom_link.get())
    await asyncio.sleep(sleep)
    print("mixer.aux[1].clink:")
    pprint(await aux[1].clink.get())
    await asyncio.sleep(sleep)

    await processing_strip_independent(aux[1], "mixer.aux[1]", sleep=sleep)

    print("mixer.aux[1].solo_safe:")
    pprint(await aux[1].solo_safe.get())
    await asyncio.sleep(sleep)
    print("mixer.aux[1].solosafe:")
    pprint(await aux[1].solosafe.get())
    await asyncio.sleep(sleep)

    await aux_eq(aux=aux[1], sleep=sleep)
    await aux_dynamics(aux=aux[1], sleep=sleep)
    await processing_strip_insert(strip=aux[1], pathstr="mixer.aux[1]", sleep=sleep)
    await processing_strip_insert(strip=aux[1], pathstr="mixer.aux[1]", alias=True, sleep=sleep)
    await channel_mains(channel=aux[1], type_path="aux[1]", sleep=sleep)
    await channel_mains(channel=aux[1], type_path="aux[1]", alias=True, sleep=sleep)
    await channel_sends(channel=aux[1], type_path="aux[1]", endpoint="bus_send", sleep=sleep)
    await channel_sends(channel=aux[1], type_path="aux[1]", endpoint="send", sleep=sleep)
    await channel_sends(channel=aux[1], type_path="aux[1]", endpoint="bus", sleep=sleep)
    await channel_sends(channel=aux[1], type_path="aux[1]", endpoint="matrix_send", sleep=sleep)
    await channel_sends(channel=aux[1], type_path="aux[1]", endpoint="matrix", sleep=sleep)
    await channel_sends(channel=aux[1], type_path="aux[1]", endpoint="mtx", sleep=sleep)
    await channel_sends(channel=aux[1], type_path="aux[1]", endpoint="mx", sleep=sleep)
    await channel_sends(channel=aux[1], type_path="aux[1]", endpoint="mx", sleep=sleep)


async def aux_eq(aux, sleep):
    """

    :param aux:
    :return:
    """
    print("mixer.aux[1].eq:")
    a_eq = aux.eq
    pprint(a_eq)
    print("mixer.aux[1].eq.enable:")
    pprint(await a_eq.enable.get())
    await asyncio.sleep(sleep)
    print("mixer.aux[1].eq.mix:")
    pprint(await a_eq.mix.get())
    await asyncio.sleep(sleep)
    print("mixer.aux[1].eq.solo:")
    pprint(await a_eq.solo.get())
    await asyncio.sleep(sleep)
    print("mixer.aux[1].eq.solo_band:")
    pprint(await a_eq.solo_band.get())
    await asyncio.sleep(sleep)
    print("mixer.aux[1].eq.model:")
    pprint(await a_eq.model.get())
    await asyncio.sleep(sleep)

    eq_map = {
        "STD": EQ.std,
        "SOUL": EQ.soul,
        "E88": EQ.e88,
        "E84": EQ.e84,
        "F110": EQ.f110,
        "PULSAR": EQ.pulsar
    }
    await print_plugins(a_eq, eq_map, "mixer.aux[1].eq", sleep=sleep)


async def aux_dynamics(aux, sleep):
    """

    :param aux:
    :return:
    """
    print("mixer.aux[1].dynamics:")
    aux_dyn = aux.dynamics
    pprint(aux_dyn)
    print("mixer.aux[1].dynamics.enable:")
    pprint(await aux_dyn.enable.get())
    await asyncio.sleep(sleep)
    print("mixer.aux[1].dynamics.on:")
    pprint(await aux_dyn.on.get())
    await asyncio.sleep(sleep)
    print("mixer.aux[1].dynamics.power:")
    pprint(await aux_dyn.power.get())
    await asyncio.sleep(sleep)
    await Multi.cmb(plugin=aux_dyn, pathstr="mixer.aux[1].dynamics", sleep=sleep)


async def output_input(out, pathstr, sleep):
    """

    :param out:
    :return:
    """
    out_in = out.input
    print(f"{pathstr}.input:")
    pprint(out_in)
    await asyncio.sleep(sleep)
    print(f"{pathstr}.input.set:")
    pprint(out_in.set)
    await asyncio.sleep(sleep)
    out_in_set = out_in.settings
    print(f"{pathstr}.input.settings:")
    pprint(out_in_set)
    await asyncio.sleep(sleep)
    print(f"{pathstr}.input.settings.invert_polarity:")
    pprint(await out_in_set.invert_polarity.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.input.settings.phase_invert:")
    pprint(await out_in_set.phase_invert.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.input.settings.inv:")
    pprint(await out_in_set.inv.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.input.settings.trim:")
    pprint(await out_in_set.trim.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.input.settings.input_trim:")
    pprint(await out_in_set.input_trim.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.input.settings.balance:")
    pprint(await out_in_set.balance.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.input.settings.input_balance:")
    pprint(await out_in_set.input_balance.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.input.settings.bal:")
    pprint(await out_in_set.bal.get())
    await asyncio.sleep(sleep)


async def output_common(out, pathstr, sleep):
    """

    :param out:
    :param pathstr:
    :return:
    """
    await output_input(out, pathstr, sleep=sleep)
    await processing_strip_independent(out, pathstr, sleep=sleep)
    print(f"{pathstr}.mono:")
    pprint(await out.mono.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.busmono:")
    pprint(await out.mono.get())
    await asyncio.sleep(sleep)

    await output_eq(out, pathstr, sleep=sleep)
    await processing_strip_dynamics(strip=out, pathstr=pathstr, sleep=sleep)
    await processing_strip_insert(strip=out, pathstr=pathstr, sleep=sleep)
    await processing_strip_insert(strip=out, pathstr=pathstr, alias=True, sleep=sleep)
    await processing_strip_insert(strip=out, pathstr=pathstr, path="post", sleep=sleep)
    await processing_strip_insert(strip=out, pathstr=pathstr, path="post", alias=True, sleep=sleep)

    print(f"{pathstr}.delay:")
    pprint(await out.delay.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.dly:")
    pprint(await out.dly.get())
    await asyncio.sleep(sleep)


async def output_eq(out, pathstr, sleep):
    """

    :param out:
    :param pathstr:
    :return:
    """
    eq_map = {
        "STD": EQ.std,
        "SOUL": EQ.soul,
        "E88": EQ.e88,
        "E84": EQ.e84,
        "F110": EQ.f110,
        "PULSAR": EQ.pulsar,
        "PIA": EQ.pia
    }
    await processing_strip_eq(out, pathstr, eq_map, sleep=sleep)


async def output_send(out, pathstr, send_attr, sleep, send_aliases = []):
    """

    :param out:
    :param pathstr:
    :param send_attr:
    :param send_aliases:
    :return:
    """
    for send_alias in send_aliases:
        print(f"{pathstr}.{send_alias}:")
        pprint(getattr(out, send_alias))
        await asyncio.sleep(sleep)
    print(f"{pathstr}.{send_attr}:")
    pprint(getattr(out, send_attr))
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{send_attr}[1]:")
    send_method = getattr(out, send_attr)[1]
    pprint(send_method)
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{send_attr}[1].on")
    pprint(await send_method.on.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{send_attr}[1].enable")
    pprint(await send_method.enable.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{send_attr}[1].level")
    pprint(await send_method.level.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{send_attr}[1].lvl")
    pprint(await send_method.lvl.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{send_attr}[1].pre")
    pprint(await send_method.pre.get())
    await asyncio.sleep(sleep)
    print(f"{pathstr}.{send_attr}[1].pre_fader")
    pprint(await send_method.pre_fader.get())
    await asyncio.sleep(sleep)


async def mixer_bus(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    print("mixer.bus_send:")
    pprint(mixer.bus_send)
    print("mixer.send:")
    pprint(mixer.send)
    print("mixer.bus:")
    pprint(mixer.bus)
    bus = mixer.bus[1]
    print("mixer.bus[1]:")
    pprint(bus)
    await asyncio.sleep(sleep)
    await output_common(bus, "mixer.bus[1]", sleep=sleep)
    await output_send(bus, "mixer.bus[1]", "bus_send", send_aliases=[ "send", "bus" ], sleep=sleep)
    await output_send(bus, "mixer.bus[1]", "main_send", send_aliases=[ "main" ], sleep=sleep)
    await output_send(
        bus, "mixer.bus[1]", "matrix_send",
        send_aliases=[ "matrix", "mtx", "mtx_send", "mx", "mx_send" ], sleep=sleep
    )


async def mixer_main(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    print("mixer.main_send:")
    pprint(mixer.main_send)
    print("mixer.main:")
    pprint(mixer.main)
    mains = mixer.main[1]
    print("mixer.main[1]:")
    pprint(mains)
    await asyncio.sleep(sleep)
    await output_common(mains, "mixer.main[1]", sleep=sleep)
    await output_send(
        mains, "mixer.main[1]", "matrix_send",
        send_aliases=[ "matrix", "mtx", "mtx_send", "mx", "mx_send" ], sleep=sleep
    )


async def mixer_matrix(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    print("mixer.matrix_send:")
    pprint(mixer.matrix_send)
    print("mixer.mtx:")
    pprint(mixer.mtx)
    print("mixer.mtx_send:")
    pprint(mixer.mtx_send)
    print("mixer.mx:")
    pprint(mixer.mx)
    print("mixer.mx_send:")
    pprint(mixer.mx_send)
    print("mixer.matrix:")
    pprint(mixer.matrix)
    matrix = mixer.matrix[1]
    print("mixer.matrix[1]:")
    pprint(matrix)
    await asyncio.sleep(sleep)
    await output_common(matrix, "mixer.matrix[1]", sleep=sleep)
    await matrix_direct_input(matrix, sleep=sleep)


async def matrix_direct_input(matrix, sleep):
    """

    :param matrix:
    :return:
    """
    print("mixer.matrix[1].dir:")
    pprint(matrix.dir)
    print("mixer.matrix[1].direct_input_signal:")
    pprint(matrix.direct_input_signal)
    print("mixer.matrix[1].direct_in:")
    pprint(matrix.direct_in)
    print("mixer.matrix[1].direct_input:")
    direct_input = matrix.direct_input
    pprint(direct_input)
    print("mixer.matrix[1].direct_input.on:")
    pprint(await direct_input.on.get())
    await asyncio.sleep(sleep)
    print("mixer.matrix[1].direct_input.enable:")
    pprint(await direct_input.enable.get())
    await asyncio.sleep(sleep)
    print("mixer.matrix[1].direct_input.level:")
    pprint(await direct_input.level.get())
    await asyncio.sleep(sleep)
    print("mixer.matrix[1].direct_input.lvl:")
    pprint(await direct_input.lvl.get())
    await asyncio.sleep(sleep)
    print("mixer.matrix[1].direct_input.invert_polarity:")
    pprint(await direct_input.invert_polarity.get())
    await asyncio.sleep(sleep)
    print("mixer.matrix[1].direct_input.inv:")
    pprint(await direct_input.inv.get())
    await asyncio.sleep(sleep)
    print("mixer.matrix[1].direct_input.phase_invert:")
    pprint(await direct_input.phase_invert.get())
    await asyncio.sleep(sleep)
    print("mixer.matrix[1].direct_input.input_source:")
    pprint(await direct_input.input_source.get())
    await asyncio.sleep(sleep)
    print("mixer.matrix[1].direct_input.input:")
    pprint(await direct_input.input.get())
    await asyncio.sleep(sleep)
    print("mixer.matrix[1].direct_input.source:")
    pprint(await direct_input.source.get())
    await asyncio.sleep(sleep)


async def mixer_dca(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    print("mixer.dca:")
    pprint(mixer.dca)
    dca = mixer.dca[1]
    print("mixer.dca[1]:")
    pprint(dca)
    await asyncio.sleep(sleep)
    print("mixer.dca[1].name:")
    pprint(await dca.name.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].color:")
    pprint(await dca.color.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].col:")
    pprint(await dca.col.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].icon:")
    pprint(await dca.icon.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].scribble_light:")
    pprint(await dca.scribble_light.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].led:")
    pprint(await dca.led.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].mute:")
    pprint(await dca.mute.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].fader:")
    pprint(await dca.fader.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].fdr:")
    pprint(await dca.fdr.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].solo:")
    pprint(await dca.solo.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].solo_led:")
    pprint(await dca.solo_led.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].sololed:")
    pprint(await dca.sololed.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].monitor:")
    pprint(await dca.monitor.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].mon:")
    pprint(await dca.mon.get())
    await asyncio.sleep(sleep)
    print("mixer.dca[1].monitor_mode:")
    pprint(await dca.monitor_mode.get())
    await asyncio.sleep(sleep)


async def mixer_mutegroup(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    print("mixer.mutegroup:")
    pprint(mixer.mutegroup)
    print("mixer.mgrp:")
    pprint(mixer.mgrp)
    print("mixer.mute_group:")
    pprint(mixer.mute_group)
    mgrp = mixer.mute_group[1]
    print("mixer.mute_group[1]:")
    pprint(mgrp)
    await asyncio.sleep(sleep)
    print("mixer.mute_group[1].name:")
    pprint(await mgrp.name.get())
    await asyncio.sleep(sleep)
    print("mixer.mute_group[1].mute:")
    pprint(await mgrp.mute.get())
    await asyncio.sleep(sleep)


async def mixer_fx(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    print("mixer.fx")
    pprint(mixer.fx)
    await asyncio.sleep(sleep)
    print("mixer.fx[1]")
    fx = mixer.fx[1]
    pprint(fx)
    await asyncio.sleep(sleep)
    print("mixer.fx[1].mix")
    pprint(await fx.mix.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].fxmix")
    pprint(await fx.fxmix.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].source")
    pprint(await fx.source.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].src")
    pprint(await fx.src.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].esource")
    pprint(await fx.esource.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].esrc")
    pprint(await fx.esrc.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].input_source")
    pprint(await fx.input_source.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].input")
    pprint(await fx.input.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].mode")
    pprint(await fx.mode.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].emode")
    pprint(await fx.emode.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].input_mode")
    pprint(await fx.input_mode.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].channel")
    pprint(await fx.channel.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].inserted_channel")
    pprint(await fx.inserted_channel.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].a_chn")
    pprint(await fx.a_chn.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].position")
    pprint(await fx.position.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].inserted_position")
    pprint(await fx.inserted_position.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].channel_insert")
    pprint(await fx.channel_insert.get())
    await asyncio.sleep(sleep)
    print("mixer.fx[1].a_pos")
    pprint(await fx.a_pos.get())
    await asyncio.sleep(sleep)

    await mixer_fx_plugin(fx=fx, sleep=sleep)


async def mixer_fx_plugin(fx, sleep):
    """

    :param dyn:
    :return:
    """
    print("mixer.fx[1].model:")
    pprint(await fx.model.get())
    await asyncio.sleep(sleep)

    fx_map = {
        "NONE": FX.none,
        "EXT": FX.ext,
        "HALL": FX.hall,
        "ROOM": FX.room,
        "CHAMBER": FX.chamber,
        "PLATE": FX.plate,
        "CONCERT": FX.concert,
        "AMBI": FX.ambi,
        "V-ROOM": FX.vroom,
        "V-REV": FX.vrev,
        "V-PLATE": FX.vplate,
        "GATED": FX.gated,
        "REVERSE": FX.reverse,
        "DEL/REV": FX.delrev,
        "SHIMMER": FX.shimmer,
        "SPRING": FX.spring,
        "DIMCRS": FX.dimcrs,
        "CHORUS": FX.chorus,
        "FLANGER": FX.flanger,
        "ST-DL": FX.stdl,
        "TAP-DL": FX.tapdl,
        "TAPE-DL": FX.tapedl,
        "OILCAN": FX.oilcan,
        "BBD-DL": FX.bbddl,
        "PITCH": FX.pitch,
        "D-PITCH": FX.dpitch,
        "VSS3": FX.vss3,
        "BPLATE": FX.bplate,
        "GEQ": FX.geq,
        "PIA": FX.pia,
        "DOUBLE": FX.double,
        "PCORR": FX.pcorr,
        "LIMITER": FX.limiter,
        "DE-S2": FX.des2,
        "ENHANCE": FX.enhance,
        "EXCITER": FX.exciter,
        "P-BASS": FX.pbass,
        "ROTARY": FX.rotary,
        "PHASER": FX.phaser,
        "PANNER": FX.panner,
        "TAPE": FX.tape,
        "MOOD": FX.mood,
        "SUB": FX.sub,
        "RACKAMP": FX.rackamp,
        "UKROCK": FX.ukrock,
        "ANGEL": FX.angel,
        "JAZZC": FX.jazzc,
        "DELUXE": FX.deluxe,
        "BODY": FX.body,
        "SOUL": EQ.soul,
        "E88": EQ.e88,
        "E84": EQ.e84,
        "F110": EQ.f110,
        "PULSAR": EQ.pulsar,
        "MACH4": EQ.mach4,
        "C5-CMB": FX.c5cmb,
        "SUB-M": FX.subm,
        "V-IMG": FX.vimg,
        "SPKMAN": FX.spkman,
        "DEQ3": FX.deq3,
        "*EVEN*": FX.even,
        "*SOUL*": FX.soulch,
        "*VINTAGE*": FX.vintage,
        "*BUS*": FX.bus,
        "*MASTER*": FX.master,
    }
    await print_plugins(fx, fx_map, "mixer.fx[1]", sleep=sleep)


async def mixer_cards(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    print(f"mixer.cards:")
    cards = mixer.cards
    pprint(cards)
    await asyncio.sleep(sleep)
    print("mixer.cards.type")
    pprint(await cards.type.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.version")
    pprint(await cards.version.get())
    await asyncio.sleep(sleep)
    print(f"mixer.cards.w_live:")
    w_live = cards.w_live
    pprint(w_live)
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live.sd_link")
    pprint(await w_live.sd_link.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live.act_link")
    pprint(await w_live.act_link.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live.battery_status")
    pprint(await w_live.battery_status.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live.auto_input")
    pprint(await w_live.auto_input.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live.show_meters")
    pprint(await w_live.show_meters.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live.auto_stop")
    pprint(await w_live.auto_stop.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live.auto_play")
    pprint(await w_live.auto_play.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live.auto_record")
    pprint(await w_live.auto_record.get())
    await asyncio.sleep(sleep)
    print(f"mixer.cards.w_live[1]:")
    w_live1 = cards.w_live[1]
    pprint(w_live1)
    await asyncio.sleep(sleep)
    print(f"mixer.cards.w_live[1].control:")
    w_livectrl = w_live1.control
    pprint(w_livectrl)
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.control")
    pprint(await w_livectrl.control.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.open_session")
    pprint(await w_livectrl.open_session.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.edit_marker")
    pprint(await w_livectrl.edit_marker.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.goto_marker")
    pprint(await w_livectrl.goto_marker.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.delete_marker")
    pprint(await w_livectrl.delete_marker.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.delete_session")
    pprint(await w_livectrl.delete_session.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.stime")
    pprint(await w_livectrl.stime.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.name_session")
    pprint(await w_livectrl.name_session.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.set_marker")
    pprint(await w_livectrl.set_marker.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].control.format_sd_card")
    pprint(await w_livectrl.format_sd_card.get())
    await asyncio.sleep(sleep)
    print(f"mixer.cards.w_live[1].config:")
    w_livecfg = w_live1.config
    pprint(w_livecfg)
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].config.rec_tracks")
    pprint(await w_livecfg.rec_tracks.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].config.play_mode")
    pprint(await w_livecfg.play_mode.get())
    await asyncio.sleep(sleep)
    print(f"mixer.cards.w_live[1].status:")
    w_livestat = w_live1.status
    pprint(w_livestat)
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.state")
    pprint(await w_livestat.state.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.current_time")
    pprint(await w_livestat.current_time.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.session_list")
    pprint(await w_livestat.session_list.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.marker_list")
    pprint(await w_livestat.marker_list.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.session_name_list")
    pprint(await w_livestat.session_name_list.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.sessions")
    pprint(await w_livestat.sessions.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.markers")
    pprint(await w_livestat.markers.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.session_length")
    pprint(await w_livestat.session_length.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.session_position")
    pprint(await w_livestat.session_position.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.marker_position")
    pprint(await w_livestat.marker_position.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.track_number")
    pprint(await w_livestat.track_number.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.sample_rate")
    pprint(await w_livestat.sample_rate.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.linked_session_position")
    pprint(await w_livestat.linked_session_position.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.start")
    pprint(await w_livestat.start.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.stop")
    pprint(await w_livestat.stop.get())
    await asyncio.sleep(sleep)
    print(f"mixer.cards.w_live[1].status.sd:")
    w_livestatsd = w_livestat.sd
    pprint(w_livestatsd)
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.sd.free_space")
    pprint(await w_livestatsd.free_space.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.sd.size")
    pprint(await w_livestatsd.size.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.sd.state")
    pprint(await w_livestatsd.state.get())
    await asyncio.sleep(sleep)
    print(f"mixer.cards.w_live[1].status.error:")
    w_livestaterror = w_livestat.error
    pprint(w_livestaterror)
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.error.message")
    pprint(await w_livestaterror.message.get())
    await asyncio.sleep(sleep)
    print("mixer.cards.w_live[1].status.error.code")
    pprint(await w_livestaterror.code.get())
    await asyncio.sleep(sleep)


async def mixer_usb(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    print(f"mixer.usb:")
    usb = mixer.usb
    pprint(usb)
    await asyncio.sleep(sleep)
    print(f"mixer.usb.player:")
    usb_player = usb.player
    pprint(usb_player)
    await asyncio.sleep(sleep)
    print("mixer.usb.player.songs")
    pprint(await usb_player.songs.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.active_path")
    pprint(await usb_player.active_path.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.active_entry")
    pprint(await usb_player.active_entry.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.action_index")
    pprint(await usb_player.action_index.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.play_file")
    pprint(await usb_player.play_file.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.action")
    pprint(await usb_player.action.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.active_state")
    pprint(await usb_player.active_state.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.active_file")
    pprint(await usb_player.active_file.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.resolution")
    pprint(await usb_player.resolution.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.channels")
    pprint(await usb_player.channels.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.rate")
    pprint(await usb_player.rate.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.file_format")
    pprint(await usb_player.file_format.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.repeat")
    pprint(await usb_player.repeat.get())
    await asyncio.sleep(sleep)
    print(f"mixer.usb.player.song:")
    song = usb_player.song
    pprint(song)
    await asyncio.sleep(sleep)
    print("mixer.usb.player.song.name")
    pprint(await song.name.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.song.album")
    pprint(await song.album.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.song.artist")
    pprint(await song.artist.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.song.position")
    pprint(await song.position.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.player.song.duration")
    pprint(await song.duration.get())
    await asyncio.sleep(sleep)
    print(f"mixer.usb.recorder:")
    usb_recorder = usb.recorder
    pprint(usb_recorder)
    await asyncio.sleep(sleep)
    print("mixer.usb.recorder.active_state")
    pprint(await usb_recorder.active_state.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.recorder.active_filename")
    pprint(await usb_recorder.active_filename.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.recorder.action")
    pprint(await usb_recorder.action.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.recorder.path")
    pprint(await usb_recorder.path.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.recorder.resolution")
    pprint(await usb_recorder.resolution.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.recorder.channels")
    pprint(await usb_recorder.channels.get())
    await asyncio.sleep(sleep)
    print("mixer.usb.recorder.time")
    pprint(await usb_recorder.time.get())
    await asyncio.sleep(sleep)


async def mixer_control(mixer: WING, sleep):
    """

    :param mixer:
    :return:
    """
    print(f"mixer.control:")
    ctrl = mixer.control
    pprint(ctrl)
    await asyncio.sleep(sleep)

    await control_status(ctrl, sleep)


async def control_status(control, sleep):
    """

    :param control:
    :param sleep:
    :return:
    """
    print(f"mixer.control.status:")
    status = control.status
    pprint(status)
    await asyncio.sleep(sleep)
    print("mixer.control.status.selected_channel_strip")
    pprint(await status.selected_channel_strip.get())
    await asyncio.sleep(sleep)
    print("mixer.control.status.channel_page")
    pprint(await status.channel_page.get())
    await asyncio.sleep(sleep)
    print("mixer.control.status.channel_eq_band")
    pprint(await status.channel_eq_band.get())
    await asyncio.sleep(sleep)
    print("mixer.control.status.sends_on_fader")
    pprint(await status.sends_on_fader.get())
    await asyncio.sleep(sleep)
    print("mixer.control.status.send_page")
    pprint(await status.send_page.get())
    await asyncio.sleep(sleep)
    print("mixer.control.status.home_page_tab")
    pprint(await status.home_page_tab.get())
    await asyncio.sleep(sleep)
    print(f"mixer.control.status.console_lock:")
    lock = status.console_lock
    pprint(lock)
    await asyncio.sleep(sleep)
    print("mixer.control.status.console_lock.locked")
    pprint(await lock.locked.get())
    await asyncio.sleep(sleep)
    print("mixer.control.status.console_lock.unlock_buttons")
    pprint(await lock.unlock_buttons.get())
    await asyncio.sleep(sleep)


async def main():
    sleep = 0.05
    mixer = WING.create(host="mix.th00z")
    await mixer.initialize()

    #await mixer_status(mixer=mixer, sleep=sleep)
    #await mixer_general_configuration(mixer=mixer, sleep=sleep)
    #await mixer_system_configuration(mixer=mixer, sleep=sleep)
    #await mixer_io(mixer=mixer, sleep=sleep)
    #await mixer_channel(mixer=mixer, sleep=sleep)
    #await mixer_aux(mixer=mixer, sleep=sleep)
    #await mixer_bus(mixer=mixer, sleep=sleep)
    #await mixer_main(mixer=mixer, sleep=sleep)
    #await mixer_matrix(mixer=mixer, sleep=sleep)
    #await mixer_dca(mixer=mixer, sleep=sleep)
    #await mixer_mutegroup(mixer=mixer, sleep=sleep)
    #await mixer_fx(mixer=mixer, sleep=sleep)
    #await mixer_cards(mixer=mixer, sleep=sleep)
    await mixer_usb(mixer=mixer, sleep=sleep)
    sleep = 0.2
    await mixer_control(mixer=mixer, sleep=sleep)


asyncio.run(main())
