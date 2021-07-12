#!/usr/bin/python3



import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)


# two functions for blip and beep that make the sound when called
def blip():
    GPIO.output(7, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(7, GPIO.LOW)

def beep():
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)


# set two global variables 'blip' and 'beep'
# blip represents dots and beep represents dashes.
#blip = make_blip()
#beep = make_beep()

# dictionary of lists (Each letter and its beep lengths)
morse_alphabet = {
    "a" : [blip(), beep()],
    "b" : [beep(), blip(), blip(), blip()],
    "c" : [blip(), beep(), blip(), beep()],
}


def main():
    text_message = input("Type a text message to convert to morse code: ")
    for letter in text_message:
        print(morse_alphabet[letter])





if __name__ == '__main__':
    main()
    GPIO.cleanup()










