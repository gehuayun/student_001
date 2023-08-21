from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def firefox():
    driver1 = webdriver.Firefox()
    driver1.maximize_window()  # 最大化浏览器窗口
    driver1.implicitly_wait(8)  # 设置隐式时间等待
    driver1.get("https://www.baidu.com")  # 地址栏输入百度地址
    driver1.find_element(By.ID, 'kw').send_keys('office会自动下载软件吗')  # 搜索框
    driver1.find_element(By.ID, 'su').click()
    time.sleep(10)

    print('火狐驱动完整，百度搜索')
    driver1.quit()


def chrome():
    driver2 = webdriver.Chrome()
    driver2.maximize_window()  # 最大化浏览器窗口
    driver2.implicitly_wait(8)  # 设置隐式时间等待
    driver2.get("https://www.baidu.com")  # 地址栏输入百度地址
    # driver.find_element(By.XPATH,'//*[@id="hotsearch-content-wrapper"]/li[5]/a').click()  #热搜2
    driver2.find_element(By.ID, 'kw').send_keys('勾股定理')  # 搜索框
    driver2.find_element(By.ID, 'su').click()
    time.sleep(10)
    print('谷歌驱动完整，百度搜索中')
    driver2.quit()


def edge():
    driver3 = webdriver.Edge()
    driver3.maximize_window()  # 最大化浏览器窗口
    driver3.implicitly_wait(8)  # 设置隐式时间等待
    driver3.get("https://www.baidu.com")
    driver3.find_element(By.ID, 'kw').send_keys('hello world')
    driver3.find_element(By.ID, 'su').click()
    time.sleep(10)
    print('edge驱动完整，百度搜索中')
    driver3.quit()


firefox()
chrome()
edge()
