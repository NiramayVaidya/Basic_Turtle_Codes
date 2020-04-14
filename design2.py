import turtle 

class Design2:
    def create_design_2(self):
        turtle.bgcolor('black')
        self = turtle.Turtle()
        self.speed(50)
        for i in range(180):
            self.pencolor('#000080')
            self.forward(40)
            if i < 60:
                self.pencolor('#FF9933')
            elif i >= 60 and i < 120:
                self.pencolor('#FFFFFF')
            else:
                self.pencolor('#138808')
            self.forward(60)
            self.right(30)
            self.forward(20)
            self.left(60)
            self.forward(50)
            self.right(30)                            
            self.penup()
            self.setposition(0, 0)
            self.pendown()                                            
            self.right(2)
        turtle.done()

def main():
    d2 = Design2()
    d2.create_design_2()

if __name__ == '__main__':
    main()
