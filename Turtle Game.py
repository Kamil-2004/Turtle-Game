logo = """

 ____ ____ ____ ____ ____ ____ 
||T |||u |||r |||t |||l |||e ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|

"""

print(logo)

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="make your bet", prompt="which turtle will win")

colors = ["red", "blue", "orange", "black", "pink", "white"]

y_position = [-70, -40, -10, 20, 50, 80]

all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won the race! the {winning_color} turtle is the winner")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner")
        rand_distance = random. randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()