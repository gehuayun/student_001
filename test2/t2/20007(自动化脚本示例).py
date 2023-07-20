# 以下是一个使用Python编写的自动化测试脚本示例，用于测试一个web应用程序的登录功能：


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 设置浏览器驱动路径
driver_path = "/path/to/driver"

# 创建浏览器对象
driver = webdriver.Chrome(executable_path=driver_path)

# 访问网页
driver.get("https://example.com/login")

# 输入用户名和密码
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")
username_field.send_keys("testuser")
password_field.send_keys("password123")

# 提交表单
password_field.send_keys(Keys.RETURN)

# 等待页面加载完毕
time.sleep(5)

# 检查是否成功登录
if "Logged in as testuser" in driver.page_source:
    print("Login successful")
else:
    print("Login failed")

# 关闭浏览器
driver.quit()
# 这个脚本使用Selenium Webdriver库来控制一个Chrome浏览器实例，模拟用户在登录页面输入用户名和密码，并提交表单。
# 然后，通过检查页面内容来验证是否成功登录。最后，关闭浏览器并退出脚本。