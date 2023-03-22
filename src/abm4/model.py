# -*- coding: utf-8 -*-
"""
Created on Wed Mar 1 10:16:42 2023

@author: Ziyu Pei
"""

import random
import math
import matplotlib.pyplot as plt
import operator
import agentframework as af


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
            #change
            #distance = get_distance(a[0], a[1], b[0], b[1])
            distance = get_distance(a.x, a.y, b.x, b.y)
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
            #change
            #distance = get_distance(a[0], a[1], b[0], b[1])
            distance = get_distance(a.x, a.y, b.x, b.y)
            print("distance between", a, b, distance)
            #print("i", i, "j", j)
            min_distance = min(min_distance, distance)
            print("min_distance", min_distance)
    return min_distance

        


# Initialise agents
#text
#a = af.Agent()
#print("type(a)", type(a)) 





# Initialise agents
n_agents = 10
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(i))
    print(agents[i])
print(agents)




#movement model
#Create a new outer For Loop to loop through moving agents n_iteration times
n_iterations=10
rn = random.random()
print(rn)
'''
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
'''  
# Change agents[i] coordinates randomly
for i in range(n_agents):
#coordinate-x
    if rn < 0.5:
        agents[i].x += 1
    else:
        agents[i].x -= 1
#coordinate-y
    if rn < 0.5:
        agents[i].y += 1
    else:
        agents[i].y -= 1   
print(agents)  



    
for p in range(n_iterations):
    # Variables for constraining movement.
    # The minimum x coordinate.
    x_min = 0
    # The minimum y coordinate.
    y_min = 0
    # The maximum x coordinate.
    x_max = 99
    # The maximum y coordinate.
    y_max = 99
    
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
    for i in range(n_agents):
        plt.scatter(agents[i].x, agents[i].y, color='black')
    # Plot the coordinate with the largest x red
    lx = max(agents, key=operator.attrgetter('x'))
    plt.scatter(lx.x, lx.y, color='red')
    # Plot the coordinate with the smallest x blue
    sx = min(agents, key=operator.attrgetter('x'))
    plt.scatter(sx.x, sx.y, color='blue')
    # Plot the coordinate with the largest y yellow
    ly = max(agents, key=operator.attrgetter('y'))
    plt.scatter(ly.x, ly.y, color='yellow')
    # Plot the coordinate with the smallest y green
    sy = min(agents, key=operator.attrgetter('y'))
    plt.scatter(sy.x, sy.y, color='green')
    
    plt.show()
        
        

  




            

    
    
        
        
        
        
        