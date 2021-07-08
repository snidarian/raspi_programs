#!/usr/bin/python3


import Adafruit_DHT as afd
import RPi as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


DHT_SENSOR = afd.DHT11
DHT_PIN = 7

while True:
    humidity, temperature = afd.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp = {0:0.1f}C, Humidity = {1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor Slur (or ill-performed wiring)");
    time.sleep(1);







