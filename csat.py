import turtle

class Csat:
    def create_csat_logo(self):
        self = turtle.Turtle()
        self.speed(10)
        self.pendown()
        self.pensize(10)
        self.forward(50)
        self.penup()
        self.backward(50)
        self.pendown()
        self.left(180)
        self.circle(10, 90)
        self.forward(40)
        self.circle(10, 90)
        self.forward(50)
        self.penup()
        self.setposition(80, 0)
        self.pendown()
        self.forward(50)
        self.penup()
        self.backward(50)
        self.pendown()
        self.left(180)
        self.circle(10, 90)
        self.forward(10)
        self.circle(10, 90)
        self.forward(40)
        self.circle(-10, 90)
        self.forward(10)
        self.circle(-10, 90)
        self.forward(50)
        self.pencolor('red')
        self.penup()
        self.setposition(160, -60)
        self.pendown()
        self.right(115)
        self.forward(65)
        self.right(135)
        self.forward(63)
        self.penup()
        self.setposition(190, 20)
        self.pendown()
        self.pensize(1)
        self.right(90)
        self.circle(20, 20)
        self.penup()
        self.setposition(200, 30)
        self.pendown()
        self.right(40)
        self.circle(50, 40)
        self.penup()
        self.setposition(210, 40)
        self.pendown()
        self.right(60)
        self.circle(50, 80)
        self.penup()
        self.setposition(220, 50)
        self.pendown()
        self.right(98)
        self.circle(50, 120)
        self.penup()
        self.setposition(130, 50)
        self.pendown()
        self.pencolor('black')
        self.left(65)
        self.circle(50, 120)
        self.penup()
        self.setposition(140, 60)
        self.pendown()
        self.right(100)
        self.circle(50, 80)
        self.penup()
        self.setposition(150, 70)
        self.pendown()
        self.right(60)
        self.circle(50, 40)
        self.penup()
        self.setposition(160, 85)
        self.pendown()
        self.right(40)
        self.circle(20, 25)
        self.penup()
        self.setposition(155, 95)
        self.pendown()
        self.pensize(6)
        self.left(45)
        for iter in range(4):
            self.forward(5)
            self.right(90)
        self.right(77)
        self.penup()
        self.setposition(230, 0)
        self.pensize(10)
        self.pendown()
        self.forward(60)
        self.penup()
        self.backward(30)
        self.right(90)
        self.pendown()
        self.forward(60)
        self.penup()
        self.setposition(145, -20)
        self.pendown()
        self.left(135)
        '''
        the following code generates a filled ellipse with white color
        which previously generated figure, there isn't any utility in
        turtle for drawing an outline of a shape with no fill
        note-wanted to display the orbit of the satellite, the
        following code being an effort to do the same
        '''
        self.shape('circle')
        self.shapesize(10, 15, 1)
        self.fillcolor('white')
        turtle.done()

def main():
    cs = Csat()
    cs.create_csat_logo()

if __name__ == '__main__':
    main()
