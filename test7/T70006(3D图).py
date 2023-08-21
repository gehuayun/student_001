import numpy as np
from matplotlib import pyplot as plt
##3d散点图
a, b, c = 10., 28., 8. / 3.
def lorenz_map(x, dt = 1e-2):
    x_dt = np.array([a * (x[1] - x[0]), x[0] * (b - x[2]) - x[1], x[0] * x[1] - c * x[2]])
    return x + dt * x_dt
points = np.zeros((2000, 3))
x = np.array([.1, .0, .0])
for i in range(points.shape[0]):
    points[i], x = x, lorenz_map(x)
# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # 使用add_subplot()方法创建三维坐标轴
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Lorenz Attractor a=%0.2f b=%0.2f c=%0.2f' % (a, b, c))
ax.scatter(points[:, 0], points[:, 1],points[:, 2], zdir = 'z', c = 'c')
plt.show()