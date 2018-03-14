#!/usr/bin/env python3
#coding=UTF-8



import csv
import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.io import wavfile

def write_to_file(filename, samples, sr):
	samples_reshaped = np.array(samples).reshape(len(samples), 1)
	wavfile.write(filename, sr, samples_reshaped)

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


wavelettype = "db2"
num = 10
coeffs = pywt.wavedec(samples[1], wavelettype, level=num)
# approx not interesting
rev = list(reversed(coeffs[1:]))

for i in range(num):
	write_to_file(wavelettype + "-" + str(10 - i) + "-detail.wav", rev[i], int(44100 / (len(samples[1]) / len(rev[i]))))
	print(len(rev[i]))