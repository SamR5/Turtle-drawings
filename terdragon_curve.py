#!/usr/bin/python3
# -*- coding: utf-8 -*-


import turtle

T = turtle.Turtle()
T.hideturtle()
#T.speed(0)
turtle.tracer(8, 50)

def terdragon_curve(steps, length):
    S = "F"
    for i in range(steps):
        S = S.replace('F', 'F-F+F')
    for i in S:
        if i == 'F':
            T.forward(length)
        elif i == '-':
            T.right(120)
        elif i == '+':
            T.left(120)

if __name__ == '__main__':
    T.up(); T.goto(-400, -200); T.right(90); T.down()
    terdragon_curve(steps=8, length=10)
