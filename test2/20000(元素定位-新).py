"""
selenium中find_element定位方式
find_element(By.XPATH)
find_element(By.CSS_SELECTOR)
find_element(By.ID)
find_element(By.TAG_NAME)
find_element(By.class_name,)
find_element(By.PARTIAL_LINK_TEXT)
find_element(By.LINK_TEXT)
find_element(By.name)

e1为悬停开启按钮
from selenium.webdriver.common.action_chains import ActionChains

ActionChains(driver).move_to_element(el).perform()  # 鼠标悬停


setTimeout(function(){debugger},3000)
            #在控制台输入命令3秒内移动鼠标至悬停弹窗 页面会自动暂停


            鼠标悬停到标签上后，在Sources中按Ctrl + \ 组合键，进入debug模式，动效JS会停止继续执行

click()     # 鼠标左击点击一下
send_keys()   # 在输入框内输入信息




# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# 将option作为参数添加到Chrome中
driver = webdriver.Chrome(chrome_options=option)


#后退
driver.back()
sleep(2)
#前进
driver.forward()

# 刷新页面
driver.refresh()


# 设置浏览器浏览器的宽高为 600x800
driver.set_window_size(600, 800)
# 浏览器放大
driver.maximize_window()




浏览器窗口切换
在很多时候我们都需要用到窗口切换，
比如：当我们点击注册按钮时，
它一般会打开一个新的标签页，
但实际上代码并没有切换到最新页面中，
这时你如果要定位注册页面的标签就会发现定位不到，
这时就需要将实际窗口切换到最新打开的那个窗口。
我们先获取当前各个窗口的句柄，
这些信息的保存顺序是按照时间来的，
最新打开的窗口放在数组的末尾，
这时我们就可以定位到最新打开的那个窗口了。

1.关闭浏览器全部标签页                                            driver.quit()
2.关闭当前标签页（从标签页A打开新的标签页B，关闭标签页A）                 driver.close()
3.关闭当前标签页（从标签页A打开新的标签页B，关闭标签页B）
可利用浏览器自带的快捷方式对打开的标签进行关闭
Firefox自身的快捷键分别为：
Ctrl+t 新建tab
Ctrl+w 关闭tab
Ctrl+Tab /Ctrl+Page_Up 定位当前标签页的下一个标签页
Ctrl+Shift+Tab/Ctrl+Page_Down 定位当前标签页的前一个标签页
Ctrl+[数字键1-8] 定位所有标签页中最前的第[1-8]个
Ctrl+数字键9 定位最后一个标签页
注：如果是在一些Linux发行版系统中,比如Ubuntu,需要将Ctrl键换成Alt键
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#新建标签页
ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
# 关闭标签页
ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
4.标签页切换
from selenium import webdriver
browser=webdriver.Firefox()
browser.get('xxxxx')
# 获取当前窗口句柄（窗口A）
handle = browser.current_window_handle
# 打开一个新的窗口
browser.find_element_by_id('xx').click()
# 获取当前所有窗口句柄（窗口A、B）
handles = browser.window_handles                #################################
# 对窗口进行遍历
for newhandle in handles:
# 筛选新打开的窗口B
if newhandle!=handle:
# 切换到新打开的窗口B
browser.switch_to.window(newhandle)
# 在新打开的窗口B中操作
browser.find_element_by_id('xx').click()
# 关闭当前窗口B
browser.close()
#切换回窗口A
browser.switch_to.window(handles[0])            ##########################
# 获取打开的多个窗口句柄
windows = driver.window_handles             ######################
# 切换到当前最新打开的窗口
driver.switch_to.window(windows[-1])            ##############

driver.maximize_window()  # 最大化浏览器
driver.set_window_size(w,h)  # 设置浏览器大小 单位像素 【了解】
driver.set_window_position(x,y)  # 设置浏览器位置  【了解】
driver.back() # 后退操作
driver.forward() # 前进操作
driver.refrensh() # 刷新操作
driver.close() # 关闭当前主窗口（主窗口：默认启动那个界面，就是主窗口）
driver.quit() # 关闭driver对象启动的全部页面
driver.title # 获取当前页面title信息
driver.current_url # 获取当前页面url信息


常见操作
webdriver中的常见操作有
方法           描述
send_keys()       模拟输入指定内容
clear()           清除文本内容
is_displayed()    判断该元素是否可见
get_attribute()   获取标签属性值
size           返回元素的尺寸
text            返回元素文本

鼠标控制
在webdriver中鼠标操作都封装在ActionChains类中
常见方法如下
方法         描述
click()	            单击左键
context_click()	    单击右键
double_click()	    双击
drag_and_drop()	    拖动
move_to_element()	鼠标悬停
perform()	        执行所有ActionChains中存储的动作

键盘操作
from selenium.webdriver.common.keys import Keys
操作	            描述
Keys.ENTER          enter回车键
Keys.BACK_SPACE     backspace删除键
Keys.CONTROL,'a'    ctrl+a 全选
Keys.CONTROL,'c'    ctrl+c 复制
Keys.CONTROL,'v'    ctrl+v 粘贴
Keys.F1	            F1键
Keys.SPACE	        空格
Keys.TAB	        Tab键
Keys.ESCAPE	        ESC键
Keys.ALT	        Alt键
Keys.SHIFT	        Shift键
Keys.ARROW_DOWN	    向下箭头
Keys.ARROW_LEFT	    向左箭头
Keys.ARROW_RIGHT	向右箭头
Keys.ARROW_UP	    向上箭头

设置元素等待
很多页面都使用 ajax 技术 页面的元素不是同时被加载出来的
为了防止定位这些尚在加载的元素报错 可以设置元素等来增加脚本的稳定性。
webdriver 中的等待分为 显式等待 和 隐式等待。

显式等待
设置一个超时时间 每个一段时间就去检测一次该元素是否存在
如果存在则执行后续内容 如果超过最大时间（ 超时时间） 则抛出超时异常（ TimeoutException ）。
显示等待需要使用 WebDriverWait  同时配合 until 或 not until 。下面详细讲解一下。

WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

driver              浏览器驱动
timeout             超时时间，单位秒
poll_frequency      每次检测的间隔时间默认为0.5秒
ignored_exceptions  指定忽略的异常，如果在调用 until 或 until_not 的过程中抛出指定忽略的异常，则不中断代码，默认忽略的只有 NoSuchElementException 。
until(method, message=’ ‘)
until_not(method, message=’ ')

method              指定预期条件的判断方法，在等待期间，每隔一段时间调用该方法，
                    判断元素是否存在 直到元素出现。until_not 正好相反，当元素消失或指定条件不成立，则继续执行后续代码
message:            如果超时，抛出 TimeoutException ，并显示 message 中的内容
method 中的预期条件判断方法是由 expected_conditions 提供，下面列举常用方法。

先定义一个定位器
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
locator = (By.ID, 'kw')
element = driver.find_element_by_id('kw')

方法	                                                     描述
title_is(‘百度一下’)	                                    判断当前页面的 title 是否等于预期
title_contains(‘百度’)	                                    判断当前页面的 title 是否包含预期字符串
presence_of_element_located(locator)	                    判断元素是否被加到了 dom 树里，并不代表该元素一定可见
visibility_of_element_located(locator)	                    判断元素是否可见，可见代表元素非隐藏，并且元素的宽和高都不等于0
visibility_of(element)	                                    跟上一个方法作用相同，但传入参数为 element
text_to_be_present_in_element(locator , ‘百度’)	            判断元素中的 text 是否包含了预期的字符串
text_to_be_present_in_element_value(locator , ‘某值’)	    判断元素中的 value 属性是否包含了预期的字符串
frame_to_be_available_and_switch_to_it(locator)	            判断该 frame 是否可以 switch 进去，True 则 switch 进去，反之 False
invisibility_of_element_located(locator)	                判断元素中是否不存在于 dom 树或不可见
element_to_be_clickable(locator)	                        判断元素中是否可见并且是可点击的
staleness_of(element)	                                    等待元素从 dom 树中移除
element_to_be_selected(element)	                            判断元素是否被选中,一般用在下拉列表
element_selection_state_to_be(element, True)	            判断元素的选中状态是否符合预期，参数 element，第二个参数为 True/False
element_located_selection_state_to_be(locator, True)	    跟上一个方法作用相同，但传入参数为 locator
alert_is_present()	                                        判断页面上是否存在 alert
下面写一个简单的例子，这里定位一个页面不存在的元素，抛出的异常信息正是我们指定的内容。

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
element = WebDriverWait(driver, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, 'kw')),
                                           message='超时啦!')


隐式等待
隐式等待也是指定一个超时时间，
如果超出这个时间指定元素还没有被加载出来，就会抛出 NoSuchElementException 异常。
除了抛出的异常不同外，还有一点，隐式等待是全局性的，即运行过程中，
如果元素可以定位到，它不会影响代码运行，
但如果定位不到，则它会以轮询的方式不断地访问元素直到元素被找到，若超过指定时间，则抛出异常。

使用 implicitly_wait() 来实现隐式等待，使用难度相对于显式等待要简单很多。
示例：打开个人主页，设置一个隐式等待时间 5s 
通过 id 定位一个不存在的元素，最后打印 抛出的异常 与 运行时间。

from selenium import webdriver
from time import time

driver = webdriver.Chrome()
driver.get('https://blog.csdn.net/qq_43965708')

start = time()
driver.implicitly_wait(5)
try:
    driver.find_element_by_id('kw')
except Exception as e:
    print(e)
    print(f'耗时：{time()-start}')

代码运行到 driver.find_element_by_id('kw') 这句之后触发隐式等待，
在轮询检查 5s 后仍然没有定位到元素，抛出异常。


强制等待
使用 time.sleep() 强制等待，设置固定的休眠时间，对于代码的运行效率会有影响。
以上面的例子作为参照，将 隐式等待 改为 强制等待。

from selenium import webdriver
from time import time, sleep

driver = webdriver.Chrome()
driver.get('https://blog.csdn.net/qq_43965708')

start = time()
sleep(5)
try:
    driver.find_element_by_id('kw')
except Exception as e:
    print(e)
    print(f'耗时：{time()-start}')

    


定位一组元素
上篇讲述了定位一个元素的 8 种方法，
定位一组元素使用的方法只需要将 element 改为 elements 即可，
它的使用场景一般是为了批量操作元素。

find_elements_by_id()
find_elements_by_name()
find_elements_by_class_name()
find_elements_by_tag_name()
find_elements_by_xpath()
find_elements_by_css_selector()
find_elements_by_link_text()
find_elements_by_partial_link_text()


切换操作
窗口切换
在 selenium 操作页面的时候，
可能会因为点击某个链接而跳转到一个新的页面（打开了一个新标签页），
这时候 selenium 实际还是处于上一个页面的，需要我们进行切换才能够定位最新页面上的元素。

窗口切换需要使用 switch_to.windows() 方法



"""
