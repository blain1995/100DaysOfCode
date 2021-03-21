import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# Set up screen aesthetics
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load in the states names and location on image
states = pd.read_csv("50_states.csv")
all_states = states.state.to_list()
print(states)
score = 0
states_guessed = []
writing_tool = turtle.Turtle()
writing_tool.penup()
writing_tool.hideturtle()

while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="Input state name")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        unguessed = [answer for answer in all_states if answer not in states_guessed]
        new_data = pd.DataFrame(unguessed)
        new_data.to_csv("states_to_learn.csv")
        break

    for name in all_states:
        if name == answer_state:
            if answer_state not in states_guessed:
                score += 1
                states_guessed.append(answer_state)
                state_info = states[states["state"] == answer_state]
                writing_tool.goto(int(state_info.x), int(state_info.y))
                writing_tool.write(f"{answer_state}", False, align="center", font=("Ariel", 6, "normal"))
                print(state_info)

    print(states_guessed)

turtle.mainloop()
