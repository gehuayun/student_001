import math
import matplotlib.pyplot as plt
import numpy as np

scale = range(100)
x = [(2*math.pi*i)/len(scale)for i in scale]
y = [math.cos(i) for i in x]
plt.plot(x,y)
plt.show()

x = np.linspace(-10,10,800)
y = x**3+ 5*x-10
plt.plot(x,y)
plt.show()

#绘制多线图
x = np.linspace(0.1, 2 * np.pi, 100)
y_1 = x
y_2 = np.square(x)
y_3 = np.log(x)
y_4 = np.sin(x)
plt.plot(x,y_1)
plt.plot(x,y_2)
plt.plot(x,y_3)
plt.plot(x,y_4)
plt.show()