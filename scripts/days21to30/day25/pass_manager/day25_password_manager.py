from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please make sure all fields are populated")
    else:
        try:
            with open("data.json", "r") as data:
                json_data = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            json_data.update(new_data)
            with open("data.json", "w") as data:
                json.dump(json_data, data, indent=4)
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)


def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as data:
            info = json.load(data)
            data_file = info[website]
            email = data_file["email"]
            password = data_file["password"]
    except KeyError:
        messagebox.showinfo(title="Warning", message="I'm sorry, that password has not been saved in this database")
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="The password manager is currently empty, search is unavailable")
    else:
        messagebox.showinfo(title=website, message=f"The email is {email} and the password is {password}")


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

website_input = Entry(width=27)
website_input.grid(column=1, row=1)

website_search = Button(text="Search", width=15, command=search)
website_search.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=42)
email_input.insert(0, "alex@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_input = Entry(width=27)
pass_input.grid(column=1, row=3)

pass_button = Button(text="Generate password", command=password_gen)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
