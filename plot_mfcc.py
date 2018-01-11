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

    nprows = np.array(rows)

samples = None
with open('samples.csv', 'r') as csvfile:
    thereader = csv.reader(csvfile, delimiter=';', quotechar='\'')
    rows = []
    index = 0
    for row in thereader:
        if index < 2: # skip columnnames
            index += 1
        else:
            rows += [row]

    samples = np.array(rows).T
    

import pylab
filenames = []
for i in range(0,len(nprows)):
    values = nprows[i][2:].astype("float64")

    plt.text(0, 135, 'Frame ' + str(i))
    plt.hist(np.arange(0, nprows.shape[1] - 2), values)
    plt.xticks(np.arange(0, nprows.shape[1] - 2, 2))
    plt.yticks(np.arange(-60, 180, 20))

    pylab.savefig(str(i) + '.jpg')
    filenames += [str(i) + '.jpg']
    plt.close()

images = []
import imageio
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images)