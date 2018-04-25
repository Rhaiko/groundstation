#!/usr/bin/env python

# Made by:  Elrick Weterings
#           Rotterdam University of Applied Sciences
#           Bachelor Thesis project
#           Spring 2018
#
# This file functions as library to control the power module in the groundstation and contains the following functions:
# USB_state( STATE ) :   set USB to receive power (default, STATE = 0) or to deliver power (STATE = 1).
# isCharging()       :   return 1 if charging, 0 otherwise.
# measurePower()     :   return current battery voltage and current.
# goodPower3v3()     :   return status 3V3 buck boost converter.
# goodPower5v()      :   return status 5V  buck boost converter.
# mainButton()       :   enable or disable screen and shutdown groundstation.

import RPi.GPIO as GPIO
import smbus
from time import sleep

# Define BCM pins (GPIO numbers) connected to the power module.
PM_mainButton = 9
PM_USB_state0 = 11
PM_USB_state1 = 12
PM_charge = 22
PM_goodpower_3v3 = 23
PM_goodpower_5v = 24


# Define GPIO
GPIO.setmode( GPIO.BCM )
GPIO.setup( PM_mainButton, GPIO.IN )
GPIO.setup( PM_USB_state0, GPIO.OUT )
GPIO.setup( PM_USB_state1, GPIO.OUT )
GPIO.setup( PM_charge, GPIO.IN )
GPIO.setup( PM_goodpower_3v3, GPIO.IN )
GPIO.setup( PM_goodpower_5v, GPIO.IN )

# ADC-address (I2C)
adcAddress = 0x28      # For AD7991-0
# adcAddress = 0x29      # For AD7991-1

# ADC-bus, i.e. /dev/i20-1 is bus = 1.
adcBus = 0

# Setup SMBus access.
bus = smbus.SMBus(adcBus)

# Read to start conversion.
bus.read_byte(adcAddress)

####################################################################
# Switch between receive and give out power through the USB port.
# state = 0 :   Set groundstation USB to receive power (default).
# state = 1 :   Set groundstation USB to give out power.
####################################################################
def USB_state( state ):
    if state == 0:
        GPIO.output( PM_USB_state1, GPIO.LOW )
        sleep(0.1)
        GPIO.output( PM_USB_state0, GPIO.LOW )
        return 0
    elif state == 1:
        GPIO.output(PM_USB_state0, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(PM_USB_state1, GPIO.HIGH)
        return 0
    else:
        return -1


####################################################################
# Check if system is being charged.
# Return 1 if charging, 0 otherwise.
####################################################################
def isCharging():
    return GPIO.input( PM_charge )


####################################################################
# Measures and returns battery voltage en current.
# Return voltage; input current; output current.
####################################################################
def measurePower():
    l = []

    # If charging, measure charging current.
    if isCharging() == True:
        bus.write_byte( adcAddress, 0x18 )
        l.append( bus.read_byte( adcAddress ) )
    else
        l.append(0)

    # Measure battery output current.
    bus.write_byte(adcAddress, 0x28)
    l.append( bus.read_byte( adcAddress ) )

    # Measure battery voltage.
    bus.write_byte( adcAddress, 0x48 )
    l.append( bus.read_byte( adcAddress ) )

    return l


####################################################################
# Checks if 3v3 power supply is workings nominally.
# Return 1 if normal, 0 otherwise.
####################################################################
def goodPower3v3():
    return GPIO.input( PM_goodpower_3v3 )


####################################################################
# Checks if 5v power supply is workings nominally.
# Return 1 if normal, 0 otherwise.
####################################################################
def goodPower5v():
    return GPIO.input( PM_goodpower_5v )


####################################################################
# Checks if 5v power supply is workings nominally.
# Return 1 if normal, 0 otherwise.
####################################################################


# mainButton()       :   enable or disable screen and shutdown groundstation.











