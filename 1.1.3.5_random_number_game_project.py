# Seth Peace
# 8/24/2020
# This program is protected by all applicable copyright laws.
# Plays a number-guessing game with the user
# Gaming Assignment 1.1.3.5

import os, random

def cls():
	os.system("clear")
	print("SETH PEACE - THE NUMBER-GUESSER GAME")

number          = random.randint(0, 50)
guesses         = 0
quit            = False
msg             = "\nTry your luck and\nmake a guess!"
GUESSES_ALLOWED = 5

cls()
input("\nHere's how it works: We came up with a number between 0 and 50.\nYou have to guess it (with a little help from us) within 5 tries.\nReady? Hit ENTER to start!")

while not quit:
	cls()
	print(msg)
	try:
		guess = int(input("\nWhat is your guess? "))
	except (TypeError, ValueError):
		msg = "\nThat was not a valid guess.\nPlease try again."
	else:
		if guess < 0 or guess > 50:
			msg = "\nThat was not a valid guess.\nPlease try again."
		else:
			guesses += 1
			if guess < number:
				msg = f"\n{guess} is too low!\nYou have {GUESSES_ALLOWED-guesses} guesses left."
			elif guess > number:
				msg = f"\n{guess} is too high!\nYou have {GUESSES_ALLOWED-guesses} guesses left."
			else:
				cls()
				print(f"\nYou won! The number was {number}!\nYou had {GUESSES_ALLOWED-guesses} guesses left.")
				print("\nGood Job!")
				quit = True
			if guess != number and guesses == GUESSES_ALLOWED:
				cls()
				print("\nYou've run out of guesses.")
				print(f"The number was {number}.")
				print("\nGame over!")
				quit = True