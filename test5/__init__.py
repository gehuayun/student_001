"""
title = '这是一个?带\有/特:殊*符"号|的标题'
content = '这是内容!'
character = '\/:*?"<>|'
for s in character:
    if s in title:
        print(s)  # 打印特殊字符
        title = title.replace(s, 'Y')  # 替换成“Y”
print(title)  # 打印替换后的title
with open(title + '.txt', 'a', encoding='utf-8') as fp:
    fp.write(content)

依次遍历字符串，然后利用 if来判断title中是否存在敏感字符，
如果存在，则使用replace()函数将特殊字符替换掉（这里为了区分，我换成“Y”）
"""