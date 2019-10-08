#!/usr/bin/python3
# -*- coding: utf-8 -*-

import turtle

T = turtle.Turtle()
T.hideturtle()
T.speed(0)

def gosper_curve(length, angle, steps, init='X+YF++YF-FX--FXFX-YF+'):
    """
    {X becomes X+YF++YF-FX--FXFX-YF+,
     Y becomes -FX+YFYF++YF+FX--FX-Y}
    """
    X = 'X+YF++YF-FX--FXFX-YF+'
    Y = '-FX+YFYF++YF+FX--FX-Y'
    if steps != 0:
        for i in init:
            if i == 'X':
                gosper_curve(length, angle, steps-1, X)
            elif i == 'Y':
                gosper_curve(length, angle, steps-1, Y)
            else:
                if i == 'F':
                    T.forward(length)
                elif i == '+':
                    T.right(angle)
                elif i == '-':
                    T.left(angle)

if __name__ == '__main__':
    T.up()
    T.left(90); T.forward(250); T.right(90)
    T.down()
    gosper_curve(25, 60, 3)
