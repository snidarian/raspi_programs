#!/usr/bin/python3


import RPi.GPIO as GPIO

# reset all non-ground, non-power pins.
PINS= [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 35, 36, 37, 38, 40]

GPIO.setmode(GPIO.BOARD)


GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)



GPIO.cleanup()









