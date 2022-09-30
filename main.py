import turtle
import random
from turtle import Turtle, Screen

my_turtle = Turtle()
colours = ["#000000", "#00BFFF", "#000080", "#00FF00", "#8B0000", "#9370DB", "#483D8B", "#BC8F8F", "#FFFF00", "#808080"]

for i in range(4, 11):
    colour = random.choice(colours)
    my_turtle.color(colour)
    index = colours.index(colour)
    colours.pop(index)
    my_turtle.width(4)
    angle = 360 / i
    for j in range(i):
        my_turtle.right(angle)
        my_turtle.forward(80)


screen = turtle.Screen()
screen.exitonclick()

