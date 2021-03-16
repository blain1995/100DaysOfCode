from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    timmy.forward(50)


def move_backwards():
    timmy.backward(50)


def anti_clockwise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clockwise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def clear():
    timmy.reset()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.exitonclick()
