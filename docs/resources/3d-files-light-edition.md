# 3D Files Light Edition

There are a range of design files for the Light Edition, see the main repository here:  [https://github.com/Open-Smartwatch/3d-files](https://github.com/Open-Smartwatch/3d-files).
The 3D case designs are optimized for FDM based 3D printers.
The major difference of the designs is for which LiPo battery it has been created.
See [Hardware](hardware.md) for the recommended batteries.

*Note about PCB thickness:* Most of the cases are designed for a 1.6mm PCB, which should also fit a 0.8mm PCB.
If the file name explicitly says 0.8mm, it will not fit a 1.6mm PCB. If you create case designs, please keep this in mind and add the pcb thickness to the file name.

## Important Assembly Notes

⚠️⚠️⚠️⚠️ When assembling any watch case, please make sure to

- insulate the flex cable, to avoid shorts when pressing down on the display (best: kapton tape on the entire back of the LCD)
- the current case designs don't have sufficient room to assemble/disassemble the watch more than a few times. **there will be a fix for the cases soon**, until then carefully carve out the case until the display fits with not walls pressing against the flex cable. See [3d-files/issues/13](https://github.com/Open-Smartwatch/3d-files/issues/13).

<img src="/assets/screenshots/case-issue.png" width="256px" />

## Print Settings

### FDM

The cases are or should be designed for a layer height of 0.1mm and 100% infill. All files are printable without support, given the right orientation. Some of the `-top` parts are face down (rotated 180 degrees), if the underside is not flat. No solid wall/plane should be thinner than 0.8mm.

## Round LiPo

### Light Flex Buttons (20mm Straps)

<img src="/assets/3d-files/light-flex-buttons.png" width="270px" style="float:left; margin-right:30px"/>

This case consists of an outer shell (PLA/...) and a soft inner shell (TPU). All parts can be printed without supports, the top cases need to be facing down. Recommended for 0.2mm layers. [Repository](https://github.com/Open-Smartwatch/3d-files/tree/master/case-light-round-1.6mm-pcb-20mm-straps-flex-buttons).

 * [case-light-round-1.6mm-case-top.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-round-1.6mm-pcb-20mm-straps-flex-buttons/case-light-round-1.6mm-case-top.stl)
 * [case-light-round-1.6mm-case-bot.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-round-1.6mm-pcb-20mm-straps-flex-buttons/case-light-round-1.6mm-case-bot.stl)
 * [case-light-round-1.6mm-flex-top.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-round-1.6mm-pcb-20mm-straps-flex-buttons/case-light-round-1.6mm-flex-top.stl)
 * [case-light-round-1.6mm-flex-bot.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-round-1.6mm-pcb-20mm-straps-flex-buttons/case-light-round-1.6mm-flex-bot.stl)
 * [buttons.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-round-1.6mm-pcb-20mm-straps-flex-buttons/buttons.stl)

<div style="clear: both; margin-bottom:20px"></div>


## Rectangular LiPo

### Basic Case (20mm Straps)

<img src="/assets/3d-files/light-rect.png" width="270px" style="float:left; margin-right:30px"/>

This is a design for the rectangular LiPo. It consists of a top, middle and bottom piece.
There is an alternative top to allow the insertion of a 36mm glass. [Repository](https://github.com/Open-Smartwatch/3d-files/tree/master/case-light-1.6mm-pcb-20mm-straps).

* [case-light-1.6mm-pcb-20mm-straps-1-pla.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-1.6mm-pcb-20mm-straps/case-light-1.6mm-pcb-20mm-straps-1-pla.stl)
* [case-light-1.6mm-pcb-20mm-straps-1-glass-pla.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-1.6mm-pcb-20mm-straps/case-light-1.6mm-pcb-20mm-straps-1-glass-pla.stl)
* [case-light-1.6mm-pcb-20mm-straps-2-pla.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-1.6mm-pcb-20mm-straps/case-light-1.6mm-pcb-20mm-straps-2-pla.stl)
* [case-light-1.6mm-pcb-20mm-straps-3-pla.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-1.6mm-pcb-20mm-straps/case-light-1.6mm-pcb-20mm-straps-3-pla.stl)
* [case-light-1.6mm-pcb-20mm-straps-buttons-pla.stl](https://github.com/Open-Smartwatch/3d-files/blob/master/case-light-1.6mm-pcb-20mm-straps/case-light-1.6mm-pcb-20mm-straps-buttons-pla.stl)

<div style="clear: both; margin-bottom:20px"></div>

### Basic Case (Printed Straps)

#### Prusa SL1 Supports

Light Edition, case 1.6mm pcb, 20mm straps with pregenerated supports: [Download](/assets/downloads/sla-case-v2.sl1)

<img src="/assets/screenshots/sla-case-v2.png" width="512px" />


