import turtle

class Line:
    '''
    def __init__(self):
        self = turtle.Turtle()
    '''

    def create_line(self):
        self = turtle.Turtle()
        self.pensize(5)
        self.pencolor('#3e7bdd')
        self.forward(30)
        self.pencolor('#bf3ba2')
        self.forward(30)
        self.pencolor('#59bf3b')
        self.forward(30)
        turtle.done()

def main():
    l = Line()
    l.create_line()

if __name__ == '__main__':
    main()
