# Open Smartwatch

## Organization / Coordination

[GitHub: Open Smartwatch](https://github.com/Open-Smartwatch)
[Discord: Pauls 3D Things](https://discord.gg/9DK5JY6)

# Hardware

## Version I
- ESP32 pico d4 (module ttgo 32micro) 
        Datasheet: https://www.espressif.com/sites/default/files/documentation/esp32-pico-d4_datasheet_en.pdf
- GC9A01 based IPS display (round)
- GPS quectel l96-m33
        Datasheet: https://www.quectel.com/UploadImage/Downlad/Quectel_L96_Hardware_Design_V1.2.pdf
- micro SD card (for open street maps)
- serial to usb (CH340E)
- lipo charging (mcp73831)
        Datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/MCP73831-Family-Data-Sheet-DS20001984H.pdf
- voltage regulator (mcp1812 or TLV70233DBVR, same footprints)
- power management: TPS2115A
- sensors: BMA400, BMP280
- buttons: reset, flash, + 2-3 more (4-5 total, reset = wakeup, 3-4 different buttons)
- voltage sensing: 1MOhm voltage divider
- display pwm: 2n7002 (n-ch)

# Software 

Current repository: https://github.com/Open-Smartwatch/esp32-pico-gc9a01

## Demos

- [Perlin-Noise World Watch Face](https://www.instagram.com/p/CEaALDAKkrY/)
- [Burning Watch Face](https://www.instagram.com/p/CEXmMHgqWuu/)
