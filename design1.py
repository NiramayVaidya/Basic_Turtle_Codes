import turtle 

class Design1:
    def create_design_1(self):
        self = turtle.Turtle()
        self.speed(10)
        self.pencolor('#c68a3b')
        for i in range(180):
            self.forward(100)
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
    d = Design1()
    d.create_design_1()

if __name__ == '__main__':
    main()
    
