import pandas as pd
alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
print(alphabet)
alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

word = input("Type word to convert: ").upper()
nato_list = [alphabet_dict[letter] for letter in word]
print(nato_list)
