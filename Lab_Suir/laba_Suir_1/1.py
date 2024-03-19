import numpy as np
from time import perf_counter
data1 = np.random.random_sample(size = 10**6)   #создаю список из рандомных элементов длинной 10^6
data2 = np.random.random_sample(size = 10**6)

def multiplication(data1: list,data2: list):    #на вход подаеться 2 списка функция обычного перемножения
    t1_start = perf_counter() # старт времени
    data_m = [data1[i]*data2[i] for i in range(len(data1))] # перемножаем итый эл 1 списка на йтый жлемент второго списка и так столько раз сколько у нас жлементов
    t1_stop = perf_counter() #остановка времени
    time = t1_stop-t1_start # время затраченное=время конца-время начала
    return time

def multiplication_numpy(data1: list,data2: list):  # функция перемножения с помощью нампай
    t1_start = perf_counter()
    data_mn = np.multiply(data1,data2)
    t1_stop = perf_counter()
    time = t1_stop - t1_start
    return time

print('время, затраченное на поэлементное перемножение стандартных списков:' , end='\n')
print(multiplication(data1,data2), 'c')
print('время, затраченное на поэлементное перемножение массивов NumPy:', end='\n')
print(multiplication_numpy(data1,data2), 'c')
