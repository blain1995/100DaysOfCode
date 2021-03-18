from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT,font=("Courier", 24, "bold"))
        self.goto(0, -50)
        self.write(f"Final score is {self.score}", False, align=ALIGNMENT, font=("Courier", 24, "bold"))
