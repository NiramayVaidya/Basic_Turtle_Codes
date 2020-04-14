import turtle

class Ellipse:
    def create_ellipse(self):
        self = turtle.Turtle()
        self.left(45)
        self.shape("circle")
        self.shapesize(4, 5, 1)
        self.fillcolor("red")
        turtle.done()

def main():
    e = Ellipse()
    e.create_ellipse()

if __name__ == '__main__':
    main()
