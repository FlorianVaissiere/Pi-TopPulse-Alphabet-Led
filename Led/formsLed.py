#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

# Display different forms on the pi-topPULSE led matrix
#
# Based on the script to display digits on pi-topPULSE

import ptpulse
from ptpulse import ledmatrix

import random

import re

import time

OFFSET_LEFT = 0
OFFSET_TOP = 0

NUMS = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1,  # 0
        0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,  # 1
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1,  # 2
        1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 3
        1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1,  # 4
        1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1,  # 5
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 6
        1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,  # 6
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,  # 8
        1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]  # 9

class Show(object):

    def __init__(self):
        self.r      = random.randrange(255)
        self.g      = random.randrange(255)
        self.b      = random.randrange(255)

    def show_digit(self, val, xd, yd):
        """show_digit

            Calculate position of leds on and off

            Attributes:
                val : number display
                xd  : width display
                yd  : height display
        """

        offset = val * 15
        for p in range(offset, offset + 15):
            xt = p % 3
            yt = (p-offset) // 3
            ledmatrix.set_pixel( xt+xd, 6-yt-yd, self.r*NUMS[p], self.g*NUMS[p], self.b*NUMS[p])
        ledmatrix.show()

    def show_letters_digits(self, val):
        """show_letters_digits

            Calculate number of 

            Attributes:
                val : number or letter
        """

        valStr = str(val)
        if re.search(valStr, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            
        else :
            value   = int(val)
            abs_val = abs(value)
            tens    = abs_val // 10
            units   = abs_val % 10
            if (abs_val > 9):
                self.show_digit(tens, OFFSET_LEFT, OFFSET_TOP)
            self.show_digit(units, OFFSET_LEFT+4, OFFSET_TOP)
    


###############################################################################
# MAIN                                                                        #
###############################################################################
if __name__ == '__main__':
    ledmatrix.rotation(0)
    ledmatrix.clear()

    led = Show()
    val = 0

    while True:
        if val <= 99:
            led.show_letters_digits(val)
            time.sleep(0.1)
            val = val + 1

        if val > 99 and val < 104:
            ledmatrix.clear()
            ledmatrix.show()
            if val == 100:
                led.show_letters_digits('A')
                time.sleep(1)
                ledmatrix.clear()
                ledmatrix.show()

            if val == 101:
                led.show_letters_digits('B')
                time.sleep(1)
                ledmatrix.clear()
                ledmatrix.show()

            if val == 102:
                led.show_letters_digits('C')
                time.sleep(1)
                ledmatrix.clear()
                ledmatrix.show()

            if val == 103:
                led.show_letters_digits('L')
                time.sleep(1)
                ledmatrix.clear()
                ledmatrix.show()
            val = val + 1       
        if val >= 104:
            ledmatrix.clear()
            ledmatrix.show()
            val = 0 
            led.show_letters_digits(val)
            time.sleep(0.1)
            val = val + 1

    ledmatrix.clear()
    ledmatrix.show()