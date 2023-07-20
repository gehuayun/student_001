from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

d1 = webdriver.Chrome()
d1.maximize_window()  # 最大化浏览器窗口
d1.implicitly_wait(8)  # 设置隐式时间等待

d1.get("https://www.baidu.com")     #百度搜索
sting=d1.find_element(By.ID,'s-usersetting-top')
ActionChains(d1).move_to_element(sting).perform()
time.sleep(5)
sting_1=d1.find_element(By.CLASS_NAME,'c-font-normal')
ActionChains(d1).click(sting_1).perform()

# d1.find_element(By.ID,'kw').send_keys('python')
# d1.find_element(By.ID,'su').click()
time.sleep(5)
