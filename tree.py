#!/usr/bin/python3
# -*- coding: utf-8 -*-

import turtle
import random
import math


T = turtle.Turtle()
T.hideturtle()
#T.speed(0)
turtle.tracer(8, 25)


def tree(length=100, angle=180/8, ratio=0.65, r=3):
    """
    Draw a tree as long as the length is > 10
    The lenght is reduced by ratio each branch
    Each branch gives r branches
    """
    #angle *= random.randint(75, 125) / 100 # 25% incertitude
    #length *= random.randint(95, 105) / 100 # 5% incertitude
    if length > 10:
        T.pensize(5 * length / 100)
        T.forward(length * ratio)
        T.right(angle)
        for _ in range(r-1):
            tree(length * ratio, angle=angle, ratio=ratio)
            T.right((-2 / (r - 1)) * angle)
        tree(length * ratio, angle=angle, ratio=ratio)
        T.right(angle)
        T.up()
        T.backward(length * ratio)
        T.down()
    #else:
    #    T.dot(10, "black")

def tree2(length=100, angle=180/4, ratio=0.75, r=3, n=6):
    """
    Draw a tree that has n level of branching
    Each branch gives r branches
    """
    if n > 0:
        T.pensize(5 * length / 100)
        T.forward(length * ratio)
        T.right(angle)
        for _ in range(r-1):
            tree2(length=length*ratio, angle=angle, r=r, n=n-1)
            T.right((-2 / (r - 1)) * angle)
        tree2(length=length*ratio, angle=angle, r=r, n=n-1)
        T.right(angle)
        T.up()
        T.backward(length * ratio)
        T.down()
    #else:
    #    T.dot(10, "black")

if __name__ == '__main__':
    T.up()
    T.setposition(0, -250)
    T.left(90)
    T.down()
    #tree2(length=250, angle=50, ratio=0.55, r=3, n=5)
    tree(length=250, angle=30, ratio=0.60, r=3)
