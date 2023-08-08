# -*- coding: UTF-8 -*-
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 计算半周长
s = (a + b + c) / 2

# 计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为 %0.2f' % area)

# -*- coding: UTF-8 -*-
# 计算实数和复数平方根
# 导入复数数学模块

import cmath

num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))

# Filename : test.py
#  二次方程式 ax**2 + bx + c = 0
#  a、b、c 用户提供，为实数，a ≠ 0
# 导入 cmath(复杂数学运算) 模块
import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b ** 2) - (4 * a * c)

# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为 {0} 和 {1}'.format(sol1, sol2))

# -*- coding: UTF-8 -*-
# 用户输入摄氏温度
# 接收用户输入
celsius = float(input('输入摄氏温度: '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))

#  任意数的阶乘

# 输入数字
c = 1
a = int(input("请输入阶乘的数字"))
while True:
    c = c * a
    a = a - 1
    if a < 1:
        break
print(c)

# ····························
a1 = int(input("请输入阶乘的数字"))


def jc(a1):
    if a1 == 1:
        return a1
    else:
        return a1 * jc(a1 - 1)


print(jc(a1))

# ······················

