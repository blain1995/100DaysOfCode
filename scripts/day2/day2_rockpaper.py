import random2
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]

choice = int(input("Type 0 for rock, 1 for paper, 2 for scissors"))

if choice >= 3 or choice < 0:
    print("The number you entered is invalid")
else:
    print(f"You chose {images[choice]}")

comp_choice = random2.randint(0, 2)
print(f"Computer chose {images[comp_choice]}")

if choice == comp_choice:
    print('Draw!')
elif comp_choice == 0 and choice == 2:
    print("The computer wins")
elif comp_choice == 2 and choice == 0:
    print("You win!")
elif choice > comp_choice:
    print("You win!")
else:
    print("The computer wins")
