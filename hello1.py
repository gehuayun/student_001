from day11_tpshop import page
from day11_tpshop.base.base import Base
from day11_tpshop.base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class PageLogin(Base):
    # 点击 登录链接
    def page_click_login_link(self):
        log.info("[page_login]:执行{}元素点击链接操作".format(page.login_link))
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        log.info("[page_login]:对{}元素 输入用户名{}操作".format(page.login_username, username))
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        log.info("[page_login]:对{}元素 输入密码{}操作".format(page.login_pwd, pwd))
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        log.info("[page_login]:对{}元素 输入验证码{}操作".format(page.login_verify_code, verify_code))
        self.base_input(page.login_verify_code, verify_code)

    # 点击 登录
    def page_click_login_btn(self):
        log.info("[page_login]:执行{}元素点击操作".format(page.login_btn))
        self.base_click(page.login_btn)

    # 获取 错误提示信息
    def page_get_err_info(self):
        return self.base_get_text(page.login_err_info)

    # 点击 错误提示框 确定按钮
    def page_click_error_alert(self):
        log.info("[page_login]:执行{}元素点击操作".format(page.login_err_ok_btn))
        self.base_click(page.login_err_ok_btn)

    # 判断是否登录成功
    def page_if_login_success(self):
        # 注意 一定要将找元素的结果返回，True：存在
        return self.base_elememt_is_exist(page.login_logout_link)

    # 点击 安全退出
    def page_click_logout_link(self):
        self.base_click(page.login_logout_link)

    # 判断是否退出成功
    def page_if_logout_success(self):
        return self.base_elememt_is_exist(page.login_link)

    # 组合业务方法 登录业务直接调用
    def page_login(self, username, pwd, verify_code):
        log.info("[page_login]:正在执行登录操作，用户名：{}，密码：{}，验证码：{}".format(username, pwd, verify_code))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()

    # 组合登录业务方法 给（购物车模块、订单模块、支付模块）依赖登录使用
    def page_login_success(self, username="13800001111", pwd="123456", verify_code="8888"):
        # 点击登录链接
        self.page_click_login_link()
        log.info("[page_login]:正在执行登录操作，用户名：{}，密码：{}，验证码：{}".format(username, pwd, verify_code))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()