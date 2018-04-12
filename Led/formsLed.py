#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Display different forms on the pi-topPULSE led matrix
#
# Based on the script to display digits on pi-topPULSE

import ptpulse
from ptpulse import ledmatrix

import random

import re

import time

OFFSET_LEFT = 1
OFFSET_TOP = 1

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

REGEXP = r"(^[a-zA-Z]*)"

alphabet = {}






def show_digit(val, xd, yd, r, g ,b):
	"""show_digit

		Calculate position of leds on and off

		Attributes:
			val : number display
			xd  : width display
			yd  : height display
			r 	: red value
			g	: green value
			b   : blue value
	"""

	offset = val * 15
	for p in range(offset, offset + 15):
		xt = p % 3
		yt = (p-offset) // 3
		ledmatrix.set_pixel( xt+xd , 6-yt-yd , r*NUMS[p] , g*NUMS[p] , 
			b*NUMS[p])
	ledmatrix.show()

def show_letters_digits(val, r, g, b):
	"""show_letters_digits

		Calculate number of 

		Attributes:
			val : number or letter
			r 	: red value
			g	: green value
			b   : blue value
	"""

	"""if re.match(REGEXP, val) is not None:
		abs_val = ord(val)
		print (abs_val)
	else :"""
	value 	= int(val)
	abs_val = abs(value)
	tens 	= abs_val // 10
	units 	= abs_val % 10
	if (abs_val > 9):
		show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
	show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)

def show_L(r, g, b):
	#Vertical
	ledmatrix.set_pixel( 6 , 1 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])
	ledmatrix.set_pixel( 6 , 2 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])
	ledmatrix.set_pixel( 6 , 3 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])
	ledmatrix.set_pixel( 6 , 4 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])
	ledmatrix.set_pixel( 6 , 5 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])
	ledmatrix.set_pixel( 6 , 6 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])

	#Horizontal
	ledmatrix.set_pixel( 6 , 1 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])
	ledmatrix.set_pixel( 5 , 1 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])
	ledmatrix.set_pixel( 4 , 1 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])
	ledmatrix.set_pixel( 3 , 1 , r*NUMS[1] , g*NUMS[1] , b*NUMS[1])
	ledmatrix.show()
	


###############################################################################
# MAIN																		  #
###############################################################################
if __name__ == '__main__':
	ledmatrix.rotation(270)
	ledmatrix.clear()

	val = 0

	colorR = random.randrange(255)
	colorG = random.randrange(255)
	colorB = random.randrange(255)

	while True:
		show_L(colorR, colorG, colorB)
		"""if val <= 99:
			show_letters_digits(val, colorR, colorG, colorB)
			time.sleep(0.1)
			val = val + 1
		if val > 99:
			ledmatrix.clear()
			ledmatrix.show()
			val = 0 
			colorR = random.randrange(255)
			colorG = random.randrange(255)
			colorB = random.randrange(255)
			show_letters_digits(val, colorR, colorG, colorB)
			time.sleep(0.1)
			val = val + 1"""

	ledmatrix.clear()
	ledmatrix.show()