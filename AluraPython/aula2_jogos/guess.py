import random


def play():
	print("****************************")
	print("Welcome to Guess the Number!")
	print("****************************")

	secret_number = random.randint(0, 100)
	tries = 0
	score = 300

	print("Easy: 1\nMedium: 2\nHard: 3")
	difficult = int(input("Select difficult: "))

	match difficult:
		case 1:
			tries = 10
		case 2:
			tries = 5
		case 3:
			tries = 3

	print(tries)

	for i in range(1, tries+1):
		print(f"Round {i} of {tries}")
		# print("Round {} of 3".format(tries))

		number_guess = int(input("What is your guess? (0 to 100) "))

		if number_guess > 100 or number_guess < 0:
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
				score -= abs(secret_number - number_guess)
			elif higher_guess:
				print(f"Wrong! Your guess was higher than the secret number")
				score -= abs(secret_number - number_guess)
		

	print(f"Score: {score}\nThe secret number was {secret_number}")


if __name__ == "__main__":
	play()
