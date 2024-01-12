import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('worldometer_data.csv')
type(df)
top_10 = df[(df['Population'] >= 115223736) & (df['Population'] != 331198130 )]

top_10['alpha'] = [1,0.6,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
ax = sns.barplot(data=top_10, x="Country/Region", y="TotalCases", palette=['#ff0000', '#a52a2a', '#fa8072', '#8b0000', '#e9967a', '#e9967a', '#e9967a', '#e9967a', '#e9967a', '#e9967a'] )
for bar, alpha in zip(ax.containers[0], df['alpha']):
    bar.set_alpha(alpha)
plt.show()