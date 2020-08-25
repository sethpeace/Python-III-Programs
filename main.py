# Seth Peace
# 8/24/2020
# This program is protected by all applicable copyright laws.
# An auto-catalogging system for all of the programs I will make in Python III this semester.
# Gaming (Unassigned)

import os

exit_loop = False
error     = False
quit      = False

def cls():
	os.system("clear")
	print("SETH PEACE - PYTHON III - ASSIGNMENT AUTO-CATALOGGER AND RETRIEVER")
	print("Check out the source code at https://github.com/sethpeace/Python-III-Programs")

while not quit:
	while not exit_loop:
		catalog = []
		cls()
		print("\nAuto-catalogging in progress, please wait.")
		for file in sorted(os.listdir(".")):
			if file.endswith(".py") and file != "main.py":
				catalog.append(file)
		
		cls()
		print("\nList of availible files (highlighted files are projects):")
		for i, file in enumerate(catalog):
			if file.endswith("_project.py"):
				print(f"\u001b[48;5;227m\u001b[30m({i+1:02d}) {file} \u001b[0m")
			else:
				print(f"({i+1:02d}) {file}")

		if error:
			print("\nThat was an invalid selection! Please try again.")
			error = False

		try:
			selection = int(input("\nPlease select a number: "))
		except (TypeError, ValueError):
			error = True
		else:
			if selection > len(catalog)+1 or selection < 1:
				error = True
			elif selection == 1:
				cls()
				print("\nThanks for trying out my application!")
				exit_loop = True
				quit = True
			else:
				exit_loop = True

	if not quit:
		exit_loop = False
		os.system("clear")
		os.system("python " + catalog[selection-1])
		input("\nThe Program Has Stopped. Press ENTER To Go Back To The Catalog.")
		os.system("clear")