import random


def play():
	print("****************************")
	print("Welcome to Hangman!")
	print("****************************")

	lista = ["Banana", "Maca", "Uva", "Pera"]
	secret_word = random.choice(lista).lower()
	correct_guesses = ["_" for _ in secret_word]  # _ = a not used variable
	wrong_guesses = 5

	right_awnser = "_" not in correct_guesses
	died = wrong_guesses == 0

	while not right_awnser and not died:
		print(f"You have {wrong_guesses} guesses")
		while True:
			guess = input("Enter a letter: ").lower().strip()
			if len(guess) > 1 or guess.isdecimal() or guess in correct_guesses:
				print("Invalid entry, try again")
			else:
				break
		index = 0
		for letter in secret_word:
			if guess == letter:
				correct_guesses[index] = letter
			index += 1
		if guess not in secret_word:
			wrong_guesses -= 1

		print(correct_guesses)

		right_awnser = "_" not in correct_guesses
		died = wrong_guesses == 0


	if died:
		print("You lose!")
	else:
		print("Congrats, you won!")


if __name__ == "__main__":
	play()