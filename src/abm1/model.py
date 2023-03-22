# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 00:27:29 2023

@author: Ziyu Pei
"""

import random 
import math


# text...
x0 = 0
print("x0",x0)

y0 = 0
print("y0",y0)


rn = random.random()
print(rn)


# Set the pseudo-random seed for reproducibility
random.seed(0)  


if rn< 0.5:
    x0 = x0 + 1 
else: 
    x0 = x0 - 1
    
if rn> 0.5:
    y0 = y0 + 1 
else: 
    y0 = y0 - 1
print("x0",x0)
print("y0",y0)
print("rn",rn)


result = random.randint(0,99)
print("result", result)


#Calculate the Euclidean distance

# Calculate the difference in the x coordinates.
# Calculate the difference in the y coordinates.
# Square the differences and add the squares
# Calculate the square root
x0 = 0
y0 = 0
x1 = 3
y1 = 4
xdif = x1- x0
ydif = y1- y0
print(xdif,ydif)
addsq = (xdif * xdif) + (ydif * ydif)
print(addsq)
dis = math.sqrt(addsq)
print(dis)


# random coordinate --distance
x0 = random.randint(0,99)
y0 = random.randint(0,99)
print("x0,y0",(x0, y0))

x1 = random.randint(0,99)
y1 = random.randint(0,99)
print("x1,y1", (x1,y1))

xdif = x1- x0
ydif = y1- y0
print(xdif,ydif)

addsq = (xdif * xdif) + (ydif * ydif)
print(addsq)

dis = math.sqrt(addsq)
print(dis)


# design fuction
def euclidean_distance(coords):
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

coords = [ [1, 2], [4, 6] ]
distance = euclidean_distance(coords)
print(distance)

# random coords
coords = [ [random.randint(0,99) for i in range(2)], [random.randint(0,99) for i in range(2)]]
print(coords)
distance = euclidean_distance(coords)
print(distance)

### finish bye...