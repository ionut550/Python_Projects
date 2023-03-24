# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# This is the solving problem if the robot finds himself in square loop.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def last_steps (my_list):
    string = ""
    for i in range(0,8):
        string += my_list.pop()
    return string

steps = 0
steps_history = []

while not at_goal():
    if steps > 4:
        history = last_steps(steps_history) 
        if (history == "MRMRMRMR" or history == "RMRMRMRM"):
            if front_is_clear():
                move()
                steps_history = []
                steps = 0
            else:
                turn_left()
                steps_history = []
                steps = 0
        else:
            steps = 0

    if right_is_clear():
        turn_right()
        steps_history.append("R")
        move()
        steps_history.append("M")
        steps += 1
    elif front_is_clear():
        move()
        steps_history.append("M")
    else:
        turn_left()
        steps_history.append("L")