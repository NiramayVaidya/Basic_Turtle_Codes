from turtle import Turtle, Screen
STAMP_SIZE = 20  # size of the square turtle shape
WIDTH, LENGTH = 25, 125
yertle = Turtle(shape="square")
yertle.penup()
yertle.turtlesize(WIDTH / STAMP_SIZE, LENGTH / STAMP_SIZE)
yertle.goto(100 + LENGTH//2, 100)  # stamps are centered, so adjust X
yertle.stamp()
screen = Screen()
screen.exitonclick()
