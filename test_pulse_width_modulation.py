#!/usr/bin/python3


import RPi.GPIO as GPIO
import random
import time


# Setup pins - pins 12, 32, and 33 wired to RGB pins on RGB module
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

# So we can refer to the pins namely by their LED color production
R, G, B = 32, 12, 33


# We'll use p variable as an alias for GPIO pulse width modulation method
red = GPIO.PWM(32, 0.1)
green = GPIO.PWM(12, 0.1)
blue = GPIO.PWM(33, 0.1)


for _ in range(10):
    red.start(random.randint(0, 100))
    green.start(random.randint(0, 100))
    blue.start(random.randint(0, 100))
    time.sleep(1)
    red.stop()
    green.stop()
    blue.stop()
    time.sleep(1)



GPIO.cleanup()
