# code for lighting a raspberry pi

import RPi.GPIO as GPIO
import time


goForward = True
pins = [18, 23, 24, 25, 12, 16, 26, 13, 6, 5 ]

#initial set up
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for p in range(len(pins)):
    GPIO.setup(pins[p],GPIO.OUT)

#set up for the button
# Set pin 22 to be an input pin and set initial value to be pulled low (off)
bPin = 22
GPIO.setup(bPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def runLights():
    global goForward
    if goForward:
        for j in range(len(pins)):
            #print("LED {} on".format(j))
            GPIO.output(pins[j],GPIO.HIGH)
            time.sleep(0.05)
            #print("LED off")
            GPIO.output(pins[j],GPIO.LOW)
            time.sleep(0.05)
        goForward = False;
    else:
        for j in range(len(pins)-1, -1, -1):
            #print("LED {} on".format(j))
            GPIO.output(pins[j],GPIO.HIGH)
            time.sleep(0.05)
            #print("LED off")
            GPIO.output(pins[j],GPIO.LOW)
            time.sleep(0.05)
        goForward = True;

#now run a forever loop to do what you need
while True: # Run forever
    if GPIO.input(bPin) == GPIO.HIGH:
        #print("Button was pushed!")
        runLights()
        #time.sleep(3)

