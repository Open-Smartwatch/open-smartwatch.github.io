# 3D Files

<img src="/assets/renders/logo.png" width="384px"/>

The 3D case design is optimized for FDM based 3D printers.

The main repository is here: [https://github.com/Open-Smartwatch/3d-files](https://github.com/Open-Smartwatch/3d-files)

## Cases

The naming is `case`-`gps/light`-`<pcb-thickness>`-`<strap-type>`

⚠️⚠️⚠️⚠️ When assembling the watch, please make sure to

- insulate the flex cable, to avoid shorts when pressing down on the display (best: kapton tape on the entire back of the LCD)
- the current case designs don't have sufficient room to assemble/disassemble the watch more than a few times. **there will be a fix for the cases soon**, until then carefully carve out the case until the display fits with not walls pressing against the flex cable. See [3d-files/issues/13](https://github.com/Open-Smartwatch/3d-files/issues/13).

<img src="/assets/screenshots/case-issue.png" width="256px" />


- [case-gps-0.8mm-pcb-20mm-straps](https://github.com/Open-Smartwatch/3d-files/tree/master/case-gps-0.8mm-pcb-20mm-straps)
- [case-light-0.8mm-pcb-20mm-straps](https://github.com/Open-Smartwatch/3d-files/tree/master/case-light-0.8mm-pcb-20mm-straps)
- [case-light-0.8mm-pcb-printed-straps](https://github.com/Open-Smartwatch/3d-files/tree/master/case-light-0.8mm-pcb-printed-straps)
- [case-light-1.6mm-pcb-20mm-straps](https://github.com/Open-Smartwatch/3d-files/tree/master/case-light-1.6mm-pcb-20mm-straps)
- [case-light-1.6mm-pcb-printed-straps](https://github.com/Open-Smartwatch/3d-files/tree/master/case-light-1.6mm-pcb-printed-straps)
- [case-light-round-0.8mm-pcb-printed-straps](https://github.com/Open-Smartwatch/3d-files/tree/master/case-light-round-0.8mm-pcb-printed-straps)
- [case-light-round-1.6mm-pcb-printed-straps](https://github.com/Open-Smartwatch/3d-files/tree/master/case-light-round-1.6mm-pcb-printed-straps)
- [case-light-round-20mm-wr-test](https://github.com/Open-Smartwatch/3d-files/tree/master/case-light-round-20mm-wr-test)

## Straps

- [wrist-strap-linked](https://github.com/Open-Smartwatch/3d-files/tree/master/wrist-strap-linked)
- [wrist-strap-flex](https://github.com/Open-Smartwatch/3d-files/tree/master/wrist-strap-tpu)


Check the repository [https://github.com/Open-Smartwatch/3d-files/](https://github.com/Open-Smartwatch/3d-files/) in case the lists above are outdated.

## Print Settings

### FDM

The cases are designed for a layer height of 0.1mm and 100% infill. All files are printable without support, given the right orientation. Some of the `-top` parts are face down (rotated 180 degrees), if the underside is not flat.

<img src="/assets/screenshots/pla-parts.jpg" width="512px" />


### SLA

#### Prusa SL1

Light Edition, case 1.6mm pcb, 20mm straps with pregenerated supports: [Download](/assets/downloads/sla-case-v2.sl1)

<img src="/assets/screenshots/sla-case-v2.png" width="512px" />
