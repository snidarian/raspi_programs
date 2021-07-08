#!/usr/bin/python3

import RPi.GPIO as GPIO
import threading
import time as t
import random as r

PINS = [12, 32, 33]


def select_and_set_next_pin():
    next_pin = PINS[r.randint(0,2)]
    GPIO.output(next_pin, not GPIO.input(next_pin))

def main():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)
        while True:
            select_and_set_next_pin()
            if all(GPIO.input(pin) == GPIO.LOW for pin in PINS):
                select_and_set_next_pin()
            t.sleep(0.75)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()













