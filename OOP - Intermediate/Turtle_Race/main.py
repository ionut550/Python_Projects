from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)
color_list = ["red", "blue", "violet", "green", "yellow", "brown", "black", "cyan", "orange"]
list_of_turtles = []
for i in range(9):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(color_list[i])
    new_turtle.goto(x= -240,y= -120 + i * 30)
    list_of_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race ? Enter a color: ")


def move_forward(turtle):
    turtle.forward(random.randint(1,10))

game_on = True
while game_on:
    turtle = random.choice(list_of_turtles)
    move_forward(turtle)

    if turtle.xcor() >= 250:
        if turtle.color()[0] == user_bet:
            game_on = False
            print(f"{turtle.color()[0].capitalize()} turtle won the race. You were right")
        else:
            game_on = False
            print(f"{turtle.color()[0].capitalize()} turtle won the race. You were wrong")

screen.exitonclick()