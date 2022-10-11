# coding=utf-8
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_baidu():
    driver = webdriver.Chrome()  # 打开chrome，如果没有安装chrome,换成webdriver.Firefox()
    driver.maximize_window()  # 最大化浏览器窗口
    driver.implicitly_wait(8)  # 设置隐式时间等待
    driver.get("https://www.baidu.com")  # 地址栏输入百度地址
    # driver.find_element(By.XPATH,'//*[@id="hotsearch-content-wrapper"]/li[5]/a').click()  #热搜2
    driver.find_element(By.ID,'kw').send_keys('hello world')    #搜索框
    driver.find_element(By.ID,'su').click()

    # driver.find_element(By.XPATH,'//*[@id="1"]/div/div[1]/div/div/div[2]/p[1]').click()  #
    time.sleep(10)



    # driver.find_element(By.XPATH,'//*[@id="s-top-loginbtn"]').click()   #点击登录
    # driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__userName"]').send_keys("18236341274")   #输入账号
    # driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__password"]').send_keys("123456789")     #输入密码
    # driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_11__submit"]').click()      #点击登录
    # time.sleep(3)
    # driver.find_element(By.XPATH, '//*[@id="kw"]').click()  #搜索框搜索
    # driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("selenium")  # 搜索输入框输入Selenium
    # driver.find_element(By.XPATH, '//*[@id="su"]').click()  # su.click()  #点击百度一下按钮
    # time.sleep(3)  # 等待时间
    driver.quit()
    print("执行百度成功，进行下一个")


def test_csdn():
    driver = webdriver.Chrome()
    driver.get("https://www.csdn.net")  #
    driver.maximize_window()  # 最大化浏览器窗口
    driver.implicitly_wait(8)  # 设置隐式时间等待
    driver.find_element(By.CLASS_NAME, "toolbar-btn-loginfun").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/span[4]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/input").send_keys(
        "")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/input").send_keys(
        "")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[4]/button").click()
    time.sleep(3)


# # driver.refresh()   #刷新页/面
# driver.back()  # 返回上一个页面
# time.sleep(3)
# driver.forward()  # 切换到下一个页面

# 这里通过元素XPath表达式来确定该元素显示在结果列表，从而判断Selenium官网这个链接显示在结果列表。
# 这里采用了相对元素定位方法/../
# 通过selenium方法is_displayed() 来判断我们的目标元素是否在页面显示。
# driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed()
# driver.quit()

def test_fy():
    driver = webdriver.Chrome()
    driver.get("https://rmfyzxfw.court.gov.cn/index")
    driver.maximize_window()  # 最大化浏览器窗口
    driver.implicitly_wait(8)  # 设置隐式时间等待
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/a[1]').click()

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[4]/div/div/div[2]/div/div/input').send_keys("cad3cc6fc88d834a422ad19b92ee54bc")

    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[4]/div/div/div[3]/span/button').click()

    driver.find_element(By.CLASS_NAME,'username').send_keys('18236341274')
    # driver.find_element_by_name('username').click()
    # driver.find_element_by_name('username').send_keys("18236341274")
    # driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div/div[2]/div/div/div/input').send_keys("12QWaszx")

    # driver.find_element(By.XPATH,'//*[@id="root"]/div/form/div/div[3]/span').click()
    time.sleep(6)
# class WebDriver(webdriver.WebDriver):
#     def setup(self):
#
#     def setDowntime(self):
test_baidu()
test_csdn()
test_fy()
