import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7,4)) #размер 3д куба
ax_3d = fig.add_subplot(projection = '3d') #задаем 3д

x = np.linspace(-2*np.pi,2*np.pi,50) #x линия от -2pi до 2pi с плотностью 50
y = np.sin(x)*np.cos(x)
z = np.sin(x)*np.cos(x)

ax_3d.plot(x,y,z, label='сипмотный график')
ax_3d.set_xlabel('x')   #подписи осей
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

plt.show()