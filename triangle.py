import turtle

#equilateral triangle
class Triangle:
    def create_triangle(self):
        self = turtle.Turtle()
        color = ['red', 'blue', 'green']
        self.pensize(5)
        for iter, col in zip(range(3), color):
            self.pencolor(col)
            self.forward(70)
            self.right(120)
        turtle.done()

def main():
    t = Triangle()
    t.create_triangle()

if __name__ == '__main__':
    main()

