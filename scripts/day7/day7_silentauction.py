from day7_art import logo
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


auction = {}
bidder = "yes"
bid_object = input("What are we bidding on today?:")

while bidder == "yes":
    print(logo)
    name = input("what is your name? :")
    bid = float(input(f"what is your bid for {bid_object}? :£"))
    auction[name] = bid
    bidder = input("is there another bidder? 'yes' or 'no:").lower()
    clear()

highest_bid = 0
winner = ""
for key in auction.keys():
    if auction[key] > highest_bid:
        highest_bid = auction[key]
        winner = key

print(f"""The winner is {winner} with the highest bid of £{highest_bid},
congratulations, you have won {bid_object}""")
