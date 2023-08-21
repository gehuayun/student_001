import re
import os
import requests

url = "https://www.xiaohongshu.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}

res = requests.get(url=url, headers=headers)
# 使用json（）方法 将response对象 转为列表|字典
# json = res.json()
res.encoding = res.apparent_encoding
print(res.text)

# 遍历字典，获取所需资料
# for i in json:
#     for j in i:
#         print(j)


# parr = re.compile('src="(/u.*?)".alt="(.*?)"')
# image = re.findall(parr, res.text)
# for content in image:
#     print(content)
