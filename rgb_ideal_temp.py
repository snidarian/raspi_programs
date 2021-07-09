#!/usr/bin/python3


import RPi.GPIO as GPIO
import time
import random

R, G, B = 32, 12, 33

PINS = [R,G,B]

# set up pins 12 32 and 33 as PWM pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)
GPIO.setwarnings(False)

red = GPIO.PWM(R, 50)
green = GPIO.PWM(G, 50)
blue = GPIO.PWM(B, 50)

cycles=0

red.start(5)
green.start(5)
blue.start(5)

while cycles < 10:
    temp = random.randint(60, 90)
    ideal_temp = 73
    precision = 2
    print(f"Ideal temp: {temp}")
    # if the temperature is within {precision} show pure green color
    if ((abs(temp - ideal_temp)) <= precision):
        green.ChangeDutyCycle(100)
        red.ChangeDutyCycle(0)
        blue.ChangeDutyCycle(0)
        time.sleep(1)
    # Temp + precision is higher than ideal: TOO HOT
    # Red/green color ratio that grows more red and less green as it gets hotter
    elif ((temp - precision) > ideal_temp):
        green.ChangeDutyCycle(10)
        red.ChangeDutyCycle(100)
        blue.ChangeDutyCycle(0)
        time.sleep(1)
    # Temp - precision is lesser than ideal: TOO COLD
    # Green/green color ratio that grows more blue and less green as it gets colder
    elif ((temp + precision) < ideal_temp):
        green.ChangeDutyCycle(10)
        blue.ChangeDutyCycle(100)
        red.ChangeDutyCycle(0)
        time.sleep(1)
    cycles+=1
        




GPIO.cleanup()
