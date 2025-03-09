# behringer-mixer
Python module to get basic information from Behringer digital mixers eg X32/XAir etc.

Initial inspiration (and some code) comes from https://github.com/onyx-and-iris/xair-api-python.

## What it does and what it doesn't do.
This module is a simple interface to a series of Behringer digital mixers.  It does NOT support all parameters or controls.  It is primarily focussed on getting and setting fader information.  It supports getting this information, both on a once off basis and subscribing for real-time updates.

It currently supports the following functionality for all channels/busses/matrices/auxin/dcas/main/lr/mono:
- Fader Value (float and dB) [get/set]
- Fader Color (index 0-15 and color name) [get/set]
- Fader Mute status [get/set]
- Fader Name [get]

It also supports
- Current scene/snapshot [get]
- Change scene/snapshot [set]
- Control USB Player/Recorder [get/set]
- Current USB Filename [get]
- Firmware version
- Control of head-amps gain/phantom power

If you want a module that allows you to control the full functionality of the mixer, eg configuring effects/eq etc then I would recommend checking out https://github.com/onyx-and-iris/xair-api-python instead.

## Prerequisites

-   Python 3.10 or greater

## Installation

```
pip install behringer-mixer
```

## Usage

This module depends on the asyncio module to handle multiple runnings tasks simultaneously.

### Example
```python
import asyncio
import logging
from behringer_mixer import mixer_api

def updates_function(data):
    print(f"The property {data.get('property')} has been set to {data.get('value')}")

async def main():
    mixer  = mixer_api.create("X32", ip="192.168.201.149", logLevel=logging.WARNING)
    await mixer.start()
    state = await mixer.reload()
    state = mixer.state()
    print(state)
    asyncio.create_task(mixer.subscribe(updates_function))
    await mixer.set_value("/ch/1/mix_fader", 10)
    await asyncio.sleep(20)

if __name__ == "__main__":
    asyncio.run(main())
```

### Property Keys
The data returned by both the `state` and `subscription` callback function is based on a number of property keys for the mixer.  While these keys are 'similar' to the values used in the OSC commands they are not always the same.

Each key is a mixture of a base 'group' key eg `/ch/1/` and a more specific key.  
They keys have also been altered slightly to maintain a consistent approach between different mixers. eg. For channel/bus numbers the leading zero has been removed. on the XAir mixers the main fader is `/main/lr` whereas on the X32 it is `/main/st`.  This modules returns both as `/main/st`.

#### `mixer_api.create("<mixer_type>", ip="<ip_address>")`
The code is written to support the following mixer types:
- `X32`
- `XR18`
- `XR16`
- `XR12`

The following keyword arguments may be passed:

-   `ip`: ip address of the mixer (Required)
-   `port`: mixer port, defaults to 10023 for x32 and 10024 for xair
-   `delay`: a delay between each command, defaults to 20ms.
    -   a note about delay, stability may rely on network connection. For wired connections the delay can be safely reduced.  
-   `logLevel`: the level of logging, defaults to warning (enums from logging eg logging.DEBUG)
-   `include`: Optional. A list of what types of data to include. eg ["channels","bussess"] If not included then ALL data is returned.   Valid values are:
    - `channels`
    - `channelsends`
    - `auxins`
    - `busses`
    - `bussends`
    - `matrices`
    - `dcas`
    - `headamps`
    - `mains`
    - `mono`
    - `show`
    - `usb`

The create function only creates an instance of the mixer, it does not 'connect' to it.
You should call the `mixer.start()` function to prepare communication and then call `mixer.validate_connection()` to check that the connection to the mixer worked.

#### `mixer.firmware()`
Returns the firmware version of the mixer.
`
#### `mixer.info()`
Returns information about the mixer, giving the number of channels/busses etc as well as the base part of the 'address' for that component.
```
        {
            "channel": {
                "number": 32,
                "base_address": "ch",
            },
            "bus": {
                "number": 16,
                "base_address": "bus",
            },
            "matrix": {
                "number": 6,
                "base_address": "mtx",
            },
            "dca": {
                "number": 8,
                "base_address": "dca",
            },
            "fx": {
                "number": 10,
                "base_address": "fx",
            },
            "auxrtn": {
                "number": 8,
                "base_address": "auxrtn",
            },
            "scenes": {
                "number": 100,
                "base_address": "scene",
            },
        }
```

#### `mixer.last_received()`
Returns a unix timestamp giving the last time data was received from the mixer.

#### async `mixer.load_scene(scene_number)`
Changes the current/scene snapshot of the mixer.
`scene_number` is the scene number as stored on the mixer.

#### `mixer.name()`
Returns the network name of the mixer.

#### async `mixer.query(address)` (Low Level Call)
This is a low level call and returns the response of a previous `send` call. You should not need to call this, but rely on the managed state instead.

#### async `mixer.reload()`
Causes the the mixer to be requeried for it's current state. This only updates the module's internal state.  You would then need to call `mixer.state()` to receive the updated state.

#### async `mixer.send(address, value)` (Low Level Call)
This is a low level call to send an OSC message to the mixer.  As this is a low level call, the address of the OSC message being sent would have to conform to that required by the mixer in its documenation, no changing of the address is performed.  This call does not update the internal state. You should not need to call this, but rely on the managed state instead.

#### async `mixer.set_value(address, value)`
Tells the mixer to update a particular field parameter to the `value` specified.
`address` should be in the format returned by the `mixer.state()` call.
`value` should be in a format appropriate to the address being used. The module does no checking on the appropriateness of the value.
This call also updates the internal state of the module.

#### async `mixer.start()`
Starts the OSC server to process messages. Data will not be returned/processed unless this has been run

#### `mixer.state(<address>)`
Returns the current state of the mixer. If the optional address parameter is provided then the current state of that address is returned.  If the parameter is not provided then the entire state is returned as a dictionary of values.
```
{
	'/ch/1/mix_fader': 0.75,
	'/ch/1/mix_fader_db': 0.0,
    ...
	'/ch/1/mix_on': False,
	'/ch/2/mix_on': False,
	'/ch/1/config_name': 'VOX 1',
	'/ch/1/config_color': 4,
	'/ch/1/config_color_name': 'BL',
	...
	'/bus/1/mix_fader': 0.37829911708831787,
	'/bus/1/mix_fader_db': -19.7,
	...
	'/bus/4/mix_on': True,
	...
	'/bus/2/config_name': '',
	...
	'/dca/3/config_name': 'Drums',
	'/dca/3/config_color': 10,
	'/dca/3/config_color_name': 'GNi',
	...
	'/main/st/mix_fader': 0.7497556209564209,
	'/main/st/mix_fader_db': -0.0,
	'/main/st/mix_on': True,
	...
	'/scene/current': 6
}
```

#### async `mixer.stop()`
Stops the OSC server and the ability to process messages

#### async `mixer.subscribe(callback_function)`
This registers a `callback_function` that is called whenever there is a change at the mixer on one of the monitored properties.
The callback function will receive one dictionary parameter that contains the data that has been updated.
The content of this data parameter is as follows

```python
{ 
    'property': '/ch/01/mix_fader',
    'value': 0.85
}
```

#### async `mixer.subscription_connected()`
Returns true if the module has received data from the mixer in the last 15 seconds. 

#### async `mixer.subscription_status_register(callback_function)`
Register a function to be called when the subscription status changes.  This function is called when `subscription_connected()` changes.

#### async `mixer.unsubscribe()`
Stops the module listening to real time updates

#### async `mixer.validate_connection()`
Returns `True` if the connection to the mixer is successful, `False` otherwise.


## Tests

These tests attempt to connect to a mixer to exercise get/set from the channels.
The tests will change the state of the mixer, so it is recommended you save the current settings before running.
It is also recommended that any amplifier is turned off as feedback could occur if signals are present on the channels.

To run all tests:

`pytest -v`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Documentation

[XAir OSC Commands](https://behringer.world/wiki/doku.php?id=x-air_osc)

[X32 OSC Commands](https://wiki.munichmakerlab.de/images/1/17/UNOFFICIAL_X32_OSC_REMOTE_PROTOCOL_%281%29.pdf)

## Special Thanks

[Onyx-and-Iris](https://github.com/onyx-and-iris) for writing the XAir Python module


| OSC-Command                   | OSC-Type        | Description                                                                             | behringer-mixer Endpoint Path                                        | Endpoint Class  | Endpoint Type            |                  R / W                  |
|:------------------------------|:----------------|:----------------------------------------------------------------------------------------|:---------------------------------------------------------------------|:----------------|:-------------------------|:---------------------------------------:|
| `/$stat`                      | Node            | Status Node                                                                             | `mixer.status`                                                       | Component       | WINGStatus               |                  - / -                  |
| `/$stat/A`                    | Node            | AES50 A node                                                                            | `mixer.status.aes50_a`                                               | Component       | WINGStatusAES50Port      |                  - / -                  |
| `/$stat/A/stat`               | String          | AES50 A state [RO]                                                                      | `mixer.status.aes50_a.status`                                        | Endpoint        | WINGStringEnumEndpoint   |        :white_check_mark: / :x:         |
| `/$stat/A/dev`                | String          | AES50 A Device [RO]                                                                     | `mixer.status.aes50_a.device`                                        | Endpoint        | WINGStringEndpoint       |        :white_check_mark: / :x:         |
| `/$stat/B`                    | Node            | AES50 B node                                                                            | `mixer.status_aes50_b`                                               | Component       | WINGStatusAES50Port      |                  - / -                  |
| `/$stat/B/stat`               | String          | AES50 B state [RO]                                                                      | `mixer.status.aes50_b.status`                                        | Endpoint        | WINGStringEnumEndpoint   |        :white_check_mark: / :x:         |
| `/$stat/B/dev`                | String          | AES50 B Device [RO]                                                                     | `mixer.status.aes50_b.device`                                        | Endpoint        | WINGStringEndpoint       |        :white_check_mark: / :x:         |
| `/$stat/C`                    | Node            | AES50 B node                                                                            | `mixer.status_aes50_c`                                               | Component       | WINGStatusAES50Port      |                  - / -                  |
| `/$stat/C/stat`               | String          | AES50 C state [RO]                                                                      | `mixer.status.aes50_c.status`                                        | Endpoint        | WINGStringEnumEndpoint   |        :white_check_mark: / :x:         |
| `/$stat/C/dev`                | String          | AES50 C Device [RO]                                                                     | `mixer.status.aes50_c.device`                                        | Endpoint        | WINGStringEndpoint       |        :white_check_mark: / :x:         |
| `/$stat/lock`                 | Integer         | Clock lock [RO]                                                                         | `mixer.status.clock.lock`                                            | Endpoint        | WINGBoolEndpoint         |        :white_check_mark: / :x:         |
| `/$stat/ppm`                  | Integer         | Clock ppm [RO]                                                                          | `mixer.status.clock.ppm`                                             | Endpoint        | WINGIntEndpoint          |        :white_check_mark: / :x:         |
| `/$stat/solo`                 | Integer         | Solo [RO]                                                                               | `mixer.status.solo`                                                  | Endpoint        | WINGBoolEndpoint         |        :white_check_mark: / :x:         |
| `/$stat/sip`                  | Integer         | Solo In Place [RO]                                                                      | `mixer.status.solo_in_place`                                         | Endpoint        | WINGBoolEndpoint         |        :white_check_mark: / :x:         |
| `/$stat/rtcerr`               | Integer         | Real Time Clock Error [RO]                                                              | `mixer.status.clock.real_time_error`                                 | Endpoint        | WINGBoolEndpoint         |        :white_check_mark: / :x:         |
| `/$stat/time` / `/$stat/date` | String / String | Clock time (depending on date format) [RO] / Clock date (depending on date format) [RO] | `mixer.status.current_time`                                          | Endpoint        | WINGDatetimeEndpoint     |        :white_check_mark: / :x:         |
| `/$stat/usbstate`             | String          | USB Player state [RO]                                                                   | `mixer.status.usb_player.status`                                     | Endpoint        | WINGStringEnumEndpoint   |        :white_check_mark: / :x:         |
| `/$stat/usbvolname`           | String          | USB Player volume name [RO]                                                             | `mixer.status.usb_player.volume_name`                                | Endpoint        | WINGStringEndpoint       |        :white_check_mark: / :x:         |
| `/$stat/sc_stat`              | String          | StageConnect status [RO]                                                                | `mixer.status.stage_connect.status`                                  | Endpoint        | WINGStringEnumEndpoint   |        :white_check_mark: / :x:         |
| `/$stat/sc_devices`           | String          | StageConnect devices [RO]                                                               | `mixer.status.stage_connect.devices`                                 | Endpoint        | WINGStringEndpoint       |        :white_check_mark: / :x:         |
| `/$stat/sc_upcnt`             | Integer         | StageConnect upstreams [RO]                                                             | `mixer.status.stage_connect.upstreams`                               | Endpoint        | WINGIntEndpoint          |        :white_check_mark: / :x:         |
| `/$stat/sc_dncnt`             | Integer         | StageConnect downstreams [RO]                                                           | `mixer.status.stage_connect.downstreams`                             | Endpoint        | WINGIntEndpoint          |        :white_check_mark: / :x:         |
| `/$stat/sc_uprout`            | String          | StageConnect upstream routing [RO]                                                      | `mixer.status.stage_connect.upstream_routing`                        | Endpoint        | WINGStringEndpoint       |        :white_check_mark: / :x:         |
| `/$stat/rmt_a`                | String          | Name of the console connected on AES50 port A [RO]                                      | `mixer.status.remote_a`                                              | Endpoint        | WINGStringEndpoint       |        :white_check_mark: / :x:         |
| `/$stat/rmt_b`                | String          | Name of the console connected on AES50 port B [RO]                                      | `mixer.status.remote_b`                                              | Endpoint        | WINGStringEndpoint       |        :white_check_mark: / :x:         |
| `/$stat/rmt_c`                | String          | Name of the console connected on AES50 port C [RO]                                      | `mixer.status.remote_c`                                              | Endpoint        | WINGStringEndpoint       |        :white_check_mark: / :x:         |
| `/cfg`                        | Node            | General Configuration Node                                                              | `mixer.general_configuration`                                        | Component       | WINGGeneralConfiguration |                  - / -                  |
| `/cfg/mainlink`               | String          | Main Link                                                                               | `mixer.general_configuration.main_link`                              | Endpoint        | WINGStringEnumEndpoint   | :white_check_mark: / :white_check_mark: |
| `/cfg/dcamgrp`                | Integer         | DCA mutegroups (DCA mute mutes all channels assigned to DCA)                            | `mixer.general_configuration.dca_mutegroups`                         | Endpoint        | WINGBoolEndpoint         | :white_check_mark: / :white_check_mark: |
| `/cfg/mon`                    | Node            | Monitor buses config node                                                               | `mixer.general_configuration.monitor_bus`                            | List[Component] | WINGMonitorConfiguration |                  - / -                  |
| `/cfg/mon/1`                  | Node            | Monitor bus 1 node                                                                      | `mixer.general_configuration.monitor_bus[1]`                         | Component       | WINGMonitorConfiguration |                  - / -                  |
| `/cfg/mon/1/$lvl`             | Float           | Monitor bus 1 level (dB) [RO (on Full-Size WING)]                                       | `mixer.general_configuration.monitor_bus[1].level`                   | Endpoint        | WINGFaderEndpoint        |        :white_check_mark: / :x:         |
| `/cfg/mon/1/inv`              | Integer         | Monitor bus 1 invert (polarity)                                                         | `mixer.general_configuration.monitor_bus[1].invert_polarity`         | Endpoint        | WINGBoolEndpoint         | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/pan`              | Float           | Monitor bus 1 pan                                                                       | `mixer.general_configuration.monitor_bus[1].pan`                     | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/wid`              | Float           | Monitor bus 1 width (%)                                                                 | `mixer.general_configuration.monitor_bus[1].width`                   | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq`               | Node            | Monitor bus 1 EQ node                                                                   | `mixer.general_configuration.monitor_bus[1].eq`                      | Component       | WING6BandEQ              |                  - / -                  |
| `/cfg/mon/1/eq/on`            | Integer         | Monitor bus 1 EQ off / on                                                               | `mixer.general_configuration.monitor_bus[1].eq.on`                   | Endpoint        | WINGBoolEndpoint         | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/lsg`           | Float           | Monitor bus 1 EQ low shelf gain (dB)                                                    | `mixer.general_configuration.monitor_bus[1].eq.low_shelf.gain`       | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/lsf`           | Float           | Monitor bus 1 EQ low shelf frequency (Hz)                                               | `mixer.general_configuration.monitor_bus[1].eq.low_shelf.frequency`  | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/1g`            | Float           | Monitor bus 1 EQ band 1 gain (dB)                                                       | `mixer.general_configuration.monitor_bus[1].eq.band[1].gain`         | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/1f`            | Float           | Monitor bus 1 EQ band 1 frequency (Hz)                                                  | `mixer.general_configuration.monitor_bus[1].eq.band[1].frequency`    | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/1q`            | Float           | Monitor bus 1 EQ band 1 Q                                                               | `mixer.general_configuration.monitor_bus[1].eq.band[1].q`            | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/2g`            | Float           | Monitor bus 1 EQ band 2 gain (dB)                                                       | `mixer.general_configuration.monitor_bus[1].eq.band[2].gain`         | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/2f`            | Float           | Monitor bus 1 EQ band 2 frequency (Hz)                                                  | `mixer.general_configuration.monitor_bus[1].eq.band[2].frequency`    | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/2q`            | Float           | Monitor bus 1 EQ band 2 Q                                                               | `mixer.general_configuration.monitor_bus[1].eq.band[2].q`            | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/3g`            | Float           | Monitor bus 1 EQ band 3 gain (dB)                                                       | `mixer.general_configuration.monitor_bus[1].eq.band[3].gain`         | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/3f`            | Float           | Monitor bus 1 EQ band 3 frequency (Hz)                                                  | `mixer.general_configuration.monitor_bus[1].eq.band[3].frequency`    | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/3q`            | Float           | Monitor bus 1 EQ band 3 Q                                                               | `mixer.general_configuration.monitor_bus[1].eq.band[3].q`            | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/4g`            | Float           | Monitor bus 1 EQ band 4 gain (dB)                                                       | `mixer.general_configuration.monitor_bus[1].eq.band[4].gain`         | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/4f`            | Float           | Monitor bus 1 EQ band 4 frequency (Hz)                                                  | `mixer.general_configuration.monitor_bus[1].eq.band[4].frequency`    | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/4q`            | Float           | Monitor bus 1 EQ band 4 Q                                                               | `mixer.general_configuration.monitor_bus[1].eq.band[4].q`            | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/5g`            | Float           | Monitor bus 1 EQ band 5 gain (dB)                                                       | `mixer.general_configuration.monitor_bus[1].eq.band[5].gain`         | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/5f`            | Float           | Monitor bus 1 EQ band 5 frequency (Hz)                                                  | `mixer.general_configuration.monitor_bus[1].eq.band[5].frequency`    | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/5q`            | Float           | Monitor bus 1 EQ band 5 Q                                                               | `mixer.general_configuration.monitor_bus[1].eq.band[5].q`            | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/6g`            | Float           | Monitor bus 1 EQ band 6 gain (dB)                                                       | `mixer.general_configuration.monitor_bus[1].eq.band[6].gain`         | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/6f`            | Float           | Monitor bus 1 EQ band 6 frequency (Hz)                                                  | `mixer.general_configuration.monitor_bus[1].eq.band[6].frequency`    | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/6q`            | Float           | Monitor bus 1 EQ band 6 Q                                                               | `mixer.general_configuration.monitor_bus[1].eq.band[6].q`            | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/hsg`           | Float           | Monitor bus 1 EQ high shelf gain (dB)                                                   | `mixer.general_configuration.monitor_bus[1].eq.high_shelf.gain`      | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eq/hsf`           | Float           | Monitor bus 1 EQ high shelf frequency (Hz)                                              | `mixer.general_configuration.monitor_bus[1].eq.high_shelf.frequency` | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/lim`              | Float           | Monitor bus 1 limiter level(dB)                                                         | `mixer.general_configuration.monitor_bus[1].limiter`                 | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/dly`              | Node            | Monitor bus 1 delay node                                                                | `mixer.general_configuration.monitor_bus[1].delay`                   | Component       | WINGMonitorDelay         |                  - / -                  |
| `/cfg/mon/1/dly/on`           | Integer         | Monitor bus 1 delay off / on                                                            | `mixer.general_configuration.monitor_bus[1].delay.on`                | Endpoint        | WINGBoolEndpoint         | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/dly/m`            | Float           | Monitor bus 1 delay (meters)                                                            | `mixer.general_configuration.monitor_bus[1].delay.meters`            | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/dim`              | Float           | Monitor bus 1 delay dim level (dB)                                                      | `mixer.general_configuration.monitor_bus[1].dim`                     | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/pfldim`           | Float           | Monitor bus 1 PFL Dim (dB)                                                              | `mixer.general_configuration.monitor_bus[1].pfl_dim`                 | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/eqbdtrim`         | Float           | Monitor bus 1 band solo trim (dB)                                                       | `mixer.general_configuration.monitor_bus[1].band_solo`               | Endpoint        | WINGFloatEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/srclvl`           | Float           | Monitor bus 1 source level                                                              | `mixer.general_configuration.monitor_bus[1].source.level`            | Endpoint        | WINGFaderEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/srcmix`           | Float           | Monitor bus 1 source mix (dB)                                                           | `mixer.general_configuration.monitor_bus[1].source.mix`              | Endpoint        | WINGFaderEndpoint        | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/src`              | String          | Monitor bus 1 source                                                                    | `mixer.general_configuration.monitor_bus[1].source.source`           | Endpoint        | WINGStringEnumEndpoint   | :white_check_mark: / :white_check_mark: |
| `/cfg/mon/1/$lvlact`          | Float           | Monitor bus 1 fader level [RO]                                                          | `mixer.general_configuration.monitor_bus[1].fader_level`             | Endpoint        | WINGFaderEndpoint        |        :white_check_mark: / :x:         |
| `/cfg/mon/1/tags`             | String          | Monitor bus 1 tags                                                                      | `mixer.general_configuration.monitor_bus[1].tags`                    | Endpoint        | WINGStringEndpoint       | :white_check_mark: / :white_check_mark: |
