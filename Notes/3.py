import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('worldometer_data.csv')
type(df)
top_10 = df[(df['Population'] >= 115223736) & (df['Population'] != 331198130 )]

TotalRecovered = []
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
    c = (w[i] * 1.5)/m
    q.append(c)

sns.barplot(data=top_10, x="Country/Region", y="TotalCases",width = q, palette=['#ff0000', '#a52a2a', '#fa8072', '#8b0000', '#e9967a', '#e9967a', '#e9967a', '#e9967a', '#e9967a', '#e9967a'] )
plt.show()