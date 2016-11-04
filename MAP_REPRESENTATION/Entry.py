from __future__ import print_function
from pagi_api import *
import random
# import cv2
# import numpy as np
from time import sleep

cs = connect_socket('192.168.110.1', 42209)
agent = Agent(cs)
item = Items(cs)


# RETRIEVES AND TRANSLATES THE TOP HALF OF THE TOP HALF OF THE MAP
def top():

    full = [[]] * 0
    agent.vision.update('peripheral')
    # view = agent.vision.vision
    for ln in agent.vision.vision:
        line = []
        for l in ln:
            if l == '':
                line.append(0)
            elif l == 'apple':
                line.append(2)
            else:
                line.append(1)
        full.append(line)
    i = 10
    temp = [[]] * 11
    for ln in full:
        temp[i] = ln
        i -= 1
    return temp


# RETRIEVES AND TRANSLATES THE VISION OF THE BOTTOM HALF OF THE MAP
def bottom():
    try:
        agent.rotate(180)
    except:
        ""
    agent.vision.update('peripheral')
    temp = [[]] * 0
    for ln in agent.vision.vision:
        i = 15
        tmp = [] * 0
        for l in ln:

            if ln[i] == '':
                tmp.append(0)
            elif ln[i] == 'apple':
                tmp.append(2)
            else:
                tmp.append(1)

            i -= 1
        temp.append(tmp)

    res = [[]] * 11
    return temp


# JOINS THE UPPER AND LOWER HALVES OF THE AGENT'S VISION
def join(t,b):
    fin = []*0
    for ln in t:
        fin.append(ln)
    for ln in b:
        fin.append(ln)
    return fin


# CREATES A BORDER AROUND FULL MAP REPRESENTATION
def border(f):
    tcol = [[]]*0
    for x in range(0, f.__len__()):
        trow = []*0
        if x == 0 or x == f.__len__()-1:
            trow = [1]*f[x].__len__()
        else:
            for y in range(0, f[x].__len__()):
                if y == 0 or y == f[x].__len__()-1:
                    trow.append(1)
                else:
                    trow.append(f[x][y])
        tcol.append(trow)
    return tcol


# RESET ROTATION
def rt():
    try:
        agent.reset_rotation()
    except:
        ""


# STARTING FUNCTION
def start():
    rt()
    final = border(join(top(), bottom()))
    rt()

    for ln in final:
        print(ln)


# ENTRY POINT
start()