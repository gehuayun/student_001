from selenium import webdriver
from time import sleep      # 强制时间格式
from selenium.webdriver.common.action_chains import ActionChains        # 悬停格式
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By         # 元素定位格式
from selenium.webdriver.common.keys import Keys     # 键盘按钮格式
# from test2.t2 import open_url, get_element, element_opr, web_autotest_opr

driver = webdriver.Chrome()             # Chrome浏览器
driver.maximize_window()                # 放大显示
driver.get('https://www.baidu.com')     # 百度网址
driver.implicitly_wait(5)               # 隐式等待
# sleep(2)                                # 强制等待
d1=driver.find_element(By.ID,'kw')      # d1：百度搜索框
d2=driver.find_element(By.ID,'su')      # d2：百度搜索按钮
d1.send_keys("12306")
sleep(2)
ActionChains(driver).move_to_element(d1).perform()      # 悬停操作
driver.find_element(By.XPATH,'//*[@id="normalSugSearchUl"]/li[1]').click()      # 点击悬停第一个坐标
# driver.find_element(By.ID,'kw').send_keys(Keys.ENTER)
sleep(2)
d1.clear()      # 清空搜索栏
# sleep(2)
d1.send_keys("background")
d2.send_keys(Keys.ENTER)        # 回车键
sleep(5)
driver.quit()       # 关闭浏览器
# if __name__ == '__main__':
#     open_url("https://www.baidu.com")
#     sleep(5)
#     get_element(webdriver.Chrome(), id, "kw", )
#     element_opr(webdriver.Chrome.find_element, '输入', 'hello word!')
#     sleep(5)
#     get_element(webdriver.Chrome(), id, "su", )
#     element_opr(webdriver.Chrome.find_element, '点击', )
#     sleep(5)
