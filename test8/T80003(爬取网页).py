from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os, requests, re
from selenium.webdriver.common.action_chains import ActionChains

driver1 = webdriver.Chrome()
driver1.maximize_window()
driver1.implicitly_wait(5)
driver1.get("http://www.baidu.com")
# driver1.find_element(By.ID,'kw').send_keys('内网')
# driver1.find_element(By.ID,'su').click()

try:
    # driver1.find_element(By.ID,"toolbar-search-input" ).send_keys('自动化测试')

    a1 = driver1.find_element(By.ID, "s-usersetting-top")
    ActionChains(driver1).move_to_element(a1).perform()  # 鼠标悬停   f8 或 ctrl + \
    time.sleep(5)
    driver1.find_element(By.XPATH, '//*[@id="s-user-setting-menu"]/div/a[2]/span').click()
    time.sleep(5)
    driver1.find_element(By.ID, "adv_keyword").send_keys('高级搜索')
    driver1.find_element(By.XPATH, '//*[@id="adv-setting-8"]/input[2]').click()
    time.sleep(5)

    driver1.quit()

except NameError:
    print('这次调用没走通')

# except:
# print('百度搜索成功')
# finally:
#     print('强制通过')

'''
'title-text c-font-medium c-color-t'
'c-icon title-content-top-icon c-color-red c-gap-right-small'
'title-content-index c-index-single c-index-single-hot1'
'title-content-index c-index-single c-index-single-hot2'


'''



