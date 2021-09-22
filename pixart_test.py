import pixart
import turtle


def test_init():
    pixart.init()

    s = turtle.speed(0)
    assert(s == 0)

    x = turtle.xcor()
    assert(x == -270)

    y = turtle.ycor()
    assert(y == -300)

    turtle.isdown()
    assert(turtle.isdown == False)

    turtle.pencolor()
    assert(turtle.pencolor == 'Black')

    turtle.fillcolor()
    assert(turtle.fillcolor == 'white')
