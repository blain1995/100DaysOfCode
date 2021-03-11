from day6_decodeart import alphabet, logo
print(logo)


def caesar(input_text, shift_amount, version):
    output_text = ""
    if version == "decode":
        shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            index = alphabet.index(char)
            index_new = index + shift_amount
            output_text += alphabet[index_new]
        else:
            output_text += char
    print(f"The {direction}d text is {output_text}")


decision = True
while decision:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(input_text=text, shift_amount=shift, version=direction)
    continue_game = input("Would you like to re-run the cipher? Yes or No")
    if continue_game == "No":
        decision = False
        print("Goodbye!")
