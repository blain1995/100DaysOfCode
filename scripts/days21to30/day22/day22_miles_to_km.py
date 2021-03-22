import tkinter

window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(width=250, height=150)
window.config(padx=60, pady=70)

user_input = tkinter.Entry(width=10)
user_input.grid(column=0, row=0)

label1 = tkinter.Label(text="Miles")
label1.grid(column=1, row=0)


def convert():
    miles = user_input.get()
    km = round(float(miles) * 1.689)
    label2["text"] = f"is equal to {km} km"


label2 = tkinter.Label(text=f"is equal to km")
label2.grid(column=0, row=1)

button = tkinter.Button(text="Caclulate", command=convert)
button.grid(column=0, row=2)

window.mainloop()
