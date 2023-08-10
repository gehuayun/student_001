rec1 = str("""
Python中有关文件的操作包括：

打开文件：使用open()函数打开文件，可以指定文件名和打开模式。
读取文件：使用read()方法读取文件内容，或者使用readline()方法逐行读取文件内容。
写入文件：使用write()方法向文件中写入内容。
关闭文件：使用close()方法关闭文件。
文件模式：Python中的文件模式包括：
r：只读模式，只能读取文件内容，不能写入或修改文件。
w：写入模式，可以向文件中写入内容，如果文件不存在则创建文件，如果文件存在则覆盖原有内容。
a：追加模式，可以向文件中追加内容，不会覆盖原有内容。
x：独占模式，只能打开一个文件进行读写操作，如果文件已经存在则无法打开。
b：二进制模式，以二进制方式读取或写入文件。
t：文本模式，以文本方式读取或写入文件。
递归访问文件夹：使用os.walk()函数可以递归访问文件夹，遍历文件夹下的所有子文件夹和文件。
序列化和反序列化：Python中的序列化和反序列化操作可以将数据转换为二进制格式或者将二进制格式的数据转换为Python对象。常用的序列化模块包括pickle和json
""")
import os
import xlrd.book  # 表格
import xlwt

path = "D:\工作\下载\测试3"
name = "cs"
with open(path + "/{}.txt".format(name), "wt") as txt:
    txt.write(rec1)
    txt.close()
print(name + "写入成功")
# os.remove(path + '\测试文本.txt')   # 删除文本

rec2 = str("""
Python 提供内置函数 open() 实现对文件的操作。操作步骤分三步，"打开-操作-关闭。
" open(file, mode='r', encoding=None) # file 包含文件名的字符串，可以是绝对路径，可以是相对路径。 
# mode 一个可选字符串，用于指定打开文件的模式。默认值 r 表示文本读。 # encoding 文本模式下指定文件的字符编码 。

相对路径与绝对路径：进行文件处理时经常会碰到相对路径和绝对路径的问题。
相对路径一般是指相对当前脚本的路径，比如上面的案例中的 a.txt。
绝对路径指定了文件在电脑中的具体位置，以 Windows 电脑为例：d:\class\demon\python入门.py。

with 上下文管理：解决经常会忘记关闭文件句柄，造成资源浪费，所以处理文件是往往使用 with 语句进行上下文管理。

多种读文件的方式：1) json.dump() 将Python对象序列化为json格式的数据流并写入文件类型的对象中。
import json 
dic = { "student" : [ {"name" : "xlh", "time" : "09:04"} ] } 
with open('./dic.json', mode='w', encoding='utf-8') as f: json.dump(dic, f)
""")

rec3 = str("""
在Python中，可以使用以下库来操作图片格式：

OpenCV：这是一个用于计算机视觉和图像处理的开源库，可以读取、处理和保存各种常见的图像格式，如JPEG、PNG、BMP等。
PIL（Python Imaging Library）：这是一个用于图像处理和格式转换的库，可以读取、处理和保存多种图像格式，如JPEG、PNG、BMP、GIF等。
Matplotlib：这是一个用于数据可视化的库，可以读取、处理和显示各种图像格式，如JPEG、PNG、BMP等。
以下是使用Matplotlib读取和显示图片的示例代码：

import matplotlib.pyplot as plt

# 读取图片
img = plt.imread('image.jpg')

# 显示图片
plt.imshow(img)
plt.show()
以上代码使用Matplotlib读取名为“image.jpg”的图片文件，并将其显示在图形窗口中。请确保已经安装了Matplotlib库，并在代码中指定正确的图片文件路径。
""")
