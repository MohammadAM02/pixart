import pixart
import turtle

def test_init():
    pixart.init()

    s=turtle.speed()
    assert(s==0)

    x=turtle.xcor()
    assert(x==-200)

    y=turtle.ycor()
    assert(y == -270)

    p=turtle.isdown()
    assert(p == False)

    c=turtle.pencolor()
    assert(c == 'black')

    f=turtle.fillcolor()
    assert(f == 'white')



