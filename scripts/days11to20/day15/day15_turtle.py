from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for i in range(50):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()
#
# shapes = {
#     "triangle": 3,
#     "square": 4,
#     "pentagon": 5,
#     "hexagon": 6,
#     "heptagon": 7,
#     "octagon": 8,
#     "nonagon": 9,
#     "decagon": 10
# }
#
#
# def draw(shape):
#     sides = shapes[shape]
#     angle = 360/sides
#     for j in range(sides):
#         timmy.forward(100)
#         timmy.left(angle)
#
#
# for item in shapes:
#     draw(item)

directions = [0, 90, 180, 270]
colours = ["coral", "red", "blue", "purple", "black", "grey", "green", "yellow"]

timmy.pensize(1)
timmy.speed("fastest")
colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def random_walk():
    for steps in range(300):
        timmy.color(random_colour())
        timmy.forward(20)
        timmy.setheading(random.choice(directions))


def spirograph(size):
    for step in range(90):
        timmy.color(random_colour())
        timmy.circle(size)
        timmy.left(4)


# random_walk()
spirograph(100)
screen = Screen()
screen.exitonclick()
