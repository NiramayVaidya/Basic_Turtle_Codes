import math
from itertools import cycle
from turtle import Turtle, Screen

COLORS = cycle(['red', 'green', 'blue', 'yellow'])

def clip(subjectPolygon, clipPolygon):
    def inside(p):
        return(cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])

    def computeIntersection():
        dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ]
        dp = [ s[0] - e[0], s[1] - e[1] ]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0] 
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]

    outputList = subjectPolygon
    cp1 = clipPolygon[-1]

    for clipVertex in clipPolygon:
        cp2 = clipVertex
        inputList = outputList
        outputList = []
        s = inputList[-1]

        for subjectVertex in inputList:
            e = subjectVertex
            if inside(e):
                if not inside(s):
                    outputList.append(computeIntersection())
                    outputList.append(e)
                elif inside(s):
                    outputList.append(computeIntersection())
            s = e
            cp1 = cp2
    return(outputList)

def rotate_polygon(polygon, angle):

    theta = math.radians(angle)
    sin, cos = math.sin(theta), math.cos(theta)

    return [(x * cos - y * sin, x * sin + y * cos) for x, y in polygon]

def fill_polygon(turtle, polygon, color):

    turtle.color(color)

    for vertex in polygon:
        turtle.goto(vertex)
        if not turtle.filling():
            turtle.begin_fill()
            
    turtle.end_fill()
    
# triangle cursor 5x in size and X translated 50 pixels
polygon = ((100, -28.85), (50, 57.75), (0, -28.85))

screen = Screen()

yertle = Turtle(visible=False)
yertle.speed('slowest')  # slowly so we can see redrawing
yertle.penup()

polygons = []
POLYGON, COLOR = 0, 1

for angle in range(0, 360, 30):
        rotated_polygon = rotate_polygon(polygon, angle)
        color = next(COLORS)
        fill_polygon(yertle, rotated_polygon, color)
        polygons.append((rotated_polygon, color))

# The -3 here is empirical and really should be calculated, an exercise for the reader
for forward, backward in enumerate(range(-3, 1 - len(polygons), -1)):
    if polygons[forward] != polygons[backward]:
        try:
            intersection_polygon = clip(rotated_polygon, polygons[forward][POLYGON])
        except (IndexError, ZeroDivisionError):
            break  # because clip() can throw an error when no intersection

        if intersection_polygon:
            fill_polygon(yertle, intersection_polygon, polygons[forward][COLOR])
        else:
             break  # if no intersection, don't look any further
    else:
        break  # avoid testing against polygons clockwise from this one (needs work)

screen.exitonclick()
