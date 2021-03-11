# This is a simplified version of BlackJack, the rules are as follows:

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from os import system, name
from day9_art import logo


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(input_cards):
    input_cards.append(random.choice(cards))


def calculate_score(player):
    answer = sum(player)
    for card in player:
        if card == 11 and answer > 21:
            player.remove(11)
            player.append(1)
            answer = sum(cards)
    return answer


def computer_turn():
    while calculate_score(computer_cards) < 17:
        deal_card(computer_cards)
    if calculate_score(computer_cards) == 0:
        print(f"Computer has BlackJack with these cards: {computer_cards}")
    elif calculate_score(computer_cards) > 21:
        print(f"""Congratulations, you win! The dealer had a final score of {calculate_score(computer_cards)}
              by drawing these cards: {computer_cards}""")
    elif calculate_score(user_cards) > calculate_score(computer_cards):
        print(f"Congratulations you win! The dealer drew these cards: {computer_cards}")
    elif calculate_score(user_cards) == calculate_score(computer_cards):
        print(f"""It's a draw! The dealer drew these cards: {computer_cards}""")
    else:
        print(f"""Computer has won with these cards: {computer_cards},
              better luck next time!""")


def go():
    draw_card = 'yes'
    for i in range(2):
        deal_card(user_cards)
        deal_card(computer_cards)
    while draw_card == 'yes':
        clear()
        print(logo)
        print(f"Your cards are {user_cards}")
        user_sum = calculate_score(user_cards)
        print(f"Your cards add up to {user_sum}")
        print(f"The dealers first card is {computer_cards[0]}, the other is hidden")
        if user_sum == 21:
            print("Congratulations, you have BlackJack!")
            draw_card = 'no'
            computer_turn()
        elif user_sum > 21:
            draw_card = 'no'
            print("Sorry, your cards are over 21 - you lose!")
        else:
            draw_card = input("Do you want to draw another card? 'yes' or 'no':")
            if draw_card == 'yes':
                deal_card(user_cards)
            else:
                computer_turn()


while input("Do you want to play a game? 'yes' or 'no':") == 'yes':
    clear()
    user_cards = []
    computer_cards = []
    go()
print("Thanks for playing!")
