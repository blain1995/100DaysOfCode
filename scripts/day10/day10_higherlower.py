# Import modules
import random
from day10_art import logo2, vs
from day10_gamedata import data
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def pull_data():
    return random.choice(data)
# Build a comparison function


def compare(account_a, account_b):
    """Compares to see if the answer is correct"""
    choice = input(f"Does {account_b['name']} have a higher or lower follower count? :")
    if choice == 'higher' and account_a['follower_count'] < account_b['follower_count']:
        return True
    elif choice == 'higher' and account_a['follower_count'] > account_b['follower_count']:
        return False
    elif choice == 'lower' and account_a['follower_count'] > account_b['follower_count']:
        return True
    elif choice == 'lower' and account_a['follower_count'] < account_b['follower_count']:
        return False
    else:
        print("correct input required")
        return False


def game():
    score = 0
    result = True
    account_a = pull_data()
    account_b = pull_data()
    while result:
        print(logo2)
        print(f"Your current score is {score}")
        print(f"Choice A is {account_a['name']} who is a {account_a['description']} from {account_a['country']}")
        print(vs)
        print(f"Choice B is {account_b['name']} who is a {account_b['description']} from {account_b['country']}")
        result = compare(account_a, account_b)

        if result:
            score += 1
            account_a = account_b
            account_b = pull_data()

        if account_a == account_b:
            account_b = pull_data()
        print(f"That's correct! Your score is {score}")
        clear()

    print(f"Sorry that is incorrect, better luck next time. Your final score is {score}")


game()
while input("Do you want to play again? 'yes' or 'no': ") == 'yes':
    game()
print("Thanks for playing!")
