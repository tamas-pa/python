import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

ds_states = pd.read_csv("50_states.csv")
all_states = ds_states.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 of the state",
                                    prompt="Whats another state name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        save_state_file = screen.textinput(title="Do you want to improve?",
                                           prompt="Would you like to save the remaining states to a .csv file?").title()

        if save_state_file == "Yes":
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
        screen.bye()
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = ds_states[ds_states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()
