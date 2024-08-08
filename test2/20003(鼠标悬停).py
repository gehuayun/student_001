import yapf as yapf
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
driver = webdriver.Chrome()                                     # Chrome浏览器
# driver = webdriver.Edge()                                       # Edge 浏览器
driver.maximize_window()                                        # 最大化页面
driver.get('https://www.baidu.com')                             # 百度页面
driver.implicitly_wait(10)                                      # 隐式等待
el = driver.find_element(By.ID, 's-usersetting-top')            # 定位鼠标悬停元素
ActionChains(driver).move_to_element(el).perform()              # 鼠标悬停
driver.find_element(By.XPATH, '//*[@id="s-user-setting-menu"]/div/a[2]/span').click()          # 定位高级搜索-弹框上的元素
driver.find_element(By.ID, 'adv_keyword').send_keys('百度一下')                                  # 输入框输入信息
driver.find_element(By.XPATH, '//*[@id="adv-setting-8"]/input[2]').click()                     # 点击搜索按钮
sleep(3)
handles = driver.window_handles                                                 # 获取打开多个窗口的句柄
# driver.close()                                                                # 关闭首个网页
driver.switch_to.window(handles[0])                                             # 切换至 0 页面
driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[6]/span/i').click()       # 关闭高级搜索
sleep(2)
driver.find_element(By.ID, 'kw').send_keys('hello word !')                      # 输入搜索内容
driver.find_element(By.ID, 'su').click()                                        # 点击进行搜索
sleep(3)
driver.switch_to.window(handles[1])                                              # 切换到 1 页面
driver.find_element(By.ID, 'kw').clear()                                         # 清空搜索框
driver.find_element(By.ID, 'kw').send_keys('台风')                                # 输入搜索内容
driver.find_element(By.ID, 'su').click()                                         # 点击进行搜索
sleep(3)
driver.quit()  # 关闭浏览器
