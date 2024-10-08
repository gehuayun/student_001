import requests
import re
import os

url = "https://wallpaperscraft.com/all/3840x2160/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Referer": "https://wallpaperscraft.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Connection":"keep-alive",
    "Cookie":"_gid=GA1.2.1558185134.1697002942; __gpi=UID=00000c5c6a9c1075:T=1697002941:RT=1697003355:S=ALNI_MahhiK0FVl54TbxTHjL3psd66oGbA; _gat_gtag_UA_11053870_8=1; _ga_1LLJE8K50W=GS1.1.1697002942.1.1.1697003478.0.0.0; _ga=GA1.2.396350578.1697002942; __gads=ID=77de5bcf4c56f97a-22d15d7483e40008:T=1697002941:RT=1697003478:S=ALNI_MYeQ84-nz21hYQFXsDAr-QjvnI6dg",
    "Host":"wallpaperscraft.com"
}


def re_1():  # 通过正则表达式把一个个图片的链接和名字给匹配出来，存放到一个列表中
    global image
    parr = re.compile('src="(/u.*?)".alt="(.*?)"')
    image = re.findall(parr, response.text)
    for content in image:
        print(content)


def os_1():  # 创建文件夹，保存内容
    global image
    path = "E:\工作\下载\测试4"
    if not os.path.isdir(path):
        os.mkdir(path)  # 判断是否存在，若不存在则直接创建文件夹
    # 对列表进行遍历
    for i in image:
        link = i[0]  # 获取链接
        name = i[1]  # 获取名字
        character = '\/:*?"<>|'     # 特殊符号匹配
        for s in character:
            if s in name:
                name = name.replace(s, 'A')  # 替换成“A”
        """
        在文件夹下创建一个空jpg文件，打开方式以 'wb' 二进制读写方式
        @param res：图片请求的结果
        """
        with open(path + "/{}.jpg".format(name), "wb") as img:
            res = requests.get("https://pic.netbian.com" + link)
            img.write(res.content)  # 将图片请求的结果内容写到jpg文件中
            img.close()  # 关闭操作
        print(name + ".jpg 获取成功······")


for i in range(1, 2):   # 页数遍历
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    print(response.text)  # 获取网页信息
    if i == 1:  # 首个页面
        re_1()
        # os_1()
    else:  # 其他页面
        url = f"https://pic.netbian.com/index_{i}.html"
        re_1()
        # os_1()


