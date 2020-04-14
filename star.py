import turtle
import random

class Star():
    def create_star(self):
        self = turtle.Turtle()
        color = ['red', 'blue', 'green', 'yellow', 'orange']
        self.pensize(5)
        for iter in range(5):
            self.pencolor(random.choice(color))
            self.forward(70)
            self.right(144)
        turtle.done()
            
def main():
    s = Star()
    s.create_star()

if __name__ == '__main__':
    main()
