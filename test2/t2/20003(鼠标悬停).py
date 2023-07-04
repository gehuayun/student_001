from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# # 不自动关闭浏览器
# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)

# # 将option作为参数添加到Chrome中
# driver = webdriver.Chrome(option)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
sleep(3)
# 定位鼠标悬停元素
el = driver.find_element(By.ID,'s-usersetting-top')  # #s-usersetting-top
ActionChains(driver).move_to_element(el).perform()  # 鼠标悬停
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="s-user-setting-menu"]/div/a[2]/span').click()  # 定位弹框上的元素
# sleep(1)
driver.find_element(By.ID,'adv_keyword').send_keys('百度一下')      # 输入框输入信息
# sleep(1)
driver.find_element(By.XPATH, '//*[@id="adv-setting-8"]/input[2]').click()      # 点击搜索按钮
sleep(3)
d1=driver.find_element(By.ID,'kw')
d2=driver.find_element(By.ID,'su')
d1.clear()          # 清空搜索框
sleep(3)
d1.send_keys('hello word !')
sleep(1)
d2.click()
sleep(3)
driver.quit()     # 关闭浏览器
