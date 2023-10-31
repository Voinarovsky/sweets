    # import numpy as np
    #
    # a = np.array([1.2,2,3.4])
    # print(a)
    #
    # b = np.array([1.2, 3, 'test'])
    # print(type(b))
    #
    # c = np.array([[1,2],[4,5],[4,3]])
    # print(c)
    # print(c.ndim, c.shape, c.size, c.dtype) #количество осей, матрицу 3 на 2, кол-во эл, тип элементов
    #
    # d = np.zeros((3,3), dtype='int32')
    # print(d)
    #
    # print(d[0], d[0][1])
    #
    # e = np.eye(4,4, dtype='int16') #единечная матрица 4 на 4 в итновом типе
    # print(e)
    #
    # f = np.arange(0.5, 5.5, 0.5) #все числа от 0б5 до 5.5 с шагом 0.5
    # print(f)
    #
    # g = np.linspace(0, 1, 10) #10 точек от 0 до 1 распределеные на равном расстоянии
    # print(g)

import matplotlib.pyplot as plt

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

ax1.plot(list(range(0,5)), list(range(0,5)), linewidth=3)
ax2.scatter(list(range(0,10)), list(range(0,10)), s=100)
ax3.scatter(list(range(-5,6)), [x**2 for x in list(range(-5,6))], s=10)
ax3.plot(list)

ax1.set_title('Title',fontsize=20)
ax1.set_xlabel('X axis', frontsize=14)
ax1.set_ylabel('Y axis', frontsize=14)
plt.show()