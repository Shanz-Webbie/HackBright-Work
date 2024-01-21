import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

sides = int(input("Number of sides in polygon?"))
length = int(input("Length of the sides in polygon?"))
colorname = input("Color of polygon?")
fcolor = input("Fill color of polygon?")

alex.color = (colorname)
alex.fillcolor = (fcolor)

for i in range(sides):
    alex.forward(length)
    alex.left(360 / sides)