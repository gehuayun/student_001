import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCw2LDMsMSw0LDUsMiw4LDcsOQ%3D%3D")
# driver.implicitly_wait(10)
# 获取当前页面的高度
last_height = driver.execute_script("return document.body.scrollHeight")

# 模拟下拉操作，直到滑动到底部
while True:
    # 模拟下拉操作
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 等待页面加载
    time.sleep(2)

    # 获取当前页面的高度
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 判断是否已经到达页面底部
    if new_height == last_height:
        break

    # 继续下拉操作
    last_height = new_height