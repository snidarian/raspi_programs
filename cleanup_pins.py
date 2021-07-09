#!/usr/bin/python3


import RPi.GPIO as GPIO


PINS= [12, 32, 33]

GPIO.setmode(GPIO.BOARD)


GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)



GPIO.cleanup()









