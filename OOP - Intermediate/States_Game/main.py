import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

write_turtle = turtle.Turtle()
write_turtle.penup()
write_turtle.hideturtle()

states = pandas.read_csv("50_states.csv")
score = 0
guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()

    if user_answer.lower() == "exit":
        unknown_states = []
        for state in states.state:
            if state not in guessed_states:
                unknown_states.append(state)
        pandas.DataFrame({"State": unknown_states}).to_csv("Unkown_Staes.csv")
        break

    if user_answer in states.state.to_list():
        score += 1
        guessed_states.append(user_answer)
        write_turtle.goto(x=int(states[states.state == user_answer].x), y=int(states[states.state == user_answer].y))
        write_turtle.write(arg=user_answer)


screen.exitonclick()