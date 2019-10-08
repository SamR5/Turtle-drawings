#!/usr/bin/python3
# -*- coding: utf-8 -*-


import turtle


T = turtle.Turtle()
T.reset()
T.hideturtle()
#T.speed(0)
turtle.tracer(0, 0)
T.up(); T.goto(230, 110); T.down()


def dragon_seq(n):
    """
    The curve can be constructed by representing a left turn by 1 and a
    right turn by 0. The first-order curve is then denoted 1. For higher
    order curves, append a 1 to the end, then append the string of
    preceding digits with its middle digit complemented.
    """
    seq = [True]
    for i in range(n):
        seq += [True] +\
               seq[:len(seq)//2] +\
               [not seq[len(seq)//2]] +\
               seq[len(seq)//2+1:]
    return seq

def dragon_curve():
    T.forward(10)
    for i in dragon_seq(11):
        if not i:
            T.left(90)
        else:
            T.right(90)
        T.forward(10)

if __name__ == '__main__':
    dragon_curve()
