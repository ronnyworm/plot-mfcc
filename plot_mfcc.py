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

wavelettype = "db10"
cA, cD = pywt.dwt(samples[1], wavelettype)


from scipy.io import wavfile
samples_reshaped = np.array(cA).reshape(len(cA), 1)
wavfile.write(wavelettype + "-approx.wav", 22050, samples_reshaped)

samples_reshaped = np.array(cD).reshape(len(cD), 1)
wavfile.write(wavelettype + "-detail.wav", 22050, samples_reshaped)