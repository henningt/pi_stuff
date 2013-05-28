#!/usr/bin/env python

import RPi.GPIO as GPIO

light_on = False
LED_PIN = 25
BUTTON_PIN = 4

def setup():
    """
    This function will get the breadboard ready for input and output
    """
    
    GPIO.setmode(GPIO.BCM)

    # Disable warnings
    GPIO.setwarnings(False)
    
    # next line sets pin 25 for output (led)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    # this line will make sure that the led is off
    GPIO.output(LED_PIN, GPIO.LOW)    
    
    # next line sets pin 4 for input (button)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def toggle_led():
    """
    This will toggle led 
    """
    global light_on

    if light_on == True:
        GPIO.output(LED_PIN, GPIO.LOW)
        light_on = False

    elif light_on == False:
        GPIO.output(LED_PIN, GPIO.HIGH)
        light_on = True

def wait_for_button():
    """
    This will wait for the button to be pushed and call a function
    """

    while True:
        GPIO.wait_for_edge(BUTTON_PIN, GPIO.RISING)
        toggle_led()

    
setup()
wait_for_button()
