import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./12. us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./12. us-states-game-start/50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        
        new_data = pandas.Series(missing_states)
        # new_data = pandas.DataFrame(missing_states) -> sama aja karena sama 1 kolom doang
        new_data.to_csv("./12. us-states-game-start/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        

