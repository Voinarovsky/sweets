import numpy as np

a = np.array([[1,2,3],
              [4,5,6]])
a[:,1]=0

b = a.reshape(3,2)#изменение матрицы
b = a.transpose()#транспонирование
a.fill(0)#заменяет все элементы на 0

print(3 in a)
print(b)

k= np.array([1, 2, 3])
h= np.array([4, 5, 6])
print(k+h)