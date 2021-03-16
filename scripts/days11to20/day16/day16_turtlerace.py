from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colours = ["red", "orange", "blue", "purple", "green"]
names = []
color_index = 0
y = -100

user_bet = screen.textinput(title="Place your bet", prompt="Which colour turtle will win?")
print(user_bet)

for i in range(5):
    new_turtle = Turtle("turtle")
    new_turtle.color(colours[color_index])
    color_index += 1
    new_turtle.penup()
    new_turtle.goto(-240, y)
    y += 50
    names.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in names:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Congratulations you won! The {winner} is the winner!")
            else:
                print(f"Sorry you lose. The winner is {winner}")
        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
