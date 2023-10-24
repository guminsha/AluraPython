import random
import os


def introdution():
    print("****************************")
    print("Welcome to Hangman!")
    print("****************************")


def draw_hang(lifes):
    print("  _______     ")
    print(" |/      |    ")

    if(lifes == 4):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(lifes == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(lifes == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    
    if(lifes == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |        \   ")

    if (lifes == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def create_secret_word():
    file = open(os.path.join("AluraPython/curso_2/aula_jogos/frutas.txt"))
    with open(os.path.join("AluraPython/curso_2/aula_jogos/frutas.txt")) as file:
        fruit_list = file.read().split(", ")
    file.close()

    secret_word = random.choice(fruit_list).upper()

    return secret_word


def create_guess(caracters):
    while True:
        guess = input("Enter a letter: ").upper().strip()
        if len(guess) > 1 or guess.isdecimal() or guess in caracters:
            print("Invalid entry, try again")
        else:
            break

    return guess


def check_correct_guess(guess, word, caracters):
    index = 0
    for letter in word:
        if guess == letter:
            caracters[index] = letter
        index += 1

    return caracters


def check_wrong_guess(guess, word, lifes):
    if guess not in word:
        lifes -= 1

    return lifes


def check_win(caracters, word):
    right_awnser = "_" not in caracters

    if right_awnser:
        return True
    else:
        return False


def check_death(lifes):
    if lifes == 0:
        return True
    else:
        return False


def play():
    introdution()
    
    secret_word = create_secret_word()
    lifes = 5
    correct_caracters = ["_" for _ in secret_word]  # _ = a not used variable
    correct = False
    died = False

    draw_hang(lifes)

    while not correct and not died:
        print(f"You have {lifes} guesses")
        guess = create_guess(correct_caracters)

        correct_caracters = check_correct_guess(guess, secret_word, correct_caracters)
        lifes = check_wrong_guess(guess, secret_word, lifes)
        
        correct = check_win(correct_caracters, secret_word)
        died = check_death(lifes)

        draw_hang(lifes)
        print(correct_caracters)
    
    if correct:
        print("\nCongrats, you won!")
    else:
        print(f"\nYou lost!\nThe word was {secret_word.capitalize()}")
        
        

if __name__ == "__main__":
    play()
