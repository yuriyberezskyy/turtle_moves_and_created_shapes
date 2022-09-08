import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("red")

repeat = 0

# while repeat < 4:
#     tim.forward(100)
#     tim.right(90)
#     repeat += 1

# Draw dashes
# while repeat < 10:
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     repeat+=1

# Draw shapes of geometry
# for i in range(3,10):
#     y = 0
#     while y < i:
#         tim.right(360 / i)
#         tim.forward(100)
#         y+=1

#Draw random way lines
# count = 0
# arr_moves = [90, 180, 270]
# arr_colors = ["red", "green", "blue", "black", "orange"]
# while count < 1000:
#     tim.pen(pensize=10)
#     tim.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     tim.speed(8)
#     tim.right(random.choice(arr_moves))
#     tim.forward(25)
#     count += 1

#draw circle
i=0
while i < 360:
    tim.right(i)
    tim.speed(10)
    tim.circle(100,None,10)
    i+=3

screen = Screen()
screen.exitonclick()