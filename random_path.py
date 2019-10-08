#!/usr/bin/python3.6
# -*- coding: utf-8 -*-


import turtle
import random


AMOUNT = 90
turtles = []
turtle.tracer(10, 100)


colors =\
    [(1, round(i/100, 2), 0) for i in range(0, 100, 2)] +\
    [(round(i/100, 2), 1, 0) for i in range(100, 0, -2)] +\
    [(0, round(i/100, 2), round(1-i/100, 2)) for i in range(100, 0, -2)] +\
    [(round(i/100, 2), 0, 1) for i in range(0, 100, 2)]


def init():
    for i in range(AMOUNT):
        t = turtle.Turtle(visible=False)
        t.pensize(3)
        t.right(random.randint(0, 360))
        turtles.append(t)

def main(steps, distInterval=(2, 4), angleInterval=(-15, 15)):
    X = steps / len(colors)
    for i in range(steps):
        for t in turtles:
            t.color(colors[int(i//X)])
            t.right(random.randint(angleInterval[0], angleInterval[1]))
            t.forward(random.randint(distInterval[0], distInterval[1]))

if __name__ == '__main__':
    init()
    #main(50)
    main(50, (2, 4), (-2, -2))
