import os

path = "D:\工作\下载\测试3"
if not os.path.isdir(path):  # 判断是否存在，若不存在则直接创建文件夹
    os.mkdir(path)  # 创建单个文件夹 mkdir 测试1

path = "D:\工作\下载\测试2\测试3"
if not os.path.isdir(path):  # 判断是否存在，若不存在则直接创建文件夹
    os.makedirs(path)  # 创建多级文件夹 makedirs 测试2\测试3

path = "D:\工作\下载\测试3"
if os.path.isdir(path):  # 判断是否存在，若存在则直接删除文件夹
    os.rmdir(path)  # 删除文件夹 rmdir


"""
在Python中，可以使用os模块进行文件夹操作。以下是一些常用的方法：

os.path.isabs()：判断路径是否是绝对路径。
os.path.exists()：判断路径或文件是否存在。
os.path.isdir()：判断路径是否是个目录。
os.path.isfile()：判断路径是否是个文件。
os.mkdir()：创建新文件夹。
os.rmdir()：删除指定路径的文件夹。
os.chdir()：改变当前工作目录。
os.walk()：递归遍历指定路径下的所有文件和文件夹。
以下是一个示例代码，演示如何使用os模块进行文件夹操作：
"""

import os

# 判断是否绝对路径
path = "D:\\Python_shutil"
if os.path.isabs(path):
    print("路径是绝对路径")
else:
    print("路径不是绝对路径")

# 判断是否真实存在
if os.path.exists(path):
    print("路径或文件存在")
else:
    print("路径或文件不存在")

# 判断是否是个目录
if os.path.isdir(path):
    print("是个目录")
else:
    print("不是目录")

# 判断是否是个文件
if os.path.isfile(path):
    print("是个文件")
else:
    print("不是文件")

# 创建新文件夹
os.mkdir(path)
print("文件夹创建成功")

# 删除指定路径的文件夹
if os.path.exists(path):
    os.rmdir(path)
    print("文件夹删除成功")
else:
    print("文件夹不存在")
# ```<em>1</em><em>2</em><em>3</em>
