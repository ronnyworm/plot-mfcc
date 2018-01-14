#!/usr/bin/env python3
#coding=UTF-8



import csv
import numpy as np
import matplotlib.pyplot as plt

nprows = None
meta = None
with open('outmfcc_D_A.csv', 'r') as csvfile:
    thereader = csv.reader(csvfile, delimiter=';', quotechar='\'')
    rows = []
    first = True
    for row in thereader:
    	if first: # skip columnnames
    		meta = row
    		first = False
    	else:
        	rows += [row]

    nprows = np.array(rows).T
    
timestep = nprows[1].astype("float64")
values = nprows[2:].astype("float64")

def f(x, y):
    return values[y,x]

x = np.linspace(0, 178, 179).astype("int64")
y = np.linspace(0, 38, 39).astype("int64")

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
from mpl_toolkits import mplot3d
ax = plt.axes(projection='3d')
ax.view_init(20, 30)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('timestep')
ax.set_ylabel('mfcc no')
ax.set_zlabel('value');
plt.show()


#plt.xticks(np.arange(0, nprows.shape[1] - 2, 2))
#plt.yticks(np.arange(-60, 180, 20))