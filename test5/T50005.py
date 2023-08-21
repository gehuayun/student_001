import appium
import content as content
import pip
import requests
import re
import os
from io import BytesIO
from jedi.api import file_name

url = "https://pic.netbian.com/4kmeinv/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"

}

response = requests.get(url=url, headers=headers)
# 通过发送请求成功response 通过（apparent_encoding）获取该网页的编码格式，并对response解码
response.encoding = response.apparent_encoding
print(response.text)  # 获取网页信息
"""
. 表示除空格外任意字符（除\n外）
* 表示匹配字符零次或多次
? 表示匹配字符零次或一次
.*? 非贪婪匹配
"""


def re_1():
    global image
    parr = re.compile('img src="(.*?)".alt="(.*?)"')  # 匹配图片链接和图片名字
    image = re.findall(parr, response.text)
    for content in image:
        print(content)


for i in range(1, 5):   # 页数遍历
    if i == 1:  # 首个页面
        re_1()
        # os_1()
    else:  # 其他页面
        url = f"https://pic.netbian.com/4kmeinv/index_{i}.html"
        re_1()
        # os_1()



# path = "D:\工作\下载"
#
# if not os.path.isdir(path):  # 判断是否存在该文件夹，若不存在则创建
#     os.mkdir(path)  # 创建
# c = 0
# 对列表进行遍历
# for i in image:
#     link = i[0]  # 获取链接
#     name = i[1]  # 获取名字
#     print(i[0], i[1])
#     c += 1
#     if c == 2:
#         break
# character = '[\\/:*?"<>|]'  # 特殊符号匹配
# for s in character:
#     if s in name:
#         name = name.replace(s, 'A')
#
# try:
#     # 将 图片地址（即v） 再次放入request中
#     image = requests.get(i[0], timeout=10)
# except requests.exceptions.ConnectionError:
#     print('【错误】当前图片无法下载')

# 在文件夹下创建一个空jpg文件，打开方式以 'wb' 二进制读写方式
# @param res：图片请求的结果

# with open(path + "/{}.jpg".format(name), "wb") as img:
#
#     res = requests.get(link)
#     img.write(res.content)  # 将图片请求的结果内容写到jpg文件中
#     img.close()  # 关闭操作


# 方法一：
# if response.status_code == 200:
#     print('==================================================')
#     if not os.path.exists(res.content):
#         os.makedirs(res.content)
#     total_path = res.content + '/' + file_name
# # 核心代码，比较请求返回数据的大小和请求反应头里面的大小
#     if len(response.content) == int(response.headers['Content-Length']):
#
#         # print total_path
#         with open(total_path, 'wb') as f:
#             for chunk in response.iter_content(1024):
#                 f.write(chunk)
#             f.close()
#     else:
#         raise print('图片加载不完全')
# else:
#     raise print('网络没有正常返回')


# 方法二：
"""
response = requests.get(url=source_url, headers=headers, verify=False, proxies=proxies, timeout=15)
if response.status_code == 200:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    total_path = dir_path + '/' + file_name

    image = Image.open(BytesIO(response.content))
    image.save(total_path)

    print("图片保存到本地")
    return 1
else:
    print("图片没有保存到本地")
"""
