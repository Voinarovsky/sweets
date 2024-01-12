import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('worldometer_data.csv')
type(df)
top_10 = df[(df['Population'] >= 115223736) & (df['Population'] != 331198130 )]

g = sns.PairGrid(df, diag_sharey=False)
g.map_upper(sns.scatterplot, s=15)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot, lw=2)
sns.barplot(data=top_10, x="Country/Region", y="TotalCases", color='blue')
plt.show()