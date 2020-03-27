import turtle

def h_tree(order, center, size):
    draw_turtle(center, size)

    if order > 0:
        ep1, ep2, ep3, ep4 = get_endpoints(center, size)

        h_tree(order - 1, (ep1, ep2), size / 2)
        h_tree(order - 1, (ep1, ep4), size / 2)
        h_tree(order - 1, (ep3, ep2), size / 2)
        h_tree(order - 1, (ep3, ep4), size / 2)

def draw_turtle(center, size):
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()

    turtle.forward(size / 2)  # right side of H
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.right(180)
    turtle.forward(size)

    turtle.penup()
    turtle.goto(center)
    turtle.pendown()

    turtle.right(90)  # left side of H
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(180)
    turtle.forward(size)

    turtle.right(90)  # return turtle to original orientation

def get_endpoints(center, size):
    ep1 = center[0] + size / 2
    ep2 = center[1] + size / 2
    ep3 = center[0] - size / 2
    ep4 = center[1] - size / 2

    return ep1, ep2, ep3, ep4

def main():

    turtle.speed('fastest')

    h_tree(2, (0.0, 0.0), 300)

    turtle.hideturtle()

    turtle.done()

main()



