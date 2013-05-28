#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
raw_input("Hit enter to turn on the LED")
GPIO.output(25, GPIO.HIGH)
raw_input("Hit enter to turn off the LED")
GPIO.output(25, GPIO.LOW)
