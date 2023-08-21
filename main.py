# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime

from test3 import abc
from test2 import open_url, get_element


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # abc()
    # open_url("www.baidu.com")
    # get_element()
    # print(type(input("输入")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


now = datetime.datetime.now()
time0 = now.strftime("%H:%M:%S")  # %Y-%m-%d %H:%M:%S
time1 = '09:00:00'
time2 = '17:20:00'
if time1 > time0:
    print(time0,111)
elif time2 > time0:
    print(time0,222)
else:
    print(time0,333)
