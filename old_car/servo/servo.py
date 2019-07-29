#!/usr/bin/env python
import sys
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/')
sys.path.append('/opt/nvidia/jetson-gpio/lib/python/Jetson/GPIO')

import Jetson.GPIO as GPIO
import time
output_pin = 33

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    curr_value = GPIO.HIGH
    try:
        for x in range(0,100):
            #time.sleep(0.015)
            print("Outputting {} to pin {}".format(x, output_pin))
            GPIO.output(output_pin, x)
            time.sleep(0.1)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
