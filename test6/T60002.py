import os

import wechat

# 设置微信路径
wechat_path = "F:\WeChat"

# 打开微信应用程序
os.startfile(os.path.join(wechat_path, "WeChat.exe"))

# 打开微信好友列表
wechat.OpenContactList()

# 发送消息
friend = wechat.GetContactByUserName("Y13736175482")
friend.SendText("你好，我是Python脚本！")

# 关闭WeChat对象
wechat = None