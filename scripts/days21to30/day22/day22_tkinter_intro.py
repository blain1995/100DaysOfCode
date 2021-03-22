import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Ariel", 24, "normal"))
my_label.grid(column=0, row=0)


def button_clicked():
    my_label["text"] = user_input.get()


my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

new_button = tkinter.Button(text="Just for fun")
new_button.grid(column=2, row=0)

user_input = tkinter.Entry(width=10)
user_input.grid(column=4, row=3)
user_input.get()

window.mainloop()
