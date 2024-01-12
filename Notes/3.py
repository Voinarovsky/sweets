import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('worldometer_data.csv')
type(df)
top_10 = df[df['Population'] > 115223736]
df1 = df['Population']
w = []
for i in range(len(df1)):
    if df1[i] > 115223736:
        w.append(df1[i])

m = max(w)
q = []
for i in range(len(w)):
    c = (w[i] * 1.5)/m
    q.append(c)
print(q)

# plt.bar(x, height = h, width = w)
# top_10.plot(x="Country/Region", y="TotalCases", kind="bar", rot=10, fontsize=7, width = 2)
sns.set_style("ticks")
sns.barplot(data=top_10, x="Country/Region", y="TotalCases", width = q, palette=cm.Blues(df['b']*10)
plt.show()