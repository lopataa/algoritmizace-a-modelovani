import turtle

LENGTH =   250
GAP_SIZE = -50

turtle.hideturtle()
turtle.width(5)

def draw_spiral(length, gap_size):
    if not (length > gap_size > 0):
       raise ValueError("Invalid parameters :(")

    if length == LENGTH:
        turtle.forward(length)

    for i in range(2):
        turtle.right(90)
        turtle.forward(length)

    if length - gap_size >= gap_size:
        draw_spiral(length - gap_size, gap_size)

draw_spiral(LENGTH, GAP_SIZE)

turtle.done()