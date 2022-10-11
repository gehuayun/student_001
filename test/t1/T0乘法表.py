print("hello world")
for j in range(1, 10):      #计从1到9，不包括10，而且1-9是连续的range(100)默认0-99
    for i in range(1, j+1): #观察发现乘号左边的数字小于等于右边的数字，i左，j右,一般二层循环的变量小于一层的(非通用)
        result = i * j
        if i <j:                                        #观察每一行的最后一个式子会发现换行的根据，
            print(i, '*', j, '=', result, ' ', end = '')# 即，除最后一个式子，左都小于右（i<j），而且连续打印
                                                         # 不换行（所以用end=''）
        else:                                           #换行的根据是i=j,虽然要换行，但也是打印了之后换行的
            print(i, '*', j, '=', result, ' ')          #i不可能大于j,因为i的范围就是range(1, j+1)
