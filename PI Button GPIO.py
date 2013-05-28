#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(25, GPIO.RISING)

def my_callback(arg1):
    print 'PUSHED! (%s)' % str(arg1)

GPIO.add_event_callback(25, my_callback)
