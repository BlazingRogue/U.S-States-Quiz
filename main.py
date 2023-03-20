from turtle import *
import turtle as turtle
import pandas
import time

screen = Screen()
screen.title("U.S States Quiz")
image = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, -300)
writer.write("Type 'Exit' to finish", False, align="center", font=('Courier', 15, 'normal'))


def time_convert(times):
    minutes = times / 60
    sec = times % 60

    keeper = Turtle()
    keeper.hideturtle()
    keeper.penup()
    keeper.goto(0, 300)
    time_lapsed = "Time Lapsed = {0}:{1}".format(int(minutes), int(sec))
    keeper.write(time_lapsed, False, align="center", font=('Courier', 20, 'normal'))


start_time = time.time()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    current_row = data[data.state == answer_state]

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        writer.goto(int(current_row.x), int(current_row.y))
        writer.write(answer_state)


end_time = time.time()
time_complete = end_time - start_time
time_convert(time_complete)

end = Turtle()
end.hideturtle()
end.penup()
end.goto(0, 260)
end.write(f"You guessed {len(guessed_states)}/50 states", False, align="center", font=('Courier', 20, 'normal'))
screen.exitonclick()
