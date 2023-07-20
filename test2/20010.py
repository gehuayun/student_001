import requests
from bs4 import BeautifulSoup

# 发起HTTP请求获取网页内容
url = 'https://www.baidu.com'  # 你要抓取的网页的URL
response = requests.get(url)
content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(content, 'html.parser')

# 提取你需要的数据
# 这里以提取网页标题为例
title = soup.title.text

# 打印提取的数据
print(title)