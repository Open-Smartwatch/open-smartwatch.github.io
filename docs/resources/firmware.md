# Firmware

This page describes the requirements to manually flash the firmware.

Also check the latest readme file within the software repository: [https://github.com/Open-Smartwatch/open-smartwatch-os/blob/master/Readme.md](https://github.com/Open-Smartwatch/open-smartwatch-os/blob/master/Readme.md)

Watch this video: [https://www.youtube.com/watch?v=p-mDOIUr-rQ&ab_channel=pauls_3d_things](https://www.youtube.com/watch?v=p-mDOIUr-rQ&ab_channel=pauls_3d_things)

## Requirements

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

Got to the directory `include/` and copy the `config.h.example` to `config.h`.

Inside `include/config.h` make sure to adapt the following defines:

```c++
#define WIFI_SSID "yourSSID"
#define WIFI_PASS "yourP4ssw0rd"

#define TIMEZONE 1
#define DAYLIGHTOFFSET 0

#define DEVICE_NAME "yourDeviceName"
```

## Uploading

<img src="/assets/uploading.jpg" width="512px"/>

**Keep in mind the PCB is flipped when inserted into the watch:**

1. To set the watch into upload mode, you need to hold the lower left button and then click the reset button (top left). This enables flash mode, the display will turn dark.
2. Press the reset button after uploading
