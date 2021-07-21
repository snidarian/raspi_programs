#!/usr/bin/python3


import RPi.GPIO as GPIO
import random
import time


# pin colors
R=40
B=35
G=36
Y=37
W=38

# board pin numbers
PINS = [ R, B, G, Y, W]

# groun pin is pin 39

# setup led pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PINS, GPIO.OUT)



def straight_through(freq) -> None:
    for pin in PINS:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(freq)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(freq)


def there_and_back(freq) -> None:
    for pin in [R, B, G, Y, W, W, Y, G, B, R]:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(freq)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(freq)

def slow_mo(freq) -> None:
    for pin in PINS:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(freq + .5)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(freq + .5)


def main(freq) -> None:
    for _ in range(10):
        straight_through(freq)
        there_and_back(freq)
        slow_mo(freq)



if __name__ == "__main__":
    try:
        main(.05)
    except KeyboardInterrupt:
        GPIO.cleanup()


GPIO.cleanup()




















