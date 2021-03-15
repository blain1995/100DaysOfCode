from turtle import Turtle, Screen, colormode
import random

# Extract colours from image - only have to do once
# import colorgram
#
# palette = colorgram.extract('hirst.jpg', 16)
# colours = []
# for i in palette:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb = (r, g, b)
#     colours.append(rgb)
#
# print(colours)

colours_new = [(222, 241, 236), (112, 192, 125), (215, 167, 113), (228, 224, 126), (211, 127, 180),
               (249, 212, 218), (141, 147, 152), (17, 171, 216), (47, 53, 47), (71, 172, 132), (234, 85, 51),
               (244, 249, 252), (164, 79, 61), (67, 114, 95), (184, 100, 151)]

timmy = Turtle()
timmy.speed(0)
colormode(255)


def hirst_painting():
    timmy.penup()
    timmy.hideturtle()
    timmy.setx(-200)
    y = -200
    timmy.sety(y)
    for row in range(10):
        for col in range(10):
            timmy.dot(20, random.choice(colours_new))
            timmy.forward(50)
        y += 50
        timmy.sety(y)
        timmy.setx(-200)


hirst_painting()
screen = Screen()
screen.exitonclick()
