from turtle import Turtle, Screen
import random as r

screen = Screen()
screen.setup(height=400, width=500)
is_race_on = False
all_turtles = []
colours = ["red", "violet", "blue", "green", "yellow", "indigo"]

user_pick = screen.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter the colour: ')
if user_pick:
    is_race_on = True
x_pos = -200
y_pos = -150
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x_pos, y_pos)
    y_pos += 50
    all_turtles.append(new_turtle)
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if user_pick == turtle:
                print(f"The race is over.{turtle.pencolor()} turtle won the race!. You won the bid:) ")
                is_race_on = False

            else:
                print(f"The race is over.{turtle.pencolor()} turtle won the race. You lose the bid!:( ")
                is_race_on = False
            
        else:
            turtle.forward(r.randint(0, 10))


