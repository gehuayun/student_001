import requests
import os
import re

url = 'http://10.19.168.171/#/login?uesername=ghy&password=123'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 '
                  'Safari/537.36'}
response = requests.post(url)
pagetext = response.text
print(pagetext)