#!/usr/bin/python3


import Adafruit_DHT as afd
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)


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
        








