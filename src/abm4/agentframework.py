# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:11:24 2023

@author: Ziyu Pei
"""

import random

class Agent:
   def __init__(self, i):
       """
       The constructor method.

       Parameters
       ----------
       i : Integer
       To be unique to each instance.

       Returns
       -------
       None.

       """
       self.i = i
       self.x = random.randint(0, 99)
       self.y = random.randint(0, 99)
       pass
        
   def __str__(self):
        return self.__class__.__name__ + "(x=" + str(self.x) \
            + ", y=" + str(self.y) + ")"
    
    #print String representations of agents when printing the agents list
   def __repr__(self):
       return str(self)
    
   def move(self, x_min, y_min, x_max, y_max):
        rn = random.random()
        if rn < 0.5:
            self.x += 1
        else:
            self.x -= 1
        rn = random.random()
        if rn < 0.5:
            self.y += 1
        else:
            self.y -= 1
            
        if self.x < x_min:
            self.x = x_min
        if self.y < y_min:
            self.y = y_min
        if self.x > x_max:
            self.x = x_max
        if self.y > y_max:
            self.y = y_max
            
        return self  