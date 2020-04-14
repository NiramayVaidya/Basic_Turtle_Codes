import turtle
import random

class Polygon:
    def __init__(self, sides, side_len):
        self.t = turtle.Turtle()
        self.sides = sides
        self.len = side_len
        self.angle = 360 / sides
        
    def create_polygon(self):
        for iter in range(self.sides):
            self.t.forward(self.len)
            self.t.right(self.angle)
        turtle.done()

class ColouredPolygon(Polygon):
    def __init__(self, sides, side_len, color):
        self.color = color
        super().__init__(sides, side_len)

    def create_polygon(self):
        for iter in range(self.sides):
            self.t.pencolor(random.choice(self.color))
            self.t.forward(self.len)
            self.t.right(self.angle)
        turtle.done()

def main():
    '''
    p = Polygon(5, 70)
    p.create_polygon()
    '''
    color = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan']
    p = ColouredPolygon(10, 60, color)
    p.create_polygon()

if __name__ == '__main__':
    main()

