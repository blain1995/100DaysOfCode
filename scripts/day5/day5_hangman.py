from random_word import RandomWords
r = RandomWords()

print("Welcome to hangman :)")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
difficulty = input("choose difficulty: easy, medium, hard:")
if difficulty == "easy":
    max_len = 4
elif difficulty == "medium":
    max_len = 6
elif difficulty == "hard":
    max_len = 10
else:
    print("The value inputted is not a valid option")
    max_len = 0
    end_of_game = True

chosen_word = str(r.get_random_word(hasDictionaryDef="true", maxLength=max_len))

hangman = []
for i in range(len(chosen_word)):
    hangman += "_"

print(hangman)

lives = 6

end_of_game = False
hangman_index = -1

while end_of_game == False:
    guess = input("choose a letter:").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            hangman[i] = letter
    if guess not in chosen_word:
        lives -= 1
        hangman_index -= 1
    print(hangman)
    print(stages[hangman_index])
    if "_" not in hangman:
        end_of_game = True
        print("Congratulations, you won!")
    if lives == 0:
        end_of_game = True
        print(f"Better luck next time! The word was {chosen_word}")
