import turtle as t
import colorgram
import random

# Setup 
turtle = t.Turtle()
screen = t.Screen()
screen.setup(width=600, height=600)
t.speed(0)
t.colormode(255)
pen_size = 20
colors = colorgram.extract('image.jpg', 10)
print(colors)
#colors = ["coral", "seagreen", "chocolate","darkred"]

# Setup start position
turtle.hideturtle()
turtle.penup()
turtle_current_x = int(-screen.window_width()/2+pen_size)
turtle_current_y = int(-(screen.window_height()/2)+pen_size)
turtle.setposition(turtle_current_x, turtle_current_y)
#turtle.showturtle()
#turtle.pendown()
"""
0,0 = Center
-400 = left or bottom
400 = right or top
"""

# Draw
while turtle.xcor() < 400 and turtle.ycor() < 400:
# move forward to the right side and draw circles at even number intervalls
    distance_between_circles = int(screen.window_width()/pen_size)
    #for step in range(0, screen.window_width(), distance_between_circles):
    while turtle.xcor() < screen.window_width()/2-pen_size:
        # Pick random color of circle
        new_color = random.choice(colors)
        turtle.pencolor(new_color.rgb)
        turtle.dot(pen_size)
        #turtle.pensize(pen_size)
        #turtle.pendown()
        #turtle.forward(1)
        #turtle.penup()
        turtle.forward(pen_size*1.5)

    
    turtle_current_y+=40
    turtle.setposition(turtle_current_x, turtle_current_y)
# Move up one row to the left 
# continue until at top right position


screen.exitonclick()