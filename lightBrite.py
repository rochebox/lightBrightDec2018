# code for lighting a raspberry pi

import RPi.GPIO as GPIO
import time



myPins = [18, 23, 24, 25, 12, ]

pins = [18, 23, 24, 25, 12, 16, 26, 13, 6, 5 ]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for p in range(len(pins)):
    GPIO.setup(pins[p],GPIO.OUT)

for i in range(1000):

    for j in range(len(pins)):
        #print("LED on")
        GPIO.output(pins[j],GPIO.HIGH)
        time.sleep(0.1)
        #print("LED off")
        GPIO.output(pins[j],GPIO.LOW)
        time.sleep(0.1)
