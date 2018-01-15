#!/usr/bin/env python3
#coding=UTF-8



import csv
import numpy as np
import matplotlib.pyplot as plt
import pywt


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
    
timesteps = samples[0].astype("float64")
values = samples[1].astype("float64")

cA, cD = pywt.dwt(samples[1], "db2")

# siehe Verstärkung am Ende der Zeile
plt.plot(timesteps, values * 50)
plt.plot(timesteps[:len(cA)], cA * 50)
plt.plot(timesteps[:len(cD)], cD * 50)

plt.title("Samples with db2 Wavelet")
plt.legend(['samples', 'approximation coefficients', 'detail coefficients'], loc='upper left')
plt.xticks(np.arange(min(timesteps), max(timesteps)+0.2, 0.2))

plt.show()