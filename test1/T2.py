
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 设置selenium使用chrome的无头模式
chrome_options = Options()
# 在启动浏览器时加入配置
driver = webdriver.Chrome()
driver.maximize_window()      #最大化窗口
# 打开百度options=chrome_options
driver.get('https://rmfyzxfw.court.gov.cn/index')

# 等待加载，最多等待20秒
driver.implicitly_wait(10)
# driver.find_element_by_class('fd-header-actionTc fd-header-login').send_keys("")
# driver.find_element_by_id('su').clike()
driver.close()