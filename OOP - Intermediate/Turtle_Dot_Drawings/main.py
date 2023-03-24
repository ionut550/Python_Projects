# import colorgram
#
# def color_selector():
#     color_list = []
#     colors = colorgram.extract('hirst_colors.jpg', 30)
#     for color in colors:
#         color_list.append((color.rgb.r , color.rgb.g, color.rgb.b))
#     print(color_list)

import random
from turtle import Turtle,Screen


color_list = [(132, 79, 49), (169, 149, 41), (158, 53, 161), (36, 36, 144), (233, 51, 143), (189, 8, 64), (109, 202, 155), (245, 225, 87), (133, 235, 126), (254, 164, 162), (26, 151, 53), (183, 164, 104), (234, 242, 246), (254, 254, 0), (43, 168, 52), (165, 209, 210), (71, 87, 160), (185, 131, 175), (35, 26, 22), (249, 158, 169), (85, 87, 193), (10, 9, 94), (140, 33, 5), (144, 157, 195), (251, 5, 62), (175, 175, 230), (103, 7, 45)]
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.goto(-300,-300)
direction = 90

for i in range(14):
    tim.dot(20, random.choice(color_list))
    for j in range(13):
        tim.forward(50)
        tim.dot(20,random.choice(color_list))
    tim.left(direction)
    tim.forward(50)
    tim.left(direction)
    direction *= -1


screen.exitonclick()