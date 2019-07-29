import Jetson.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
#GPIO.setup(33,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(33,GPIO.OUT)
#GPIO.setup(37,GPIO.OUT,initial=GPIO.HIGH)
p=GPIO.PWM(33,50)
p.start(0)
try:
    while True:
	for i in range(0,181,10):
	    p.ChangeDutyCycle(50)
	    time.sleep(0.02)
            p.ChangeDutyCycle(0)
            time.sleep(0.2)

        for i in range(181,0,-10):
	    p.ChangeDutyCycle(50)
	    time.sleep(0.02)
            p.ChangeDutyCycle(0)
            time.sleep(0.2)
	#print("while")
        #for dc in range(0,101,1): 
        #    print('1')
	#    p.ChangeDutyCycle(dc)
        #    time.sleep(0.1)
        #for dc in range(100,-1,-1):    
        #    print('2')
        #    p.ChangeDutyCycle(dc)
        #    time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup() 
