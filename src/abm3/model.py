# -*- coding: utf-8 -*-
"""
Created on Wed Mar 1 10:16:42 2023

@author: Ziyu Pei
"""

import random
import math
import matplotlib.pyplot as plt
import time


# Set the pseudo-random seed for reproducibility
random.seed(0)


#Distance Calculations
#Define a Function
def get_distance(x0, y0, x1, y1):
    xdif = x1- x0
    ydif = y1- y0
    addsq = (xdif * xdif) + (ydif * ydif)
    dis = math.sqrt(addsq)
    print(dis)
    return dis

get_distance(1, 5, 9, 4)


#Calculate the maximum distance

#text
max_distance = 0 # Initialise max_distance
agents= []

for a in agents:
    for b in agents:
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)

#####
max_distance = 0
for i in range(len(agents)):
    a = agents[i]
    for j in range(len(agents)):
        b = agents[j]
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)
        
        
        
        
#define function max_dis
def get_max_distance():
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(len(agents)):
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            print("distance between", a, b, distance)
            #print("i", i, "j", j)
            max_distance = max(max_distance, distance)
            print("max_distance", max_distance)
    return max_distance
        
        
        
        
#Other distance statistics
#min_distance
def get_min_distance():
    min_distance = math.inf
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            print("distance between", a, b, distance)
            #print("i", i, "j", j)
            min_distance = min(min_distance, distance)
            print("min_distance", min_distance)
    return min_distance

        






#movement model
n_agents = 15
n_iterations = 1000
agents = []
rn = random.random()
print(rn)
def mp(coor):
  #x
    if rn < 0.5:
        coor[0] += 1
    else:
        coor[0] -= 1
  #y
    if rn < 0.5:
        coor[1] += 1
    else:
        coor[1] -= 1
    return coor
    

for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
    print(agents)
    
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99       

#Create a new outer For Loop to loop through moving agents n_iteration times
n_iterations=1000

for i in range(n_iterations):
    for i in range(len(agents)):
        agents[i] = mp(agents[i])
        if agents[i][0] < x_min:
            agents[i][0] = x_min
        if agents[i][1] < y_min:
            agents[i][1] = y_min
        if agents[i][0] > x_max:
            agents[i][0] = x_max
        if agents[i][1] > y_max:
            agents[i][1] = y_max
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
    
    
        
        
        
        
        