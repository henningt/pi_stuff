#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep, time

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
last_push = 0

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

def button_pushed(button_pin):
    """
    this will ask if button is pushed
    """
    global last_push
    
    elapsed_time = time() - last_push
    if elapsed_time < 0.5:
        return False
    
    if GPIO.input(button_pin):
        last_push = time()
        return True
    else:
        return False
    

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
state = False
while 1:
    # check if state is true, toggle led 1, if so
    if state == True:
        toggle_led(1)
        sleep(0.25)
        toggle_led(1)
              
    # check button to maybe switch state
    if button_pushed(BUTTON) == True:
         state = not state   
    
    # check if state is true, toggle led 2, if so
    if state == True:
        toggle_led(2)
        sleep(0.25)
        toggle_led(2)
    
    # check button to maybe switch state
    if button_pushed(BUTTON) == True:
         state = not state   
    
    
    # check if state is true, toggle led 3, if so
    if state == True:
        toggle_led(3)
        sleep(0.25)
        toggle_led(3)
        
    # check button to maybe switch state
    if button_pushed(BUTTON) == True:
         state = not state   
     
    # check if state is true, toggle led 4, if so
    if state == True:
        toggle_led(4)
        sleep(0.25)
        toggle_led(4)
        
    # check button to maybe switch state
    if button_pushed(BUTTON) == True:
         state = not state   





    
