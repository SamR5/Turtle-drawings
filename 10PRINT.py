#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random as r
import turtle
import math as m

def random01grid(W, H):
    """"""
    return [[r.choice((0, 1)) for _ in range(W)] for _ in range(H)]

def filter_squares(sequences):
    """Avoid the closed squares with the random01grid generator"""
    for i in range(1, len(sequences) - 1):
        for j in range(1, len(sequences[0])):
            if all([sequences[i-1][j-1] == 0,
                    sequences[i-1][j] == 1,
                    sequences[i][j-1] == 1,
                    sequences[i][j] == 0]):
                if r.random() > 0.5:
                    sequences[i][j] = 1
                else:
                    sequences[i-1][j] = 0
    return sequences

def rand_bars(seqs, angle, size):
    """"""
    T = turtle.Turtle(visible=False)
    T.pensize(2)
    turtle.tracer(50, 200)
    turtle.bgcolor('black')
    T.up(); T.goto(-1920//2, 1080//2); T.down()
    #T.up(); T.goto(-700, 500); T.down()
    s2 = size/2
    size2 = float(size)/(m.sin(m.radians(angle)))
    T.pencolor('orange')
    for seq in seqs:
        xline, yline = T.position()
        for i in seq:
            x, y = T.position()
            if i:
                # 26.56 5**0.5
                T.up(); T.goto(x, yline+s2); T.down()
                T.right(angle); T.forward(size2); T.left(angle)
            else:
                T.up(); T.goto(x, yline-s2); T.down()
                T.left(angle); T.forward(size2); T.right(angle)
        T.up(); T.goto(xline, yline-size); T.down()
    turtle.update()

if __name__ == "__main__":
    rand_bars(filter_squares(random01grid(128, 72)), angle=45, size=15)
    #rand_bars(random01grid(128, 72), angle=45, size=15)
    pass
