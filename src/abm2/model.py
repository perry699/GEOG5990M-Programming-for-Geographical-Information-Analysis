# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 01:53:32 2023

@author: Ziyu Pei
"""

import random
import math
import matplotlib.pyplot as plt
import operator


# Create a list to store agents
#agents = []

# text
# Initialise variable x0
#x0 = random.randint(0, 99)
#print("x0", x0)
# Initialise variable y0
#y0 = random.randint(0, 99)
#print("y0", y0)
#agents.append([x0, y0])
#print(agents)

# Plot the agents

#x1 = random.randint(0, 99)
#print("x1", x1)
# Initialise variable y0
#y1 = random.randint(0, 99)
#print("y1", y1)
#agents.append([x1, y1])
#print(agents)
#plt.scatter(agents[0][0], agents[0][1], color='black')
#plt.scatter(agents[1][0], agents[1][1], color='black')
#plt.show()
# Get the coordinates with the largest x-coordinate
#print(max(agents, key=operator.itemgetter(0)))



#### other content
# Set the pseudo-random seed for reproducibility
random.seed(0)

# Create a list to store agents
agents = []


n_agents = 10
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
    #Putting print in a loop makes it easier to see the difference
    print(agents)
    
    
# Using the same For Loop construction--modify the code to move the agents
rn = random.random()
print(rn)

# Change agents[i] coordinates randomly
for i in range(n_agents):
#coordinate-x
    if rn < 0.5:
        agents[i][0] += 1
    else:
        agents[i][0] -= 1
#coordinate-y
    if rn < 0.5:
        agents[i][1] += 1
    else:
        agents[i][1] -= 1
print(agents)


#made plot
#show all point
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')

#more plot---change colour
# the largest x coordinate using the colour red;
large_x =max(agents, key=operator.itemgetter(0)) 
plt.scatter(large_x[0], large_x[1], color='red')

# the smallest x coordinate using the colour blue;
small_x =min(agents, key=operator.itemgetter(0)) 
plt.scatter(small_x[0], small_x[1], color='blue') 

# the largest y coordinate using the colour yellow;
large_y =max(agents, key=operator.itemgetter(1)) 
plt.scatter(large_y[0], large_y[1], color='yellow')

# the smallest y coordinate using the colour green;
small_y =min(agents, key=operator.itemgetter(1)) 
plt.scatter(small_y[0], small_y[1], color='green') 

#get point informtion
print(large_x,small_x,large_y,small_y)



#Calculate the Euclidean distance
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

    




























