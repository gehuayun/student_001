import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
logging.basicConfig(filename="a.log", level=logging.INFO, format=fmt)

logging.debug("调试")
logging.info("信息")
logging.warning("警告")
logging.error("错误")

def chrome1():
    global d1
    d1 = webdriver.Chrome()
    d1.maximize_window()
    d1.get("http://10.19.168.171/#/login")
    d1.implicitly_wait(10)
    d1.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/input').send_keys('ghy')
    d1.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div/input').send_keys('tooLong@passWord999')
    d1.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/button/span').click()
    time.sleep(1)


def shang():
    d1.find_element(By.XPATH,
                    '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/button/span/div/span[1]').click()
    time.sleep(5)
    d1.quit()


def xia():
    d1.find_element(By.XPATH,
                    '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/button/span/div/span[1]').click()
    time.sleep(5)
    d1.quit()


now = datetime.datetime.now()
time0 = now.strftime("%H:%M:%S")  # %Y-%m-%d %H:%M:%S   获取当前时间
time1 = '09:00:00'
time2 = '18:00:00'
if time1 > time0:
    chrome1()
    print(fr"现在时间:{time0},开始打卡上班！！！")
    # 上班打卡
    shang()
elif time0 > time2:
    chrome1()
    print(fr"现在时间:{time0},开始打卡下班！！！")
    # 下班打卡
    xia()
else:
    print(fr"现在时间:{time0},未到打卡时间！！！")
    time.sleep(5)
