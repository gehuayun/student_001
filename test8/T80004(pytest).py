import pytest


class Test_login():  # 登录模块的测试类
    # 该测试类---有个前置的操作（初始化）
    def setup_class(self):  # 类级别的初始化--可选项
        # 一个项目，先登录，再购物，登录就是购物类的前置条件，可以放在setup_class里面
        print("执行测试类之前，我需要执行操作")

    def test_login01(self):
        print("---test_login01----")
        assert 1 + 1 == 2

    def test_login02(self):
        print("---test_login02----")
        assert 1 + 1 == 3

    def teardown(self):  # 看业务本身需不需要初始化和清除环境，--可选项
        print("------该测试类的环境清除-----")


if __name__ == '__main__':
    pytest.main(["test_func01.py", "-s"])
