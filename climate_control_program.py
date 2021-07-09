#!/usr/bin/python3


import Adafruit_DHT as afd
import RPi.GPIO as GPIO
import threading
import time


# initial all gpio pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# green and red LED status light indicators
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
# Pulse width modulation pins on data out
R, G, B = 32, 12, 33
PINS = [R,G,B]

#GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.setup(32, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.setup(33, GPIO.OUT, initial=GPIO.HIGH)


# Setup RGB GPIO data out pins
red = GPIO.PWM(R, 50)
green = GPIO.PWM(G, 50)
blue = GPIO.PWM(B, 50)


def rgb_temp_indicator(temp) -> None:
    print(f"temp passed : {temp}")
    print(type(temp))
    ideal_temp = 73
    precision = 2
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

# Setup pins for DTH11 sensor interface
DHT_SENSOR = afd.DHT11
DHT_PIN = 4


# main loop
while True:
    humidity, temperature = afd.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp = {0:0.1f}C, Humidity = {1:0.1f}%".format(temperature, humidity))
        rgb_temp_indicator(temperature)
        GPIO.output(16, GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(16, GPIO.LOW)
        time.sleep(2)
    else:
        print("Sensor Slur (or ill-performed wiring)");
        GPIO.output(18, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(18, GPIO.LOW)
        time.sleep(2)
        

GPIO.cleanup()





