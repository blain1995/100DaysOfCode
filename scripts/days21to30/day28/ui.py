from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create canvas
        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR, width=280)

        # Create label
        self.score_label = Label(bg=THEME_COLOR, text=f"Score: {self.quiz.score}", fg="white",
                                 font=("Arial", 20, "italic"))
        self.score_label.grid(column=1, row=0)

        # Create buttons
        correct = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")
        self.correct_button = Button(image=correct, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)
        self.wrong_button = Button(image=wrong, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Congratulations, "
                                                            f"your final score was "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        outcome = self.quiz.check_answer("True")
        self.check_outcome(outcome)

    def false_pressed(self):
        outcome = self.quiz.check_answer("False")
        self.check_outcome(outcome)

    def check_outcome(self, is_right):
        if is_right:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
