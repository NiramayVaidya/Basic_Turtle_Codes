import turtle

class Square:
    def create_square(self):
        self = turtle.Turtle()
        self.pensize(5)
        color = ['red', 'yellow', 'green', 'blue']
        for iter, col in zip(range(4), color):
            self.pencolor(col)
            self.forward(70)
            self.right(90)
        turtle.done()

def main():
    s = Square()
    s.create_square()

if __name__ == '__main__':
    main()
