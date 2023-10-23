import random


def play():
	print("****************************")
	print("Welcome to Hangman!")
	print("****************************")

	lista = ["banana", "maca", "uva", "pera"]
	secret_word = random.choice(lista)
	
	correct_awnser = False
	died = False

	while not correct_awnser or  not died:
		print("jogando")

	print("GAME OVER")


if __name__ == "__main__":
	play()