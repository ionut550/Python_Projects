from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.back(20)

def rotate_clockwise():
    tim.left(10)

def rotate_counter_clockwise():
    tim.right(10)

def clear_screen():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=rotate_clockwise)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_counter_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()