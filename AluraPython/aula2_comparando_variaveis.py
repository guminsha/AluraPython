import random

print("****************************")
print("Welcome to Guess the Number!")
print("****************************")

secret_number = random.randint(0, 10)
tries = 3

for i in range(1, tries+1):
	print(f"Round {i} of 3")
	# print("Round {} of 3".format(tries))

	number_guess = int(input("What is your guess? (0 to 10) "))

	if number_guess > 10 or number_guess < 0:
		print("You lost a try, your entry isn't valid")
		continue

	correct_guess = secret_number == number_guess
	lower_guess = number_guess < secret_number
	higher_guess = number_guess > secret_number

	if correct_guess:
		print("Correct!")
		break
	else:
		if lower_guess:
			print(f"Wrong! Your guess was lower than the secret number")
		elif higher_guess:
			print(f"Wrong! Your guess was higher than the secret number")
	

print(f"The secret number was {secret_number}")
