# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:29:14 2023

@author: gy22zp
"""

import math


#Distance Calculations
#Define a Function
def get_distance(x0, y0, x1, y1):
    xdif = x1- x0
    ydif = y1- y0
    addsq = (xdif * xdif) + (ydif * ydif)
    dis = math.sqrt(addsq)
    print(dis)
    return dis

