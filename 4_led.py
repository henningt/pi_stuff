#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

light_on = {
    1: False,
    2: False,
    3: False,
    4: False,
}
LED = {
    1: 4,
    2: 17,
    3: 18,
    4: 23,
}
BUTTON = 25

def setup():
    """
    This function will get the breadboard ready for input and output
    """
    
    GPIO.setmode(GPIO.BCM)

    # Disable warnings
    GPIO.setwarnings(False)
    
    for i in range(1, 5):
        # next line sets a pin for output (led)
        GPIO.setup(LED[i], GPIO.OUT, initial=GPIO.LOW)
        
        # this line will make sure that the led is off
        GPIO.output(LED[i], GPIO.LOW)

    # next line sets pin for input (button)
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    

def toggle_led(led_number):
    """
    This will toggle led 
    """
    if light_on[led_number] == True:
        GPIO.output(LED[led_number], GPIO.LOW)
        light_on[led_number] = False

    elif light_on[led_number] == False:
        GPIO.output(LED[led_number], GPIO.HIGH)
        light_on[led_number] = True

def toggle_all():
    """
    this will toggle all the led
    """
    for i in xrange(1, 5):
        toggle_led(i)
        sleep(0.1)

def wait_for_button():
    """
    This will wait for the button to be pushed and call a function
    """
    GPIO.wait_for_edge(BUTTON, GPIO.RISING)

    
setup()

while 1:
    wait_for_button()
    toggle_all()
    sleep(0.5)        
