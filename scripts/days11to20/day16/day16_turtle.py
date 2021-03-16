from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()
screen.listen()


def move_forwards():
    timmy.forward(10)


screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
