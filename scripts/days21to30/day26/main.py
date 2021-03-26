from tkinter import *
import pandas as pd
from random import *
BACKGROUND_COLOR = "#B1DDC6"

# --------------------- Functions----------------------------
try:
    words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original = pd.read_csv("data/french_words.csv")
    words_dict = original.to_dict(orient="records")
else:
    words_dict = words.to_dict(orient="records")

current_card = {}


def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = choice(words_dict)
    french_word = current_card["French"]
    canvas.itemconfig(card, image=front_card)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(chosen_word, text=french_word, fill="black")

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(chosen_word, text=current_card["English"], fill="white")


def correct():
    words_dict.remove(current_card)
    data = pd.DataFrame(words_dict)
    pd.DataFrame.to_csv(data, "data/words_to_learn.csv", index=False)
    new_word()


# --------------------- Set up GUI----------------------------
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# Load in all the images needed
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
cross_image = PhotoImage(file="images/wrong.png")
tick_image = PhotoImage(file="images/right.png")

# Create the Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
chosen_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Create buttons
wrong_button = Button(image=cross_image, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=tick_image, highlightthickness=0, command=correct)
right_button.grid(column=1, row=1)

new_word()
window.mainloop()
