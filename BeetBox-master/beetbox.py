#!/usr/bin/env python

"""beetbox.py: Trigger script for the BeetBox."""

__author__ = "Scott Garner"
__email__ = "scott@j38.net"

import pygame

import RPi.GPIO as GPIO
import mpr121

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

#*Allow for students to add their own sounds. Provide one sound and let students figure out the rest they want to add.
kick = pygame.mixer.Sound('samples/kick.wav')
kick.set_volume(.65);
snare = pygame.mixer.Sound('samples/snare.wav')
snare.set_volume(.65);
openhh = pygame.mixer.Sound('samples/open.wav')
openhh.set_volume(.65);
closedhh = pygame.mixer.Sound('samples/closed.wav')
closedhh.set_volume(.65);
clap = pygame.mixer.Sound('samples/clap.wav')
clap.set_volume(.65);
cymbal = pygame.mixer.Sound('samples/cymbal.wav')
cymbal.set_volume(.65);

# Track touches

touches = [0,0,0,0,0,0];


while True:

	#*check if the interupt pin has a high signal. if so, pass
	#*based on the capacitance of the specific beet
	#IRQ is the Interrupt Request signal pin. It is pulled up to 3.3V on the breakout and when the sensor chip detects a change in the touch sense switches, the pin goes to 0V until the data is read over i2c
	if (GPIO.input(7)): # Interupt pin is high
		pass
	#*otherwise 
	else: # Interupt pin is low

		touchData = mpr121.readData(0x5a)
		#*loop through each beet and check if the pin is activated.


		for i in range(6):
			#*give information about bitwise manipulation
			if (touchData & (1<<i)):

				#*if the beet is not touched, print the beet that was touched and play the associated wav file
				if (touches[i] == 0):

					print( 'Pin ' + str(i) + ' was just touched')

					#*play the corresponding sound based on beet touched
					if (i == 0):
						kick.play()
					elif (i == 1):
						snare.play()
					elif (i == 2):
						openhh.play()
					elif (i == 3):
						closedhh.play()
					elif (i == 4):
						clap.play()
					elif (i == 5):
						cymbal.play()

				#*Change the status of specific beet to 'touched'
				touches[i] = 1;

			#*else statement for if the beet is being touched
			else:
				if (touches[i] == 1):
					print( 'Pin ' + str(i) + ' was just released')
				#*reset status of corresponding pin to being touched
				touches[i] = 0;
