"""
要使用Python爬取动态网页数据，可以使用requests库结合BeautifulSoup或者Selenium库来实现。
如果使用requests库结合BeautifulSoup，可以先发送POST请求获取网页数据，然后使用BeautifulSoup对返回的数据进行解析。可以参考如下代码：
"""

import requests
from bs4 import BeautifulSoup


def get_page(page):
    data = {
        'yzm': 'yxAH',
        'ft': '',
        'ktrqks': '2020-05-22',
        'ktrqjs': '2020-06-22',
        'spc': '',
        'yg': '',
        'bg': '',
        'ah': '',
        'pagesnum': page
    }
    url = base_url + urlencode(data)
    try:
        response = requests.request("POST", url, headers=headers)
        if response.status_code == 200:
            content = response.content.decode('gbk')
            return content
    except requests.ConnectionError as e:
        print('Error', e.args)
    except (TimeoutError, Exception):
        n -= 1
        if n == 0:
            print('请求3次均失败，放弃此url请求,检查请求条件')
            return
        else:
            print('请求失败，重新请求')
            continue

for page in range(1, 5):
    html = get_page(page)
    print("第" + str(page) + "页提取完成")

import requests
from bs4 import BeautifulSoup


def get_page(page):
    data = {
        'yzm': 'yxAH',
        'ft': '',
        'ktrqks': '2020-05-22',
        'ktrqjs': '2020-06-22',
        'spc': '',
        'yg': '',
        'bg': '',
        'ah': '',
        'pagesnum': page
    }
    url = base_url + urlencode(data)
    try:
        response = requests.request("POST", url, headers=headers)
        if response.status_code == 200:
            content = response.content.decode('gbk')
            return content
    except requests.ConnectionError as e:
        print('Error', e.args)
    except (TimeoutError, Exception):
        n -= 1
        if n == 0:
            print('请求3次均失败，放弃此url请求,检查请求条件')
            return
        else:
            print('请求失败，重新请求')
            continue


for page in range(1, 5):
    html = get_page(page)
    print("第" + str(page) + "页提取完成")
"""
其中，get_page函数用于发送POST请求获取网页数据，然后返回解析后的内容。在遍历页数的循环中，调用get_page函数获取每一页的数据。
如果使用Selenium库，可以模拟浏览器操作，动态加载网页内容，并提取所需数据。具体代码如下：
"""


from selenium import webdriver

driver = webdriver.Chrome()  # 使用Chrome浏览器
driver.get(url)  # 打开要爬取的网页

# 进行模拟操作，例如点击按钮、滚动页面等
...

# 获取动态加载后的网页内容
html = driver.page_source

# 关闭浏览器
driver.quit()

from selenium import webdriver

driver = webdriver.Chrome()  # 使用Chrome浏览器
driver.get(url)  # 打开要爬取的网页

# 进行模拟操作，例如点击按钮、滚动页面等
...

# 获取动态加载后的网页内容
html = driver.page_source

# 关闭浏览器
driver.quit()
"""
通过Selenium模拟浏览器操作，可以获取动态加载后的网页内容。然后可以使用解析库如BeautifulSoup对网页内容进行解析和提取所需数据。
总结起来，要爬取动态网页数据，可以使用requests库结合BeautifulSoup或Selenium库来实现。
前者通过发送POST请求并解析返回的数据，后者通过模拟浏览器操作获取动态加载后的网页内容。具体选择哪种方式取决于目标网页的具体情况和需求
"""