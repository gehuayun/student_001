from selenium import webdriver
from selenium.webdriver.common.by import By  # 元素定位引用
import time

df = webdriver.Chrome()  # Chrome 浏览器
# df.minimize_window()      # Window窗口最小化
# df.set_window_size(1500,800)    # Window设置窗口大小
df.maximize_window()  # Window窗口最大化
df.get("https://www.baidu.com/")  # Baidu首页   1号页面
time.sleep(3)  # 强制等待
df.implicitly_wait(10)  # 隐式等待
'''
webDriverWait(df,timeout,poll_frequency=0.5,ignored_exceptions=None)
driver: 浏览器驱动
timeout: 超时时间，等待的最长时间（同时要考虑隐性等待时间）
poll_frequency: 每次检测的间隔时间，默认是0.5秒
ignored_exceptions:超时后的异常信息，默认情况下抛出NoSuchElementException异常
until(method,message=‘’)
method: 在等待期间，每隔一段时间调用这个传入的方法，直到返回值不是False
message: 如果超时，抛出TimeoutException，将message传入异常
until_not(method,message=‘’): 与until相反，until是当某元素出现或什么条件成立则继续执行，until_not是当某元素消失或什么条件不成立则继续执行，参数也相同。

from selenium.webdriver.support import expected_conditions as EC
# 判断标题是否和预期的一致
title_is
# 判断标题中是否包含预期的字符串
title_contains
# 判断指定元素是否加载出来
presence_of_element_located
# 判断所有元素是否加载完成
presence_of_all_elements_located
# 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0，传入参数是元组类型的locator
visibility_of_element_located
# 判断元素是否可见，传入参数是定位后的元素WebElement
visibility_of
# 判断某个元素是否不可见，或是否不存在于DOM树
invisibility_of_element_located
# 判断元素的 text 是否包含预期字符串
text_to_be_present_in_element
# 判断元素的 value 是否包含预期字符串
text_to_be_present_in_element_value
#判断frame是否可切入，可传入locator元组或者直接传入定位方式：id、name、index或WebElement
frame_to_be_available_and_switch_to_it
#判断是否有alert出现
alert_is_present
#判断元素是否可点击
element_to_be_clickable
# 判断元素是否被选中,一般用在下拉列表，传入WebElement对象
element_to_be_selected
# 判断元素是否被选中
element_located_to_be_selected
# 判断元素的选中状态是否和预期一致，传入参数：定位后的元素，相等返回True，否则返回False
element_selection_state_to_be
# 判断元素的选中状态是否和预期一致，传入参数：元素的定位，相等返回True，否则返回False
element_located_selection_state_to_be
#判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了
staleness_of
'''  # 显式等待

'''
print(df.title)         # Title网页标题
print(df.current_url)   # Current URL当前网址
print(df.name)      # Name浏览器名称
print(df.page_source)       # Page source网页源码
'''  # 获取网页信息
'''
df.get("https://blog.csdn.net/")    # csdn首页    2号页面
df.back()   # 后退至1号页面
df.forward()    # 前进至2号页面
'''  # 页面前进和后退
'''
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标悬停引用
context_click() # 右击
double_click() # 双击
double_and_drop() # 拖拽
move_to_element() # 悬停
perform() # 执行所有ActionChains中存储的动作
'''  # 模拟鼠标操作
'''
from selenium.webdriver.common.keys import Keys  # 引入Keys类
send_keys(Keys.BACK_SPACE)      # 删除键
send_keys(Keys.SPACE)           # 空格键
send_keys(Keys.TAB)             # 制表键
send_keys(Keys.ESCAPE)          # 回退键
send_keys(Keys.ENTER)           # 回车
send_keys(Keys.CONTROL,'a')     # 全选
send_keys(Keys.CONTROL,'c')     # 复制
send_keys(Keys.CONTROL,'x')     # 剪切
send_keys(Keys.CONTROL,'v')     # 粘贴
send_keys(Keys.F1)              # 键盘f1
'''  # 模拟键盘操作

df.find_element(by=By.ID, value='kw')

time.sleep(3)
df.close()  # Close关闭浏览器
