import pytest
import requests

params = {}
data = {}

resp = requests.request(url='http://www.baidu.com',
                        method='post',
                        params=params,
                        data=data)
print(resp.text)


def re(url, method, params, data):
    resp = requests.request(url=url, method=method, params=params, data=data)
    print(resp.text)

# re()
