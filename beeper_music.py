#!/usr/bin/python3
# prelude in C major by JS Bach
# incomplete

import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
beeper = GPIO.PWM(16, 1000)
# set initial duty cycle - adjusting this is crucial to tone clarity
beeper.start(5)

tones = {
"B0": 30.87,"C1": 32.70,"CS1": 34.65,"D1": 36.71,"DS1": 38.89,"E1": 41,"F1": 44,"FS1": 46,"G1": 49,"GS1": 52,"A1": 55,
"AS1": 58,"B1": 62,

"C2": 65,"CS2": 69,"D2": 73.42,"DS2": 78,"E2": 82,"F2": 87,"FS2": 93,"G2": 98,"GS2": 104,"A2": 110,"AS2": 117,"B2": 123.47,

"C3": 130.81,"CS3": 139,"D3": 146.83,"DS3": 156,"E3": 165,"F3": 175,"FS3": 185,"G3": 196,"GS3": 208,"A3": 220,"AS3": 233,"B3": 247,

"C4": 262,"CS4": 277,"D4": 294,"DS4": 311,"E4": 330,"F4": 349,"FS4": 370,"G4": 392.0,"GS4": 415,"A4": 440.0,"AS4": 466,"B4": 494,

"C5": 523.25,"CS5": 554,"D5": 587,"DS5": 622,"E5": 659.25,"F5": 698.46,"FS5": 740,"G5": 784,"GS5": 831,"A5": 880,"AS5": 932,"B5": 988,

"C6": 1047,"CS6": 1109,"D6": 1175,"DS6": 1245,"E6": 1319,"F6": 1397,"FS6": 1480,"G6": 1568,"GS6": 1661,"A6": 1760,
"AS6": 1865,"B6": 1976,

"C7": 2093,"CS7": 2217,"D7": 2349,"DS7": 2489,"E7": 2637,"F7": 2794,"FS7": 2960,"G7": 3136,"GS7": 3322,"A7": 3520,"AS7": 3729,"B7": 3951,

"C8": 4186,"CS8": 4435,"D8": 4699,"DS8": 4978
}


pattern_list = [
    # First measure - used twice
    [tones["C3"],tones["E3"],tones["G4"],tones["C5"], tones["E5"]],
    # Second measure
    [tones["C3"],tones["D3"],tones["A4"],tones["D5"], tones["F5"]],
    # Third measure
    [tones["B2"],tones["D3"],tones["G4"],tones["D5"], tones["F5"]],
    [tones["C3"],tones["E3"],tones["A4"],tones["E5"], tones["A5"]],
    [tones["C3"],tones["D3"],tones["FS4"],tones["A4"], tones["C5"]],
    [tones["B2"],tones["D3"],tones["G4"],tones["D5"], tones["G5"]],
    [tones["B2"],tones["C3"],tones["E4"],tones["G4"], tones["C5"]],
    [tones["A2"],tones["C3"],tones["E4"],tones["G4"], tones["C5"]],
    [tones["D2"],tones["A2"],tones["D4"],tones["FS4"], tones["C5"]],
    [tones["G2"],tones["B2"],tones["D4"],tones["G4"], tones["B4"]],
    [tones["B2"],tones["C3"],tones["E4"],tones["G4"], tones["C5"]],
    [tones["A2"],tones["C3"],tones["E4"],tones["G4"], tones["C5"]],
    [tones["D2"],tones["A2"],tones["D4"],tones["FS4"], tones["C5"]],
    [tones["G2"],tones["B2"],tones["D4"],tones["G4"], tones["B4"]],
    [tones["G2"],tones["AS2"],tones["E4"],tones["G4"], tones["CS5"]],
    [tones["F2"],tones["A2"],tones["D4"],tones["A4"], tones["D5"]],
    [tones["F2"],tones["GS2"],tones["D4"],tones["F4"], tones["B4"]],
    [tones["E2"],tones["G2"],tones["C4"],tones["G4"], tones["C5"]],
    [tones["E2"],tones["F2"],tones["A3"],tones["C4"], tones["F4"]],
    [tones["D2"],tones["F2"],tones["A3"],tones["C4"], tones["F4"]],
    [tones["G1"],tones["D2"],tones["G3"],tones["B3"], tones["F4"]],
    [tones["C2"],tones["E2"],tones["G3"],tones["C4"], tones["E4"]],
    # Second page
    [tones["C2"],tones["G2"],tones["AS3"],tones["C4"], tones["E4"]],
    [tones["F1"],tones["F2"],tones["A3"],tones["C4"], tones["E4"]],
    # 3rd measure
    [tones["FS1"],tones["C2"],tones["A3"],tones["C4"], tones["DS4"]],
    # 4th measure
    [tones["GS1"],tones["F2"],tones["B3"],tones["C4"], tones["D4"]],
    # 5th measure 2nd row
    [tones["G1"],tones["F2"],tones["G3"],tones["B3"], tones["D4"]],
    # 6th measure 2nd row
    [tones["G1"],tones["E2"],tones["G3"],tones["C4"], tones["E4"]],
    # 7th measure 2nd row
    [tones["G1"],tones["D2"],tones["G3"],tones["C4"], tones["F4"]],
    # 8th measure 2nd row
    [tones["G1"],tones["D2"],tones["G3"],tones["B3"], tones["F4"]],
    # 9th measure 3rd row
    [tones["G2"],tones["DS3"],tones["A3"],tones["C4"], tones["FS4"]],
    # 10th measure 3rd row
    [tones["G1"],tones["E2"],tones["G3"],tones["C4"], tones["G4"]],
    # 11th measure 3rd row
    [tones["G1"],tones["D2"],tones["G3"],tones["C4"], tones["F4"]],
    # 12th measure 3rd row
    [tones["G1"],tones["D2"],tones["G3"],tones["B3"], tones["F4"]],
    # 13th measure 4th row
    [tones["C1"],tones["C2"],tones["G3"],tones["AS3"], tones["E4"]],

    
]


def play_main_pattern(note_set, rate) -> None:
    for _ in range(2):
        beeper.ChangeFrequency(note_set[0])
        time.sleep(rate)
        beeper.ChangeFrequency(note_set[1])
        time.sleep(rate)
        beeper.ChangeFrequency(note_set[2])
        time.sleep(rate)
        beeper.ChangeFrequency(note_set[3])
        time.sleep(rate)
        beeper.ChangeFrequency(note_set[4])
        time.sleep(rate)
        beeper.ChangeFrequency(note_set[2])
        time.sleep(rate)
        beeper.ChangeFrequency(note_set[3])
        time.sleep(rate)
        beeper.ChangeFrequency(note_set[4])
        time.sleep(rate)

def play_ending(rate) -> None:
    for note in ["C1","C2","F3","A3","C4","F4","C4","A3",
                 "C4","A2","F2","A2","F2","D2","F2","D2",
                 "C1", "B1", "G4","B4","D5","F5","D5","B4",
                 "D5","B4","G4","B4","D4","F4","E4","D4",
                 "C2","C2","C2","C2"]:
        beeper.ChangeFrequency(tones[note])
        time.sleep(rate)


def main(rate):
    try:
        print("1 measure")
        play_main_pattern(pattern_list[0], rate)
        print("2 measure")
        play_main_pattern(pattern_list[1], rate)
        print("3 measure")
        play_main_pattern(pattern_list[2], rate)
        # pattern 0 repeats once
        print("4 measure")
        play_main_pattern(pattern_list[0], rate)
        print("5 measure")
        play_main_pattern(pattern_list[3], rate)
        print("6 measure")
        play_main_pattern(pattern_list[4], rate)
        print("7 measure")
        play_main_pattern(pattern_list[5], rate)
        print("8 measure")
        play_main_pattern(pattern_list[6], rate)
        print("9 measure")
        play_main_pattern(pattern_list[7], rate)
        print("10 measure")
        play_main_pattern(pattern_list[8], rate)
        print("11 measure") #
        play_main_pattern(pattern_list[9], rate)
        print("12 measure")
        play_main_pattern(pattern_list[10], rate)
        print("13 measure")
        play_main_pattern(pattern_list[12], rate)
        print("14 measure")
        play_main_pattern(pattern_list[13], rate)
        print("15 measure")
        play_main_pattern(pattern_list[14], rate)
        print("16 measure")
        play_main_pattern(pattern_list[15], rate)
        print("17 measure")
        play_main_pattern(pattern_list[16], rate)
        print("18 measure")
        play_main_pattern(pattern_list[17], rate)
        print("19 measure")
        play_main_pattern(pattern_list[18], rate)
        print("20 measure")
        play_main_pattern(pattern_list[19], rate)
        print("21 measure")
        play_main_pattern(pattern_list[20], rate)
        print("22 measure")
        play_main_pattern(pattern_list[21], rate)
        print("23 measure")
        play_main_pattern(pattern_list[22], rate)
        print("24 measure")
        play_main_pattern(pattern_list[23], rate)
        print("25 measure")
        play_main_pattern(pattern_list[24], rate)
        print("26 measure")
        play_main_pattern(pattern_list[25], rate)
        print("27 measure")
        play_main_pattern(pattern_list[26], rate)
        print("28 measure")
        play_main_pattern(pattern_list[27], rate)
        print("29 measure")
        play_main_pattern(pattern_list[28], rate)
        print("30 measure")
        play_main_pattern(pattern_list[29], rate)
        print("31 measure")
        play_main_pattern(pattern_list[30], rate)
        print("32 measure")
        play_main_pattern(pattern_list[31], rate)
        print("33 measure")
        play_main_pattern(pattern_list[32], rate)
        print("34 measure")
        play_main_pattern(pattern_list[33], rate)
        print("35 measure")
        play_main_pattern(pattern_list[34], rate)
        # finish with the ending function which plays the final notes
        play_ending(rate + .2)
    except KeyboardInterrupt:
        print("KeyboardInterrupt Exception handled")
        GPIO.cleanup()




if __name__ == '__main__':
    main(.1)






