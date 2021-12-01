import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

ds_states = pd.read_csv("50_states.csv")
all_states = ds_states.state.to_list()

answer_state = screen.textinput(title="Guess the state" , prompt="Whats another state name?").lower()

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = ds_states[ds_states.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state)

screen.exitonclick()