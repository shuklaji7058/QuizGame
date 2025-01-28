import turtle
import pandas # type: ignore

screen = turtle.Screen()
screen.title("INDIA state Game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("India_States.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
