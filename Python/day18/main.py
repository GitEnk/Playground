import turtle as t
from turtle import Screen
import random
#import tkinter as tk

colors = ["coral", "seagreen", "chocolate","darkred"]
headings = [0, 90, 180, 270, 360]
def draw_dashed(length):
    for _ in range(0,length, 10):
        turtle.pendown()
        turtle.forward(length/10)
        turtle.penup()
        turtle.forward(length/10)

def random_walk():
    turtle.pencolor(random_color())
    print(turtle.color())
    turtle.setheading(random.choice(headings))
    turtle.forward(30)


def random_color():
    return (random.randrange(10,245),random.randrange(10,245),random.randrange(10,245))

turtle = t.Turtle()
t.colormode(255)
turtle.pensize(1)
turtle.speed(0)

start = 0
stop = 360
steps = 10
angle = 0
for step in range(start, stop, steps):
    turtle.pencolor(random_color())
    turtle.circle(100)
    angle+=steps
    turtle.setheading(angle)
"""
# Random Walk
for steps in range(100):
    random_walk()
"""

"""
turtle.color("seagreen")
for s in range(3,11):
    angle = 360/s
    for a in range(0, s):
        turtle.forward(100)
        turtle.right(angle)
"""
   
"""
for _ in range(4):
    draw_dashed(44)
    turtle.left(90)
"""

screen = Screen()
screen.exitonclick()
