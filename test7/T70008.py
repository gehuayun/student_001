import numpy as np
from matplotlib import pyplot as plt
# Matplotlib 也能够使用更通用的方式绘制三维曲面：
angle = np.linspace(0, 2 * np.pi, 32)
theta, phi = np.meshgrid(angle, angle)
r, r_w = .25, 1.
x = (r_w + r * np.cos(phi)) * np.cos(theta)
y = (r_w + r * np.cos(phi)) * np.sin(theta)
z = r * np.sin(phi)
# Display the mesh
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.plot_surface(x, y, z, color = 'c', edgecolor='m', rstride = 2, cstride = 2)
plt.show()

################################################################
# 同样可以使用 plot_wireframe() 替换对 plot_surface() 的调用，以便获得圆环的线框视图：
angle = np.linspace(0, 2 * np.pi, 32)
theta, phi = np.meshgrid(angle, angle)
r, r_w = .25, 1.
x = (r_w + r * np.cos(phi)) * np.cos(theta)
y = (r_w + r * np.cos(phi)) * np.sin(theta)
z = r * np.sin(phi)
# Display the mesh
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.plot_wireframe(x, y, z, edgecolor='c', rstride = 2, cstride = 1)
plt.show()