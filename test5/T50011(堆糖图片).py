import urllib.parse
import json
import requests
import jsonpath

url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'
# url = "https://www.duitang.com/search/?kw=%E7%BE%8E%E5%A5%B3&type=feed"

labe = '美女'
label = urllib.parse.quote(labe)
num = 0

for index in range(0, 2400, 24):
    u = url.format(label, index)
    we_data = requests.get(u).text
    html = json.loads(we_data)
    photo = jsonpath.jsonpath(html, "$..path")

    for i in photo:
        a = requests.get(i)
        with open(r'D:\工作\下载\测试2\{}.jpg'.format(num), 'wb') as f:
            f.write(a.content)
        num += 1
