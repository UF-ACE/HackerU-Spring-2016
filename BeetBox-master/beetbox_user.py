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

''' ADD 4 MORE SOUNDS USING FORMAT BELOW. LOOK THROUGH SAMPLES FOLDER AND PICK. ADD VOLUME AS APPROPRIATE '''

kick = pygame.mixer.Sound('samples/kick.wav')
kick.set_volume(.65);

snare = pygame.mixer.Sound('samples/snare.wav')
snare.set_volume(.65);

# openhh = pygame.mixer.Sound('samples/open.wav')
# openhh.set_volume(.65);
# closedhh = pygame.mixer.Sound('samples/closed.wav')
# closedhh.set_volume(.65);
# clap = pygame.mixer.Sound('samples/clap.wav')
# clap.set_volume(.65);
# cymbal = pygame.mixer.Sound('samples/cymbal.wav')
# cymbal.set_volume(.65);

# Track the touches with this array. If a beet has been touched, the corresponding value in the array becomes 1
touches = [0,0,0,0,0,0];

while True:

	#*Understand/explain interrupt pin
	# check if the interupt pin has a high signal. if so, pass
	# based on the capacitance of the specific beet
	# IRQ is the Interrupt Request signal pin. It is pulled up to 3.3V on the breakout and when the sensor chip detects a change in the touch sense switches, the pin goes to 0V until the data is read over i2c
	if (GPIO.input(7)): # Interupt pin is high
		pass
 
	else: # Interupt pin is low

		touchData = mpr121.readData(0x5a)
		#*explain loop through each beet and check if the pin is activated.


		for i in range(6):
			#*give information about bitwise manipulation
			if (touchData & (1<<i)):

				#*explain if the beet is not touched, print the beet that was touched and play the associated wav file
				if (touches[i] == 0):

					''' ADD A PRINT STATEMENT TO OUTPUT WHICH PIN WAS TOUCHED '''
					print( 'Pin ' + str(i) + ' was just touched')

					''' USE PYGAME .PLAY() METHOD TO PLAY EACH SOUND BASED ON PIN (i VALUE) TOUCHED'''
					# if (i == 0):
					# 	kick.play()
					# elif (i == 1):
					# 	snare.play()
					# elif (i == 2):
					# 	openhh.play()
					# elif (i == 3):
					# 	closedhh.play()
					# elif (i == 4):
					# 	clap.play()
					# elif (i == 5):
					# 	cymbal.play()

				''' SET THE PIN'S VALUE IN THE touches ARRAY TO TRUE (1) '''
				touches[i] = 1;

			#* explain else statement for if the beet is being touched
			else:
				if (touches[i] == 1):

					''' ADD A PRINT STATEMENT TO OUTPUT WHICH PIN WAS RELEASED '''
					print( 'Pin ' + str(i) + ' was just released')
				
				''' SET THE PIN'S VALUE IN THE touches ARRAY TO FALSE (0) '''
				touches[i] = 0;
