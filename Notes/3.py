import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('worldometer_data.csv')
# type(df)
top_10 = df[(df['Population'] >= 115223736) & (df['Population'] != 331198130 )]

TotalRecovered = [2047660, 1377384, 676357,308848,256058,143824, 75645, 32430,28877,28877]
Deaths = [98644,41638,14606,60517,6035,3306,5521,930,2016,365]
t = []
for i in range(len(Deaths)):
    c = (Deaths[i] * 100)/max(Deaths)
    t.append(c)

# color = {'Brazil':'#e9967a', 'India':'#fa8072', 'Russia': '#f08080', 'Mexico': '#cd5c5c', 'Pakistan': '#a52a2a', 'Bangladesh': '#b22222', 'Indonesia': '#8b0000', 'Nigeria': '#800000', 'Japan': '#dc143c', 'Ethiopia': '#ff0000'}
for i in range(len(t)):
    if t[i] <= 10:
        t[i]='#e9967a'
    elif t[i] <= 20:
        t[i] = '#fa8072'
    elif t[i] <= 30:
        t[i] = '#f08080'
    elif t[i] <= 40:
        t[i] = '#cd5c5c'
    elif t[i] <= 50:
        t[i] = '#a52a2a'
    elif t[i] <= 60:
        t[i] = '#b22222'
    elif t[i] <= 70:
        t[i] = '#8b0000'
    elif t[i] <= 80:
        t[i] = '#800000'
    elif t[i] <= 90:
        t[i] = '#dc143c'
    elif t[i] <= 100:
        t[i] = '#ff0000'

dfP = df['Population']
w = []
for i in range(len(dfP)):
    if dfP[i] >= 115223736 and dfP[i] != 331198130:
        w.append(dfP[i])

m = max(w)
q = []
for i in range(len(w)):
    c = (w[i] * 0.6)/m
    q.append(c)

# sns.set_style("ticks",{'axes.grid' : True})
ax = sns.barplot(data=top_10, x="Country/Region", y="TotalCases", width=0.9, palette = t )
sns.barplot(data=top_10, x="Country/Region", y="TotalCases", width=q, color='black')
# for i in range(len(TotalRecovered)):
#     b = TotalRecovered[i]
ax.bar_label(ax.containers[0], label_type='edge',fmt='2047660', color='blue', rotation=90, fontsize=8, padding=3)
ax.bar_label(ax.containers[1], label_type='edge',fmt='1377384', color='blue', rotation=90, fontsize=8, padding=3)
ax.bar_label(ax.containers[2], label_type='edge',fmt='676357', color='blue', rotation=90, fontsize=8, padding=3)
ax.bar_label(ax.containers[3], label_type='edge',fmt='308848', color='blue', rotation=90, fontsize=8, padding=3)
ax.bar_label(ax.containers[4], label_type='edge',fmt='256058', color='blue', rotation=90, fontsize=8, padding=3)
ax.bar_label(ax.containers[5], label_type='edge',fmt='143824', color='blue', rotation=90, fontsize=8, padding=3)
ax.bar_label(ax.containers[6], label_type='edge',fmt='75645', color='blue', rotation=90, fontsize=8, padding=3)
ax.bar_label(ax.containers[7], label_type='edge',fmt='32430', color='blue', rotation=90, fontsize=8, padding=3)
ax.bar_label(ax.containers[8], label_type='edge',fmt='28877', color='blue', rotation=90, fontsize=8, padding=3)
ax.bar_label(ax.containers[9], label_type='edge',fmt='9027', color='blue', rotation=90, fontsize=8, padding=3)
plt.show()