# draw an equilateral triangle
import turtle

wn = turtle.Screen()
norvig = turtle.Turtle()

for i in range(3):
    norvig.forward(100)

    # the angle of each vertices of a regular polygon
    # is 360 divided by the number of sides
    norvig.left(360/3)

wn.exitonclick()
# draw a square
import turtle

wn = turtle.Screen()
kurzweil = turtle.Turtle()

for i in range(4):
    kurzweil.forward(100)
    kurzweil.left(360/4)

wn.exitonclick()
# draw a hexagon
import turtle

wn = turtle.Screen()
dijkstra = turtle.Turtle()

for i in range(6):
    dijkstra.forward(100)
    dijkstra.left(360/6)

wn.exitonclick()
# draw an octagon
import turtle

wn = turtle.Screen()
knuth = turtle.Turtle()

for i in range(8):
    knuth.forward(75)
    knuth.left(360/8)

wn.exitonclick()