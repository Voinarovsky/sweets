# import itertools
# mas = []
# for i in range(1, 5):
#     mas.append([i]*i)
# flat_list = list(itertools.chain(*mas))
# print(flat_list[4])

import itertools


def sequence_element(n: int):
    mas = []
    for i in range(1, n+1):
        mas.append([i] * i)
    fullmas = list(itertools.chain(*mas))
    return fullmas[n-1]
print(sequence_element(2))