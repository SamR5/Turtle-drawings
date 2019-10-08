#!/usr/bin/python3
# -*- coding: utf-8 -*-

import turtle

turtle.using_IDLE = True
T = turtle.Turtle()
#turtle.tracer(0, 0)
T.hideturtle()
T.speed(0)


def koch_curve(length, step, angle):
    if step:
        koch_curve(length/3, step-1, angle)
        T.left(angle)
        koch_curve(length/3, step-1, angle)
        T.right(2 * angle)
        koch_curve(length/3, step-1, angle)
        T.left(angle)
        koch_curve(length/3, step-1, angle)
    else:
        T.forward(length)

def koch_snowflake(length, step, angle):
    T.up()
    T.back(350); T.left(90); T.forward(175); T.right(90)
    T.down()
    for x in range(3):
        koch_curve(length, step, angle)
        T.right(120)


if __name__ == '__main__':
    koch_snowflake(length=600, step=4, angle=60)
    turtle.update()
