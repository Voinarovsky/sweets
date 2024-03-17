import numpy as np
from time import perf_counter
data1 = np.random.random_sample(size = 2**4)
data2 = np.random.random_sample(size = 2**4)

def multiplication(data1: list,data2: list) -> list:
    t1_start = perf_counter()
    data_m = [data1[i] * data2[i] for i in range(len(data1))]
    t1_stop = perf_counter()
    print("Elapsed time:", t1_stop-t1_start)
    return data_m

print(data1)
print(data2)
print(multiplication(data1,data2))

