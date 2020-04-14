import turtle

painter = turtle.Turtle()

painter.pencolor("blue")
for iter in range(50):
    painter.forward(50)
    painter.left(123)
painter.pencolor("red")
for iter in range(50):
    painter.forward(100)
    painter.left(123)
turtle.done()
