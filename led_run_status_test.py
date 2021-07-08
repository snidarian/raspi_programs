#!/usr/bin/python3

# physical gpio pinouts
# uses the board not the bcm pin layout
# there are two leds (pin 23, pin 24) and both send their power through..
# a beeper that grounds them. In this way the beeper is on whenever one of the lights is
# It ends up sounding like an heart monitor which is what I want.


import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


for _ in range(5):
    print("led on")
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.1)
    print("led off")
    GPIO.output(23, GPIO.LOW)
    time.sleep(1)
    if _ % 2 == 0:
        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(24, GPIO.LOW)
        time.sleep(1)
    











