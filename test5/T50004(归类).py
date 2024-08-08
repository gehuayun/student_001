import requests
import os
import re

c = 0


# 通过正则表达式把一个个图片的链接和名字给匹配出来，存放到一个列表中
def re_1():
    global image, c
    parr = re.compile('data.src="(h.*?)".alt="(.*?)"')
    image = re.findall(parr, response.text)
    for content in image:
        print(content)
        c += 1


# 根据链接写入文件
def os_1():
    global image
    # 判断是否存在，若不存在则直接创建文件夹
    if not os.path.isdir(path):
        os.mkdir(path)
    # 对列表进行遍历
    for i in image:
        link = i[0]  # 获取链接
        name = i[1]  # 获取名字
        character = '\/:*?"<>|'  # 特殊符号匹配
        for s in character:
            if s in name:
                name = name.replace(s, 'A')  # 替换成“A”
        """
        在文件夹下创建一个空jpg文件，打开方式以 'wb' 二进制读写方式
        @param res：图片请求的结果
        """
        with open(path + "/{}.jpg".format(name), "wb") as img:
            res = requests.get(link)
            img.write(res.content)  # 将图片请求的结果内容写到jpg文件中
            img.close()  # 关闭操作
        print(name + ".jpg 获取成功······")


if __name__ == '__main__':
    url = "https://qq.yh31.com/qt/fj/"
    # 请求头 伪装浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    # 创建文件夹，保存内容  写入绝对路径
    path = "D:\工作\下载\测试2"
    # 文件的前缀
    qurl = "https://qq.yh31.com/qt/fj/"
    for i in range(9, 8, -1):
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        if i == 9:  # 首个页面
            re_1()
            os_1()
        else:  # 其他页面
            url = f"https://qq.yh31.com/qt/fj/List_{i}.html"
            re_1()
            os_1()
    print("下载图片总数量", c)
