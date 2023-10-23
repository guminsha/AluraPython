import guess
import hangman

print("****************************")
print("******Choose your game******")
print("****************************")

game_mode = False

while not game_mode:
	try:
		game_mode = int(input("\n1- Guess the number\n2- Hangman\n"))
	except ValueError:
		print("Not a number, try again")
		

guess_number = guess
hangman_game = hangman

match game_mode:
	case 1:
		guess_number.play()
	case 2:
		hangman_game.play()
	case _:
		print("Wrong entry")

