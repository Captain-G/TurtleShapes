import turtle
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.color("grey")

for i in range(4, 11):
    angle = 360 / i
    for j in range(i):
        turtle.right(angle)
        turtle.forward(50)


screen = turtle.Screen()
screen.exitonclick()

