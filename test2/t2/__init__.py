from selenium import webdriver
from selenium.webdriver.common.by import By


def open_url(url):
    """
        打开浏览顺访问url，并返回浏器操作句柄
        :param url: 要测试的网站url
        :return: webdriver对像
        """
    opr = webdriver.Chrome()
    opr.maximize_window()
    opr.get(url)
    return opr


def get_element(opr: webdriver.Chrome, type, locatuion, index):
    """
        获取元素并返回
        :param opr: 浏览器句柄
        :param type: 定位器类型
        :param locatuion: 定位器
        :param index: 下标
        :return: 元素对象
        """
    if str.lower(type) == 'id':
        return opr.find_elements(By.ID, locatuion)[index]
    elif str.lower(type) == 'name':
        return opr.find_elements(By.NAME, locatuion)[index]
    elif str.lower(type) == 'class':
        return opr.find_elements(By.CLASS_NAME, locatuion)[index]
    elif str.lower(type) == 'tag':
        return opr.find_elements(By.TAG_NAME, locatuion)[index]
    elif str.lower(type) == 'link':
        return opr.find_elements(By.LINK_TEXT, locatuion)[index]
    elif str.lower(type) == 'plink':
        return opr.find_elements(By.PARTIAL_LINK_TEXT, locatuion)[index]
    elif str.lower(type) == 'xpath':
        return opr.find_elements(By.XPATH, locatuion)[index]
    elif str.lower(type) == 'css':
        return opr.find_elements(By.CSS_SELECTOR, locatuion)[index]


def element_opr(el: webdriver.Chrome.find_element, operation, value):
    """
        元素操作
        :param el: 元素对象
        :param operation: 操作类型
        :param value: 值
        :return: 成功（True）or失败(False)
        """
    if operation == '点击':
        el.click()
        return True
    elif operation == '输入':
        el.send_keys(value)
        return True


def web_autotest_opr(opr: webdriver.Chrome, operation, type, locatuion, index=0, value=''):
    """
        元素操作统一入口
        :param opr: 浏览器句柄
        :param operation: 操作类型
        :param type: 定位器类型
        :param locatuion: 定位器
        :param index: 下标
        :param value: 值
        :return: 成功（True）or失败(False)
        """
    if str.lower(type) != 'js':
        el = get_element(opr, type, locatuion, index)
        result = element_opr(el, operation, value)
    else:
        result = opr.execute_script(locatuion)
    return result
