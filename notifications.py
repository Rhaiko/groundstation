#!/usr/bin/env python

# Made by:  Elrick Weterings
#           Rotterdam University of Applied Sciences
#           Bachelor Thesis project
#           Spring 2018
#
# This file functions as library to control the leds and audio.

import RPi.GPIO as GPIO

NO_audio = 40
NO_LED0 = 41        # on/ off notification.
NO_LED1 = 42        # FDR.
NO_LED2 = 43        # Connection Robird.

# Define GPIO
GPIO.setmode( GPIO.BCM )
GPIO.setup( NO_LED0, GPIO.OUT )
GPIO.setup( NO_LED1, GPIO.OUT )
GPIO.setup( NO_LED2, GPIO.OUT )

# def ledRed()
# def ledYellow()
# def ledBlue()
# def