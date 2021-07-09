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
R, G, B = 12, 33, 32
PINS = [R,G,B]
GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)
#p = GPIO.PWM(R, )

DHT_SENSOR = afd.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = afd.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp = {0:0.1f}C, Humidity = {1:0.1f}%".format(temperature, humidity))
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
        







