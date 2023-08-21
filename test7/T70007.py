import numpy as np
from matplotlib import pyplot as plt, cm

'''
import points
from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# # ax = fig.gca(projection='3d')
# ax = fig.add_subplot(111,projection='3d')
# ax.scatter(points[:,0],points[:,1],points[:,2],zdir='z',c='c')'''
# 3d曲线图
a, b, c = 10., 28., 8. / 3.


def lorenz_map(x, dt=1e-2):
    x_dt = np.array([a * (x[1] - x[0]), x[0] * (b - x[2]) - x[1], x[0] * x[1] - c * x[2]])
    return x + dt * x_dt


points = np.zeros((8000, 3))
x = np.array([.1, .0, .0])
for i in range(points.shape[0]):
    points[i], x = x, lorenz_map(x)
# Plotting
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Lorenz Attractor a=%0.2f b=%0.2f c=%0.2f' % (a, b, c))
ax.plot(points[:, 0], points[:, 1], points[:, 2], c='c')
plt.show()
# 3d标量场
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
x_grid, y_grid = np.meshgrid(x, y)  # 使用`np.meshgrid()`方法将一维数组`x`和`y`转换为二维数组，得到`x_grid`和`y_grid`，用于表示XY平面上的点坐标网格。
print(x_grid)
z = np.sinc(np.sqrt(x_grid ** 2 + y_grid ** 2))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # 创建一个三维坐标轴对象。
ax.plot_surface(x_grid, y_grid, z,
                cmap=cm.viridis)  # x_grid和y_grid表示XY平面上的点坐标网格，z表示每个点上的函数值。cmap=cm.viridis指定使用'viridis'颜色映射，用于在三维图上表示高度的颜色。
plt.show()

################################
# 如果不希望看到三维曲面上显示的曲线色彩，可以使用 plot_surface() 的附加可选参数：
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
x_grid, y_grid = np.meshgrid(x, y)  # 使用`np.meshgrid()`方法将一维数组`x`和`y`转换为二维数组，得到`x_grid`和`y_grid`，用于表示XY平面上的点坐标网格。
z = np.sinc(np.sqrt(x_grid ** 2 + y_grid ** 2))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # 创建一个三维坐标轴对象。
ax.plot_surface(x_grid, y_grid, z, cmap=cm.viridis, linewidth=0,
                antialiased=False)  # x_grid和y_grid表示XY平面上的点坐标网格，z表示每个点上的函数值。cmap=cm.viridis指定使用'viridis'颜色映射，用于在三维图上表示高度的颜色。
plt.show()

################################
# 可以仅保持曲线色彩，而曲面不使用其他颜色，这也可以通过 plot_surface() 的可选参数来完成
x = np.linspace(-3, 3, 256)
y = np.linspace(-3, 3, 256)
x_grid, y_grid = np.meshgrid(x, y)  # 使用`np.meshgrid()`方法将一维数组`x`和`y`转换为二维数组，得到`x_grid`和`y_grid`，用于表示XY平面上的点坐标网格。
z = np.sinc(np.sqrt(x_grid ** 2 + y_grid ** 2))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # 创建一个三维坐标轴对象。
ax.plot_surface(x_grid, y_grid, z, edgecolor='b',
                color='w')  # x_grid和y_grid表示XY平面上的点坐标网格，z表示每个点上的函数值。cmap=cm.viridis指定使用'viridis'颜色映射，用于在三维图上表示高度的颜色。
plt.show()
