import os

# myfile = "D:\\工作\\测试用例"
# list1=os.listdir(myfile)
# print(list1)

# file = open("2.txt", "r")
# print("开始读写内容")
# print(file.read()) #查看文件内容
# print("完成")
# file.close()
#
# file = open("2.txt", "w")
# file.write(input("写入字符串在文件内容里：")) #写入内容
# file.close()
#
# file = open("2.txt", "r")
# print("查看新的内容")
# print(file.read()) #查看文件内容
# print("结束")
# file.close()
# print(len(cont))
# print(file.readlines())


# 写入字节数
my1 = "hello world!"
file = open("2.txt", "w")
print(file.write(my1))  # 写入字节数
file.close()

# with语句
with open("2.txt") as f:
    print(f.read()) #
