# -*- coding: utf-8 -*-
"""
Created on Wed Mar 1 10:35:30 2023

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
            #print("distance between", a, b, distance)
            min_distance = min(min_distance, distance)
            #print("min_distance", min_distance)
    return min_distance


#timer 
timer = [] # store time
n_agents_500 = range(500,5000,500)
#n_agent = 500
for n_agents in n_agents_500:
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    #print(agents)

    #count time
    start = time.perf_counter()
    print("Max_dis ", get_max_distance())
    end = time.perf_counter()
    # sub dis
    runtime=end-start
    print("Time taken to calculate maximum distance", runtime, "seconds")
    timer.append(runtime)
#make plot
plt.title("Time taken to calculate maximum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")
j = 0
for i in n_agents_500:
    plt.scatter(i, runtime[j], color='black')
    j += 1
plt.show()


#def make_point():
    #agents = []
    #for i in range(n_agents):
        #agents.append([random.randint(0, 99), random.randint(0, 99)])
    #print(agents)
   #make_point()
    
    
    
    























        
        



        
        
        
        
        
        
        
        
        
        
        
        
        
