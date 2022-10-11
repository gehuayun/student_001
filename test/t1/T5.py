# #include <stdio.h>
# int main()
# {
#      int i = 0;
#      #//for(i=1/*初始化*/; i<=10/*判断部分*/; i++/*调整部分*/)
#      for(i=1; i<=10; i++) #//第二次循环时，不再执行表达式1
#      {
#         printf("%d ", i) ;
#      }
#  	return 0;
#  }


# int main()
# {
# 	int i = 1;
# 	while (i <= 10)
# 	{
#         if (i == 5)//当i循环到5时，执行if语句
# 		break;//执行完if语句跳出本循环
# 		printf("%d\t ", i)
#         i++
# 	}
#     printf("haha\n")#//跳到此处继续向下执行
#     return 0
# }
# # //执行结果为：1        2       3       4       haha
#

#################################
##  for循环
# j = 0
# for i in range(101):
#     if j >= 5000:
#         break  # //打断循环
#     elif i == 50:
#         print(j)
#         continue  # //跳过循环
#     else:
#         j += i
# print(j)
# print(i)
# main = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]
# print(10 not in main)
# while i > 0:
#     if i == 50:
#         i -= 1
#         continue
#     j += i
#     i -= 1
# print(j)
