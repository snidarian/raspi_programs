#!/usr/bin/python3



import RPi.GPIO as GPIO
import threading
import time
import random

R = 12
G = 33
B = 32

PINS = [R,G,B]

def initialize_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)

def color_test(channel, frequency, speed, step):
    p = GPIO.PWM(channel, frequency)
    p.start(0)
    while True:
        for duty_cycle in range(0, 101, step):
            p.ChangeDutyCycle(duty_cycle)
            time.sleep(speed)
        for duty_cycle in range(100, -1, step):
            p.ChangeDutyCycle(duty_cycle)
            time.sleep(speed)

def color_test_thread():
    threads = []
    threads.append(threading.Thread(target=color_test, args=(R, 300, 0.02, 5)))
    threads.append(threading.Thread(target=color_test, args=(G, 300, 0.0352, 5)))
    threads.append(threading.Thread(target=color_test, args=(B, 300, 0.045, 5)))
    for t in threads:
        t.daemon = True
        t.start()
    for t in threads:
        t.join()


def main():
    try:
        initialize_gpio()
        print("mark1")
        color_test_thread()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()









