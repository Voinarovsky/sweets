import numpy as np
from time import perf_counter
data1 = np.random.random_sample(size = 10**6)
data2 = np.random.random_sample(size = 10**6)

def multiplication(data1: list,data2: list):
    t1_start = perf_counter()
    data_m = [data1[i]*data2[i] for i in range(len(data1))]
    t1_stop = perf_counter()
    time = t1_stop-t1_start
    return time

def multiplication_numpy(data1: list,data2: list):
    t1_start = perf_counter()
    data_mn = np.multiply(data1,data2)
    t1_stop = perf_counter()
    time = t1_stop - t1_start
    return time

print(multiplication(data1,data2))
print(multiplication_numpy(data1,data2))
