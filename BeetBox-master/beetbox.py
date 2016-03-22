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

''' INITIALIZE PYGAME. SYNTAX IS IN PACKET '''

''' ADD 4 MORE SOUNDS USING FORMAT BELOW. LOOK THROUGH SAMPLES FOLDER AND PICK. ADD VOLUME AS APPROPRIATE '''

kick = pygame.mixer.Sound('samples/kick.wav')
kick.set_volume(.65);

snare = pygame.mixer.Sound('samples/snare.wav')
snare.set_volume(.65);

# Track the touches with this array. If a beet has been touched, the corresponding value in the array becomes 1
touches = [0,0,0,0,0,0];

while True:

	# IRQ is the Interrupt Request signal pin. It is pulled up to 3.3V on the breakout and when the sensor chip detects a change in the touch sense switches, 
	# the pin goes to 0V until the data is read over i2c.

	# This if checks if the interupt pin has a high signal. if so, break the loop.
	if (GPIO.input(7)): # If the GPIO's pin 7 (Interupt) is high
		pass
 
	else: # Interupt pin is low

		# Reads data from mpr121 through default address value of 0x5a.
		touchData = mpr121.readData(0x5a)
		
		# Simultaneously loop through each beet and check if it is touched.
		for i in range(6):
			#*give information about bitwise manipulation
			if (touchData & (1<<i)):

				# If the beet i is not currently touched and is touched, print the beet that was touched, and play the corresponding wav file.
				if (touches[i] == 0):

					''' ADD A PRINT STATEMENT TO OUTPUT WHICH PIN WAS TOUCHED '''

					''' USE PYGAME .PLAY() METHOD TO PLAY EACH SOUND BASED ON PIN (i VALUE) TOUCHED'''

				''' SET THE PIN'S VALUE IN THE touches ARRAY TO TRUE (1) '''

			# Else, if the beet is currently being touched, print that it is released, when it is released.
			else:
				if (touches[i] == 1):

					''' ADD A PRINT STATEMENT TO OUTPUT WHICH PIN WAS RELEASED '''
				
				''' SET THE PIN'S VALUE IN THE touches ARRAY TO FALSE (0) '''
				touches[i] = 0;
