#!/usr/bin/env python

import RPi.GPIO as GPIO

light_on = False

def setup():
    """
    This function will get the breadboard ready for input and output
    """
    
    GPIO.setmode(GPIO.BCM)

    # Disable warnings
    GPIO.setwarnings(False)
    
    # next line sets pin 25 for output (led)
    GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
    # this line will make sure that the led is off
    GPIO.output(25, GPIO.LOW)    
    
    # next line sets pin 4 for input (button)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def toggle_led(arg):
    """
    This will toggle led 
    """
    global light_on

    if light_on == True:
        GPIO.output(25, GPIO.LOW)
        light_on = False

    elif light_on == False:
        GPIO.output(25, GPIO.HIGH)
        light_on = True

def setup_button_callback():
    """
    sets up callback to toggle led when button is pushed
    """
    GPIO.add_event_detect(4, GPIO.RISING)
    GPIO.add_event_callback(4, toggle_led)


setup()
setup_button_callback()
