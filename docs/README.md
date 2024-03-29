# Other Docs an Links

## Tutorial: Control an LED light strip from a Raspberry Pi

- Video: [How to use WS2812B RGB LEDs with Raspberry Pi](https://www.youtube.com/watch?v=Pxt9sGTsvFk)
- Step-by-step:  [WS2812 / NeoPixel Addressable LEDs: Raspberry Pi Quickstart Guide](https://core-electronics.com.au/tutorials/ws2812-addressable-leds-raspberry-pi-quickstart-guide.html)

## Hardware

- My [Amazon List](https://www.amazon.com/hz/wishlist/ls/382JJL74JTTD9?ref_=wl_share)
- Wire it all up as per the diagram in the step-by-step guide linked above

Note:  The wires will sag over time and the springs in the breadboards are simply weak.  When they stay in tension over time, the metal will relax.  For long term use, invest in a wire wrap tool.  See also [Introduction to Wire Wrap](https://www.youtube.com/watch?v=IXvEDM-m9CE).

## Software

### BLE

- [RPi Bluetooth LE](https://elinux.org/RPi_Bluetooth_LE)
- bluepy [API docs](https://ianharvey.github.io/bluepy-doc/index.html) and [source code](https://github.com/IanHarvey/bluepy)

### ANT+ Drivers
- [Link](https://opensource.quarq.com/ant_usb2_stick/)

### ANT+ Clients

Packages that enable ANT+ dongles on the Raspberry Pi.

- Python [libant](https://github.com/half2me/libant)
- Go [antgo](https://github.com/half2me/antgo)

### Python Programmable LED Demo

Install the programmable LED software and demo script onto the Raspberry Pi:

```
#!/bin/bash

# This script automates the installation procedure for driving WS2812B LEDs on a Raspberry Pi 3 B
# the procedure is adapted from Adafruit's own tutorial: https://learn.adafruit.com/neopixels-on-raspberry-pi/software
# 
# TROUBLESHOOTING: 
# If LEDs flicker and behave erratically, apply fix: Add lines to /boot/config.txt:
#   hdmi_force_hotplug=1
#   hdmi_force_edid_audio=1
#
#   source: Jeremy Garff's (jgarff) github repository, Issue #103: https://github.com/jgarff/rpi_ws281x/issues


# Install the necessary packages
cd
sudo apt-get update
sudo apt-get -y install build-essential python-dev git scons swig
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons

cd python
sudo python setup.py install
cd
```

Easier one-liner:

```
curl -L http://coreelec.io/33 | bash
```
