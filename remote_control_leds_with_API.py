#!/usr/bin/python3



import RPi.GPIO as GPIO 

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT) 

GPIO.setup(18, GPIO.OUT)

GPIO.setup(27, GPIO.OUT)

from flask import Flask

app = Flask(__name__)

@app.route('/') 

def hello_world():
    return 'Hello, World!'

@app.route('/rlon') 

def redledon():
    GPIO.output(36, GPIO.HIGH)
    return "Red LED on"

@app.route('/rloff') 

def redledoff():
    GPIO.output(36, GPIO.LOW)
    return "Red LED off" 

@app.route('/glon')

def greenledon():
    GPIO.output(40, GPIO.HIGH)
    return "Green LED on"

@app.route('/gloff')

def greenledoff():
    GPIO.output(40, GPIO.LOW)
    return "Green LED off"

@app.route('/blon')

def blueledon():
    GPIO.output(38, GPIO.HIGH)
    return "Blue LED on"

@app.route('/bloff')

def blueledoff():
    GPIO.output(38, GPIO.LOW)
    return "Blue LED off"

@app.route('/ylon')

def yellowledon():
    GPIO.output(37, GPIO.HIGH)
    return "Yellow LED on"

@app.route('/yloff')

def yellowledoff():
    GPIO.output(37, GPIO.LOW)
    return "Yellow LED off"

@app.route('/wlon')

def whiteledon():
    GPIO.output(35, GPIO.HIGH)
    return "White LED on"

@app.route('/wloff')

def whiteledoff():
    GPIO.output(35, GPIO.LOW)
    return "White LED off"



if __name__ == "__main__":
    app.run()





