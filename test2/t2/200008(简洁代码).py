def new_data():
    """
    针对字典数据， 输出元组列表， 每个元组由字典的键值组成， 其中值大于100
    """
    data_ = {"A": 100, "B": 99, "C": 33, "D": 120}

    v_ = [(k, v) for k, v in data_.items() if v >= 100]
    print(f"输出:{v_}")


def new_text():
    """
    针对多行字符串， 过滤掉所有不多于3个字母的单词
    """
    text = '''Outside, the moon is shedding its cold light on the cold snow, and the white-bearded fir-trees round 
    Camp Villa1 are casting a blue shadow across the white ground, while the Rev2 '''

    n_ = [[x for x in line.split() if len(x) < 3] for line in text.split("\n")]
    print(f'输出：{n_}')


'''
# 读取一个文件，输出一个由每行（去除行前后空白字符）组成字符串的列表，文件名：readfile.txt
py_ = [line.strip() for line in open("...\t2\readFile.txt")]        # 未成功
print(f"例三输出：{py_}")
'''


def new_e():
    """
    针对一个字符串列表，输出由元组组成（由一个布尔值（判断'a'是否出现在原字符串中）和对应的原字符串组成）的新列表的值
    """
    e_ = ["abc", "a", "b", "c", "d", "a", "e", "a", "e"]

    m = map(lambda s: (True, s) if "a" in s else (False, s), e_)
    print(f"例四输出：{list(m)}")


# 针对多行字符串，输出指定内容以及前后至多各18个位置的字符

q = "snow"
x = "the moon is shedding its cold light on the cold snow the white-bearded fir-trees round Camp Villa1 are casting"

fs = lambda x, q: x[x.find(q) - 18:x.find(q) + 18] if q in x else -1
print(f"例五输出：{fs(x, q)}")

# new_data()
# new_text()
# new_e()
