from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    reps = 0
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        mark = ""
        for _ in range(work_sessions):
            mark += "✓"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=300, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 150, image=photo)
canvas.grid(column=1, row=1)

timer_text = canvas.create_text(100, 170, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 48, "normal"))
label.grid(column=1, row=0)

button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", highlightthickness=0, command=timer_reset)
button2.grid(column=2, row=2)

check = Label(text="", fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()
