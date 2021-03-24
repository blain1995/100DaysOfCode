from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_sym = [choice(symbols) for _ in range(randint(2, 4))]
    pass_nums = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_sym + pass_nums
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    with open("data.txt", "a") as data:
        website = website_input.get()
        email = email_input.get()
        password = pass_input.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Warning", message="Please make sure all fields are populated")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \n "
                                                          f"Password: {password} \n Are you happy to save?")
            if is_ok:
                data.write(f"{website} | {email} | {password} \n")
                website_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.insert(0, "alex@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_input = Entry(width=27)
pass_input.grid(column=1, row=3)

pass_button = Button(text="Generate", command=password_gen)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
