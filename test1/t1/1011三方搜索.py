from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def firefox():
    driver1 = webdriver.Firefox()
    driver1.maximize_window()  # 最大化浏览器窗口
    driver1.implicitly_wait(8)  # 设置隐式时间等待
    # driver1.get("https://www.baidu.com")  # 地址栏输入百度地址
    # # driver1.find_element(By.XPATH,'//*[@id="hotsearch-content-wrapper"]/li[5]/a').click()  #热搜2
    # driver1.find_element(By.ID, 'kw').send_keys('hello world')  # 搜索框
    # driver1.find_element(By.ID, 'su').click()

    # driver1.get("https://zhyyys.zh.gov.cn/rzrf/#/login")
    # driver1.find_element(By.XPATH,'/html/body/div[1]/div/div/div/form/div[1]/div/div[1]/input').send_keys('17815937680')
    # driver1.find_element(By.XPATH,'/html/body/div[1]/div/div/div/form/div[2]/div/div/input').send_keys('8995')
    # driver1.find_element(By.XPATH,'/html/body/div[1]/div/div/div/form/div[3]/div/button').click()
    # print('预约预审后台登录成功')

    driver1.get("https://www.baidu.com")
    # driver1.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/a[1]').click()
    # driver1.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/input').send_keys(
    #     'cad3cc6fc88d834a422ad19b92ee54bc')
    # driver1.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[3]/span/button/span').click()
    # driver1.find_element(By.XPATH,'//*[@id="root"]').click()
    # driver1.find_element(By.XPATH,'/html/body/div[2]/div/form/div/div[3]/span').click()
    # driver1.find_element.by_class_name('username').send_keys('4444')
    # driver1.find_element(By.ID, 'kw').send_keys('hello world')  # 搜索框
    # driver1.find_element(By.ID, 'su').click()
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
    time.sleep(30)
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


# firefox()
# chrome()
edge()
