#!/usr/bin/python3



import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)


# two functions for blip and beep that make the sound when called
def blip():
    GPIO.output(7, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(7, GPIO.LOW)
    # length of pause after blip
    time.sleep(.1)

def beep():
    GPIO.output(7, GPIO.HIGH)
    time.sleep(.3)
    GPIO.output(7, GPIO.LOW)
    # length of pause after beep
    time.sleep(.1)

def letter_pause():
    time.sleep(.5)

def word_pause():
    time.sleep(.8)

def sentence_pause():
    time.sleep(2)

# set two global variables 'blip' and 'beep'
# blip represents dots and beep represents dashes.
#blip = make_blip()
#beep = make_beep()

# dictionary of lists (Each letter and its beep lengths)
morse_alphabet = {
    "a" : [blip, beep, letter_pause],
    # "b" : [beep(), blip(), blip(), blip(), letter_pause()],
    # "c" : [blip(), beep(), blip(), beep(), letter_pause()],
    # "d" : [beep(), blip(), blip(), letter_pause()],
    # "e" : [blip(), letter_pause()],
    # "f" : [blip(), blip(), beep(), blip(), letter_pause()],
    # "g" : [beep(), beep(), blip(), letter_pause()],
    # "h" : [blip(), blip(), blip(), blip(), letter_pause()],
    # "i" : [blip(), blip(), letter_pause()],
    # "j" : [blip(), beep(), beep(), beep(), letter_pause()],
    # "k" : [beep(), blip(), beep(), letter_pause],
    # "l" : [blip(), beep(), blip(), blip(), letter_pause],
    # "m" : [beep(), beep(), letter_pause()],
    # "n" : [beep(), blip(), letter_pause()],
    # "o" : [beep(), beep(), beep(), letter_pause()],
    # "p" : [blip(), beep(), beep(), blip(), letter_pause()],
    # "q" : [beep(), beep(), blip(), beep(), letter_pause()],
    # "r" : [blip(), beep(), blip(), letter_pause()],
    # "s" : [blip(), blip(), blip(), letter_pause()],
    # "t" : [beep(), letter_pause()],
    # "u" : [blip(), blip(), beep(), letter_pause()],
    # "v" : [blip(), blip(), blip(), beep(), letter_pause],
    # "w" : [blip(), beep(), beep(), letter_pause()],
    # "x" : [beep(), blip(), blip(), beep(), letter_pause()],
    # "y" : [beep(), blip(), beep(), beep(), letter_pause()],
    # "z" : [beep(), beep(), blip(), blip(), letter_pause()],
    # "." : [sentence_pause()],
    # " " : [word_pause()]
}


def main():
    text_message = "aaa"
    for letter in text_message:
        print(letter)
        morse_alphabet[letter][0]()
        morse_alphabet[letter][1]()
        morse_alphabet[letter][2]()




if __name__ == '__main__':
    main()
    GPIO.cleanup()










