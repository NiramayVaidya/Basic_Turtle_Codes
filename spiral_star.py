import turtle
import random

class Spiral_star:
    def create_spiral_star(self):
        self = turtle.Turtle()
        color = ['blue', 'red', 'green', 'yellow']
        self.pensize(5)
        for iter in range(20):
            self.pencolor(random.choice(color))
            self.forward(iter * 20)
            #spiral_star.forward(iter * iter)
            self.right(144)
        turtle.done

def main():
    ss = Spiral_star()
    ss.create_spiral_star()

if __name__ == '__main__':
    main()
