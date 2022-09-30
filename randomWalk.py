import random
from turtle import Turtle, Screen
import turtle


def moveRight():
    myTurtle.right(90)
    myTurtle.forward(30)


def moveLeft():
    myTurtle.left(90)
    myTurtle.forward(30)


def moveForward():
    myTurtle.forward(30)


def moveBackward():
    myTurtle.right(180)
    moveForward()


myTurtle = Turtle()
colours = ["#000000", "#00BFFF", "#000080", "#00FF00", "#8B0000", "#9370DB", "#483D8B", "#BC8F8F", "#FFFF00", "#808080"]
movement = ["right", "left", "forward", "backward"]
myTurtle.width(4)

for i in range(250):
    chosen = random.choice(movement)
    myTurtle.color(random.choice(colours))
    if chosen == "right":
        moveRight()
    elif chosen == "left":
        moveLeft()
    elif chosen == "forward":
        moveForward()
    elif chosen == "backward":
        moveBackward()

screen = turtle.Screen()
screen.exitonclick()
