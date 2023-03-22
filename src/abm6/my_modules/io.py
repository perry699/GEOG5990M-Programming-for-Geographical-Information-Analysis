# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:39:48 2023

@author: Ziyu Pei
"""




#change to function

def read_data():
    import csv
    # Read input data
    f = open('../../data/input/in.txt', newline='')
    data = []
    n_rows = 0
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        n_cols =0
        n_rows = n_rows+1
        for value in line:
            row.append(value)
            n_cols = n_cols + 1
            #print(value)
        data.append(row)
    f.close()
    #print(data)
    
    return data,n_rows,n_cols




