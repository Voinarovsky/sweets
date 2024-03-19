import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps
import math
import pandas as pd

df = pd.read_csv('data2.csv')
ph = df['ph']

ph_list = []
new_ph = []
ax = plt.gca()
ax.set_xlim([0, 14])
ax.set_ylim([0, 1200])
for i in range(len(ph)):
    if ph[i]>0:
        new_ph.append(ph[i])


plt.hist(ph, bins=20)
def quadratic_mean():
    SUM = 0
    for i in range(len(new_ph)):
        ph_list.append(new_ph[i])

    ph_averge = sum(new_ph)/len(new_ph)

    for i in range(len(new_ph)):
        SUM += (new_ph[i]-ph_averge)**2

    sigma = math.sqrt(SUM/len(new_ph))

    plt.axhline(y=ph_averge, color='black', linestyle='-')
    for i in range(round(sigma)):
        plt.axhline(y=ph_averge-sigma, color='r', linestyle='-', alpha=0.20)
        plt.axhline(y=ph_averge + sigma, color='r', linestyle='-', alpha=0.20)

quadratic_mean()
plt.show()