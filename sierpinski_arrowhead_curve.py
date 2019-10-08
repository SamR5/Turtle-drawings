#!/usr/bin/python3
# -*- coding: utf-8 -*-

import turtle

turtle.using_IDLE = True
T = turtle.Turtle()
T.hideturtle()
T.speed(0)
#turtle.tracer(0, 0)


def sierpinski_arrowhead_curve(length, angle, step, seq='YF-XF-Y'+'F'):
    """
    {X→YF−XF−Y,
     Y→XF+YF+X}
    """
    X = 'YF-XF-Y'
    Y = 'XF+YF+X'
    if step != 0:
        for i in seq:
            if i == 'X':
                sierpinski_arrowhead_curve(length, angle, step-1, X)
            elif i == 'Y':
                sierpinski_arrowhead_curve(length, angle, step-1, Y)
            else:
                if i == 'F':
                    T.forward(length)
                elif i == '+':
                    T.right(angle)
                elif i == '-':
                    T.left(angle)


if __name__ == '__main__':
    T.up(); T.goto(-350, -250); T.down()
    sierpinski_arrowhead_curve(length=5, angle=60, step=7)
    turtle.update()
