import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
df = pd.read_csv('worldometer_data.csv')
type(df)
top_10 = df[(df['Population'] >= 115223736) & (df['Population'] != 331198130 )]
# Задание цветов
c = ["#FF5733", "#33FF57", "#3366FF"]
q = [1,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4]
# Создание графика с настроенными цветами
top_10.plot(x="Country/Region", y="TotalCases", kind="bar", rot=5, fontsize=q, color= c)

# Отображение графика
plt.show()