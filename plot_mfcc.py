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
    

x = nprows[1].astype("float64")
# siehe Verstärkung am Ende der Zeile
plt.plot(samples[0].astype("float64"), samples[1].astype("float64") * 50)
plt.plot(x, nprows[2].astype("float64"))
plt.plot(x, nprows[15].astype("float64"))
plt.plot(x, nprows[18].astype("float64"),color="blue")
print(meta[2])
print(meta[15])
print(meta[28])

plt.legend(['y = samples', 'y = ' + meta[2], 'y = ' + meta[15], 'y = ' + meta[28]], loc='upper left')
plt.xticks(np.arange(min(x), max(x)+0.2, 0.2))

plt.show()
