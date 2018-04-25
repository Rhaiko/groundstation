#!/usr/bin/env python

# Made by:  Elrick Weterings
#           Rotterdam University of Applied Sciences
#           Bachelor Thesis project
#           Spring 2018
#
# This file must be run on boot and setups the Raspberry Pi for use.

import power_managment as PM
import lcd

# Set USB to receive power.
PM.USB_state(0)

# Set screen to full brightness.
lcd.brightnessLCD(100)

