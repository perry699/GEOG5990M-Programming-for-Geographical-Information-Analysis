# -*- coding: utf-8 -*-
"""
Created on Wed Mar 1 10:16:42 2023

@author: Ziyu Pei
"""

import random
import math
import matplotlib.pyplot as plt
import tkinter as tk
import operator
import my_modules.agentframework as af
import my_modules.geometry
import my_modules.io as io
import imageio
import os
import matplotlib.animation as anim
import matplotlib


environment,n_rows,n_cols = io.read_data()

# Set the pseudo-random seed for reproducibility
random.seed(0)
  
n_agents = 10 
agents = []
x_min=0
y_min=0
x_max = n_cols - 1
y_max=  n_rows - 1
neighbourhood = 100

# Initialise agents
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(agents,i, environment, n_rows, n_cols))
    print(agents[i])

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


      
def sum_agent_stores(agents):
    sum_store = 0  
    for i in range(len(agents)):
        sum_store = sum_store + agents[i].store
    return sum_store


def sum_environment(environment):
    sum_environment = 0
    for j in range(len(environment)):
        for i in range(len(environment[j])):
            sum_environment = sum_environment +environment[j][i]
    return sum_environment
# Initialise agents
#text
#a = af.Agent()
#print("type(a)", type(a)) 



#plot function
def plot():
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    plt.imshow(environment)
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
   # global ite
    filename = '../../data/output/images/image' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show
    images.append(imageio.imread(filename))
    return fig



##change loop
def update(frames):
     # Model loop
     global carry_on
     #for ite in range(n_iterations):
     print("Iteration", frames)
     # Move agents
     print("Move and eat")
     for i in range(n_agents):
         agents[i].move(x_min, y_min, x_max, y_max)
         agents[i].eat()
         #print(agents[i])
     # Share store
     print("Share")
     # Distribute shares
     for i in range(n_agents):
         agents[i].share(neighbourhood)
     # Add store_shares to store and set store_shares back to zero
     for i in range(n_agents):
         #print(agents[i])
         agents[i].store = agents[i].store_shares
         agents[i].store_shares = 0
     #print(agents)
     # Print the maximum distance between all the agents
     print("Maximum distance between all the agents", get_max_distance())
     # Print the total amount of resource
     sum_as = sum_agent_stores(agents)
     print("sum_agent_stores", sum_as)
     sum_e = sum_environment(environment)
     print("sum_environment", sum_e)
     print("total resource", (sum_as + sum_e))

     # Stopping condition
     # Random
     if random.random() < 0.1:
         #if sum_as / n_agents > 80:
         carry_on = False
         print("stopping condition")

     # Plot
     global ite
     plot()
     ite = ite + 1

#define function
def gen_function():
    global ite
    ite = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (ite < n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Write data
        print("write data")
        #io.write_data('../../data/output/out7.txt', environment)
        imageio.mimsave('../../data/output/out8.gif', images, fps=3)
        data_written = True

def run(canvas):
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    animation.new_frame_seq()
    canvas.draw()


def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)


# For storing images
global ite
ite = 0
images = []
# Animate
# Initialise fig and carry_on
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
data_written = False
#animation.save("animation.gif", writer="imagemagick")
    
# GUI
root = tk.Tk()
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_0 = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=menu_0)
menu_0.add_command(label="Run model", command=lambda: run(canvas))
menu_0.add_command(label="Write data", command=lambda: output())
menu_0.add_command(label="Exit", command=lambda: exiting())
menu_0.entryconfig("Write data", state="disabled")
# Exit if the window is closed.
root.protocol('WM_DELETE_WINDOW', exiting)
tk.mainloop()





try:
    os.makedirs('../../data/output/images/')
except FileExistsError:
    print("path exists")


 




    
    





       
   



        
        

  




            

    
    
        
        
        
        
        