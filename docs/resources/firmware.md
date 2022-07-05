# Firmware
## Features
The table below list all currently available features of the OSW-OS. These features can be manually enabled (or disabled) by modifying the `platformio.ini` and adding (or removing) their `-D`-Define lines.

Flag | Description | Requirements
----------- | ----------- | -----------
`OSW_FEATURE_STATS_STEPS` | Enable step history (displayed on the watchfaces) | -
`OSW_FEATURE_WIFI` | Enable all wifi releated functions (services, webinterface) | -
`OSW_FEATURE_WIFI_APST` | Allow the watch to enable wifi client and station simultaneously | `OSW_FEATURE_WIFI`
`OSW_FEATURE_WIFI_ONBOOT` | Allow the user to enable the wifi on boot | `OSW_FEATURE_WIFI`
`OSW_FEATURE_LUA` | Enable LUA scripting support for apps | `LUA_C89_NUMBERS`
`LUA_C89_NUMBERS` | Needed when compiling with LUA support | -
`DEBUG=1` | Enables debug logging to the console & additional utilities | -
`GPS_EDITION` | Configure the build for use with GPS (including apps, api, sensors) | `PROGMEM_TILES`, `BOARD_HAS_PSRAM`
`PROGMEM_TILES` | Needed when compiling with GPS support | -
`BOARD_HAS_PSRAM` | Needed when compiling with GPS support | -
`GPS_EDITION_ROTATED` | Replacement for `GPS_EDITION` to work with flipped boards | -

### Other developed available flag

This flag is available on all models.

Flag | Description | Requirements
----------- | ----------- | -----------
- `RAW_SCREEN_SERVER` | Capture the watchface and save it as a `*.png` file. | `OSW_FEATURE_WIFI`
- `ANIMATION` | Animation can be used as the background of the watchface. | -

### Support
The table below lists which features are available in which version of the OS by default. It is always our goal to also support older hardware revisions, but not all features can run properly using the old schematics.

Flag | `LIGHT_EDITION_V4_0` | `LIGHT_EDITION_V3_3` | `LIGHT_EDITION_V3_2` | `LIGHT_EDITION_DEV_LUA` | `GPS_EDITION_V3_1` | `GPS_EDITION_DEV_ROTATED`
----------- | ----------- | ----------- | ----------- | ----------- | ----------- | -----------
`OSW_FEATURE_STATS_STEPS` | ✓ | ✓ | ✓ | ❌ | ✓ | ✓
`OSW_FEATURE_WIFI` | ✓ | ✓ | ✓ | ❌ | ✓ | ✓
`OSW_FEATURE_WIFI_APST` | ❌ | ❌ | ❌ | ❌ | ✓ | ✓
`OSW_FEATURE_WIFI_ONBOOT` | ✓ | ❌ | ❌ | ❌ | ✓ | ✓
`OSW_FEATURE_LUA` | ❌ | ❌ | ❌ | ✓ | ❌ | ❌

## Prerequisites
This page describes the requirements to manually flash the firmware.

Also check the latest readme file within the software repository: [https://github.com/Open-Smartwatch/open-smartwatch-os/blob/master/Readme.md](https://github.com/Open-Smartwatch/open-smartwatch-os/blob/master/Readme.md)

Watch this video: [https://www.youtube.com/watch?v=p-mDOIUr-rQ&ab_channel=pauls_3d_things](https://www.youtube.com/watch?v=p-mDOIUr-rQ&ab_channel=pauls_3d_things)

### Development Environment

To flash the latest software to the open-smartwatch you will need to install VScode with PlatformIO (Youtube tutorial: [https://youtu.be/JmvMvIphMnY](https://youtu.be/JmvMvIphMnY)).

### Git

Install `git` from [https://git-scm.com](https://git-scm.com).

### Serial Drivers CH340

The Open-Smartwatch uses a `ch340` for USB to serial. Please install the drivers from the manufacturer: [http://www.wch-ic.com/downloads/CH341SER_ZIP.html](http://www.wch-ic.com/downloads/CH341SER_ZIP.html)

#### Fixing `error: unknown type name ‘wait_queue_t’; did you mean ‘wait_event’?`

On Fedora Silverblue 34 `make` outputs `error: unknown type name ‘wait_queue_t’; did you mean ‘wait_event’?`.
This can be fixed by using [this fork from juliagoda](https://github.com/juliagoda/CH341SER).

## Cloning the Repository

Clone the source code repository **recursively**:

    git clone --recurse-submodules https://github.com/Open-Smartwatch/open-smartwatch-os.git

Then, open the directory with Visual Studio Code.

## Set up config.h

Got to the directory `include/` and take a look into the `config.h.example` - all instructions are noted there.

## Uploading

<img src="/assets/uploading.jpg" width="512px"/>

**Keep in mind the PCB is flipped when inserted into the watch:**

1. To set the watch into upload mode, you need to hold the lower left button and then click the reset button (top left). This enables flash mode, the display will turn dark.
2. Press the reset button after uploading.

## Troubleshooting

### Check the cable

Usually, a few cables do not have a data transmission role. Try to upload to another cable.

### Check the driver

Check the [driver](https://open-smartwatch.github.io/resources/firmware/#serial-drivers-ch340) insertion.

### Arduino_TFT.h: No such file or directory

You did not clone the repository with the `--recursive-submodules` flag.

!!! note "Tip"
    After changing the branch, follow the command :
    `git submodule update`

### 'LANG_STW_START' was not declared in this scope

You did not rename `include/config.h.example`

### Failed to connect to ESP32: Timed out waiting for packet header

You did not hold down BTN1(FLASH) and then tap the RESET button on the watch whilst platform.io was trying to connect.
