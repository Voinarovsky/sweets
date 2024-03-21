import matplotlib.pyplot as plt

import math
import pandas as pd

df = pd.read_csv('data2.csv')   #испорт дататеста
ph = df['ph']   #берем 1 столбец

ax = plt.gca()  #ограничитель построения графика потому что доверительный интервал шалит (КОСТЫЛЬ НЕЗАДУЬ ИСПРАВИТЬ!)
ax.set_xlim([0, 14])
ax.set_ylim([0, 1200])

#строим обычную гистограмму
plt.hist(ph, bins=20)
#создаем масив состоящий из высот столбцов, т.е. из количества входящих в каждый интервал значений
ax = plt.gca()
p = ax.patches
heights = [patch.get_height() for patch in p]
def quadratic_mean():
    ph_averge = sum(heights)/len(heights)   #среднее значение(можно использовать метод nanstd но я про него поздно узнал)

    #считаем сигму
    SUM = 0
    for i in range(len(heights)):   #сумма (xi-xср)^2
        SUM += (heights[i]-ph_averge)**2

    sigma = math.sqrt(SUM/len(heights))

    plt.axhline(y=ph_averge, color='r', linestyle='-')  #строим среднеквадратичное значение
    for i in range(round(sigma)):   #тоже костыль( строим доверительные интервалы с помощью множества линий от пограничного значения до средней
        plt.axhline(y=ph_averge-(sigma-i), color='r', linestyle='-', alpha=0.05)
        plt.axhline(y=ph_averge + (sigma - i), color='r', linestyle='-', alpha=0.05)

quadratic_mean()
plt.show()