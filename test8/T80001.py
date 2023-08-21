import re,requests
import bs4

# url 请求地址
url = 'https://blog.csdn.net/'
# headers 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

response = requests.get(url=url,headers=headers)
# 通过发送请求成功response 通过（apparent_encoding）获取该网页的编码格式，并对response解码
response.encoding = response.apparent_encoding
print(response.text)
# parr = re.compile('img src="(h.*?)".alt="(.*?)"')
# image = re.findall(parr, response.text)
# for content in image:
#     print(content)