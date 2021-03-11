import random
from day10_art import logo
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def guess_game():
    print(logo)
    number = random.randint(1, 100)
    mode = input("Which mode would you like to play?: 'easy', 'hard': ")
    if mode == 'easy':
        lives = 10
    elif mode == 'hard':
        lives = 5
    else:
        lives = 0
        print("please input a valid mode")
    while lives > 0:
        print(f"You have {lives} attempts left")
        guess = int(input("Please guess an integer between 1 and 100: "))
        if guess > 100 or guess < 0:
            lives = 0
            print("Number inputted was not between 1 and 100, please try again")
        elif guess == number:
            lives = 0
            print(f"Congratulations! You win!")
        elif guess > number:
            lives -= 1
            print("Guess was too high!")
        else:
            lives -= 1
            print("Guess was too low")
    print("GAME OVER")


guess_game()
while input("Do you want to play again?'yes' or 'no': ") == 'yes':
    clear()
    guess_game()
print("Thank you for playing!")
