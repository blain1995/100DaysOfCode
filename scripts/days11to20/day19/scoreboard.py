from turtle import Turtle, Screen
FONT = ("Courier", 30, "bold")
ALIGN = "center"
POSITION_1 = (-50, 260)
POSITION_2 = (50, 260)
CENTRE = (0, 300)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.speed('fastest')
        self.penup()
        self.penup()
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.goto(CENTRE)
        self.pendown()
        self.setheading(270)

        for i in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()

        self.penup()
        self.goto(POSITION_1)
        self.write(f"{self.score1}", False, ALIGN, FONT)
        self.goto(POSITION_2)
        self.write(f"{self.score2}", False, ALIGN, FONT)

    def game_over(self, player):
        if player == "left":
            self.write("GAME OVER, PLAYER ONE WINS", False, ALIGN, ("Courier", 40, "bold"))
        else:
            self.write("GAME OVER, PLAYER TWO WINS", False, ALIGN, ("Courier", 40, "bold"))