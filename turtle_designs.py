#!/usr/bin/python3
# -*- coding: utf-8 -*-

import turtle
import random as r


T = turtle.Turtle()
T.hideturtle()
T.speed(0)
T.up()

colors =\
    [(1, round(i/100, 2), 0) for i in range(0, 100, 2)] +\
    [(round(i/100, 2), 1, 0) for i in range(100, 0, -2)] +\
    [(0, round(i/100, 2), round(1-i/100, 2)) for i in range(100, 0, -2)] +\
    [(round(i/100, 2), 0, 1) for i in range(0, 100, 2)]

def rotating_triangle():
    T.clear()
    T.sety(-120)
    T.setx(-230)
    T.down()
    for i in range(180):
        T.forward(450)
        T.lt(60*2+2)

def square():
    T.clear()
    T.sety(-200)
    T.setx(-200)
    T.down()
    for i in range(100, -230, -2):
        T.forward(230+i)
        T.lt(90+2)

def multicolor_spiral():
    T.clear()
    steps = 300
    X = steps / len(colors)
    turtle.bgcolor('black')
    for i in range(steps):
        turtle.color(colors[int(i//X)])
        turtle.forward(i)
        turtle.right(90+8)
