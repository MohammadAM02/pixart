import main
import turtle

def test_init():
    main.init()

    s=turtle.speed()
    assert(s==0)

    x=turtle.xcor():
    assert(x==-200)


