import turtle as tl
import pandas as pd

screen = tl.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tl.shape(image)
t = tl.Turtle()
t.hideturtle()
t.penup()
states = pd.read_csv("50_states.csv")
all_states = states.state.to_list()
print(all_states)


def get_mouse_click_coordinates(x, y):
    print(x, y)


found_states = 48
while found_states < len(all_states):
    answer = screen.textinput(title=f"{found_states}/{len(all_states)}",prompt="another state?")
    answer = answer.title()

    if answer not in all_states:
        answer = screen.textinput(title=f"{found_states}/{len(all_states)}",prompt="Wrong, guess another state?")
        state = states[states.state == answer]

    if answer in all_states:
        correct_state = states[states.state == answer]
        t.setposition(int(correct_state.x), int(correct_state.y))
        t.write(answer,font=("Arial", 8, "bold"))
        found_states+=1
        print(found_states)
    
    if found_states == len(all_states):
        t.write("Congratualations! You found all states!", align="center", font=("Arial", 20, "bold"))

tl.onscreenclick(get_mouse_click_coordinates)

tl.mainloop()



#screen.exitonclick()