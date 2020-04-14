import turtle 

class Hexagon:
    def create_hexagon(self):
        self = turtle.Turtle()
        self.pensize(5)
        num_sides = 6
        side_length = 70
        angle = 360 / num_sides
        color = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan']
        for iter, col  in zip(range(num_sides), color):
            self.pencolor(col)
            self.forward(side_length)
            self.right(angle)
        turtle.done()

def main():
    h = Hexagon()
    h.create_hexagon()

if __name__ == '__main__':
    main()
