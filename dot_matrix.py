import turtle
import random

class Dot_matrix:
    def create_dot_matrix(self):
        self = turtle.Turtle()
        dot_distance = 25
        width = 5
        height = 7
        self.penup()
        color = ['red', 'blue', 'green', 'yellow', 'cyan', 'orange']
        for y in range(height):
            for i, col in zip(range(width), color):
                self.pencolor(random.choice(color))
                self.dot()
                self.forward(dot_distance)
            self.backward(dot_distance * width)
            self.right(90)
            self.forward(dot_distance)
            self.left(90)
        turtle.done()

def main():
    dot_mat = Dot_matrix()
    dot_mat.create_dot_matrix()

if __name__ == '__main__':
    main()
