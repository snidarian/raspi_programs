#!/usr/bin/python3



import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)




GPIO.output(4, GPIO.HIGH)
time.sleep(2)
GPIO.output(4, GPIO.HIGH)
time.sleep(2)
GPIO.output(4, GPIO.HIGH)
time.sleep(2)


# list of lists (Each letter and its beep lengths)


GPIO.cleanup()










