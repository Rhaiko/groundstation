#!/usr/bin/env python

# Made by:  Elrick Weterings
#           Rotterdam University of Applied Sciences
#           Bachelor Thesis project
#           Spring 2018
#
# This file functions as library to control the backlight behind the lcd touchscreen.

import RPi.GPIO as GPIO

LCD_power = 25
LCD_backlight = 27

# Define GPIO
GPIO.setmode( GPIO.BCM )
GPIO.setup( LCD_power, GPIO.OUT )
GPIO.setup( LCD_backlight, GPIO.OUT )

pwm = GPIO.PWM( LCD_backlight, 100 )  # channel, frequency [Hz].

def brightnessLCD( procent ):
    GPIO.output(LCD_power, GPIO.HIGH)
    pwm.start(procent)

def disableLCD():
    pwm.stop()
    GPIO.output(LCD_power, GPIO.LOW)
