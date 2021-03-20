with open("Input/Names/invited_names.txt", "r") as names:
    all_names = names.readlines()


with open("Input/Letters/starting_letter.txt", "r+") as letter:
    template = letter.read()
    for name in all_names:
        stripped_name = name.strip()
        new = template.replace("[name]", stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as new_letter:
            new_letter.write(new)
