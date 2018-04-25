#!/usr/bin/env python

# Made by:  Elrick Weterings
#           Rotterdam University of Applied Sciences
#           Bachelor Thesis project
#           Spring 2018
#
# This file installs all necessaries for the groundstation.
# Tested in a Raspbian environment.

import os

#################################################
# General.
#################################################

# Upgrade system.
os.system( "sudo apt-get update" )
os.system( "sudo apt-get upgrade" )

# Install GPIO decencies.
os.system( "sudo apt-get install python dev python-rpi.gpio" )

# Set boot.py in list to be run on boot.
os.system( "echo 'python /home/pi/Desktop/groundstation/boot.py' >> /home/pi/.profile" )