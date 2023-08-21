import zipfile
import itertools


def ext_file(pwd):
    try:
        # 创建 ZipFile 对象
        with zipfile.ZipFile('2.zip') as zfile:
            # 解压文件
            zfile.extractall(path='./', pwd=pwd.encode('utf-8'))
            print('文件解压成功')
            return True
    except Exception as e:
        print('失败啦！', e)
        return False


def get_pwds(my_password_str, nums):
    for x in itertools.permutations(my_password_str, nums):
        yield ''.join(x)


if __name__ == '__main__':
    my_password_str = "abcdefghijklmnopqrstuvwxyz0123456789"
    # n = 4
    # while True:
    #     for pwd in get_pwds(my_password_str, n):
    #         print(len(pwd))
    #         print("正在测试密码：", pwd)
    #         yield_pwd = pwd
    #         ret = ext_file(yield_pwd)
    #         if ret:
    #             print("解密成功，密码是", yield_pwd)
    #             break
    #     n = +1

    for pwd in get_pwds(my_password_str, 8):
        print(len(pwd))
        print("正在测试密码：", pwd)
        yield_pwd = pwd
        ret = ext_file(yield_pwd)
        if ret:
            print("解密成功，密码是", yield_pwd)
            break
