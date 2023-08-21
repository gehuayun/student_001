# 微实例4：网络图片的爬取与存储

import requests
import os

# 引入os库以便将图片保存到本地
url = 'https://qq.yh31.com/tp/fj/202206241211029887.jpg'
root = 'D:\工作\下载\\'
# 设置根目录
path = root + url.split('/')[-1]
# 图片保存具体地址，用split以/分割链接，将最后一串字符作为图片名字
try:
    if not os.path.exists(root):
        os.mkdir(root)
    # 确认选择的根目录是否存在，不存在则创建一个
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('图片保存成功')
    # 确认该目录下同名图片是否存在，不存在则打开图片链接，以二进制形式写入内容
    else:
        print('图片已存在')
except:
    print('图片爬取失败')
