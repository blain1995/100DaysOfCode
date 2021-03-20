from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font= FONT)

    def show_score(self):
        self.goto(-210, 270)
        self.write(f"Level: {self.level}", False, align="center", font=FONT)