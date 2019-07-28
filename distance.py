#!/usr/bin/env python

import sys
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')

import Jetson.GPIO as GPIO
import time

# Pin Definitions
trig_output_pin = 13  
echo_input_pin = 18  

def distance_to_spitball():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of LOW
    GPIO.setup(trig_output_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(echo_input_pin, GPIO.IN)
    #value = GPIO.input(echo_input_pin)
    #print("Value read from pin {} : {}".format(echo_input_pin,value_str))

    print("Starting Measure now! Press CTRL+C to exit")
    try:
        distance = 0
        while True:
            # Toggle the output every second
            GPIO.output(trig_output_pin, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(trig_output_pin, GPIO.LOW)
         
            pulse_start = time.time()
            while GPIO.input(echo_input_pin)==0:
                    pulse_start = time.time()

                    pulse_end = time.time()
                    while GPIO.input(echo_input_pin)==1:
                            pulse_end = time.time()

                            pulse_duration = pulse_end - pulse_start
                            distance = pulse_duration * 17150
                            distance = round(distance, 2)

                            print ("Distance" , distance)
        print ("Final distance is" , distance)                    
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    distance_to_spitball()
