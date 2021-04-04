#!/usr/bin/python3


import RPi.GPIO as GPIO
import time




# set the pinmodes to either broadcom or board
GPIO.setmode(GPIO.BOARD)

# Set up gpio channel as output
GPIO.setup(8, GPIO.OUT)



count=0

while count < 8:
    GPIO.output(8, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(8, GPIO.LOW)
    time.sleep(.5)
    count+=1


GPIO.cleanup()









