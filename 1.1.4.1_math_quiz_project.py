# Seth Peace
# 8/25/2020
# This program is protected by all applicable copyright laws.
# Randomly creates a 5-question math quiz for the user to take
# Gaming Assignment 1.1.4.1

import random, os, time

def cls():
	os.system("clear")
	print("SETH PEACE - PYTHON III - A MATH QUIZ")

NUM_PROBLEMS  = 10
math_problems = []
results       = []

for i in range(NUM_PROBLEMS):
	math_problem = str(random.randint(0, 12))
	math_problem += "*"
	math_problem += str(random.randint(0, 12))
	math_problems.append(math_problem)

cls()
input(f"\nWelcome to the math quiz!\nHere's how it works: we've randomly created {NUM_PROBLEMS} math problems involving multiplication.\nYou'll have to tell us the answers.\nAt the end, you can see how many you got right and how long it took you!\nReady? Hit ENTER to continue!")

total_start = time.time()
for math_problem in math_problems:
	start = time.time()
	cls()
	print("")
	print(math_problem)
	try:
		answer = int(input("\nEnter the answer: "))
	except (TypeError, ValueError):
		answer = None
	if answer == eval(math_problem):
		results.append({"correct": True, 
						"time": time.time()-start,
						"answer": answer,
						"correct_answer": eval(math_problem),
						"problem": math_problem})
	else:
		results.append({"correct": False,
						"time": time.time()-start,
						"answer": answer,
						"correct_answer": eval(math_problem),
						"problem": math_problem})

cls()
print("\nAnd that's the end! Check out how you did:\n[ ", end='')
num_correct = 0
for result in results:
	if result["correct"]:
		print("✓ ", end='')
		num_correct += 1
	else:
		print("✗ ", end='')
print(f"] {num_correct}/{NUM_PROBLEMS} - Time: {time.time()-total_start:.2f} sec\n")
for result in results:
	answer         = result["answer"]
	correct_answer = result["correct_answer"]
	time_          = result["time"]
	problem        = result["problem"]
	if result["correct"]:
		print(f" ✓ {problem:>5} - You Said: {answer:>3} - Answer: {correct_answer:>3} - Time: {time_:>5.2f} sec")
	else:
		print(f" ✗ {problem:>5} - You Said: {answer:>3} - Answer: {correct_answer:>3} - Time: {time_:>5.2f} sec")