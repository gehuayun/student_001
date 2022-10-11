# # 逃离幽灵
# class Solution:
#     # 参数ghosts为数组
#     # 参数target为数组
#     # 返回布尔类型
#     def escapeGhosts(self, ghosts, target):
#         target_dist = abs(target[0]) + abs(target[1])
#         for r, c in ghosts:
#             ghost_target = abs(target[0] - r) + abs(target[1] - c)
#             if ghost_target <= target_dist:
#                 return False
#         return True
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     inputnum1 = [[1, 0], [0, 3]]
#     inputnum2 = [0, 1]
#     print("输入幽灵为：", inputnum1)
#     print("输入目标为：", inputnum2)
#     print("输出为：", solution.escapeGhosts(inputnum1, inputnum2))
#
#
# # 多米诺和三格骨牌铺瓦问题
# class Solution:
#     # 参数N为整数
#     # 返回整数
#     def numTilings(self, N):
#         if N < 3:
#             return N
#         MOD = 1000000007
#         f = [[0, 0, 0] for i in range(N + 1)]
#         f[0][0] = f[1][0] = f[1][1] = f[1][2] = 1
#         for i in range(2, N + 1):
#             f[i][0] = (f[i - 1][0] + f[i - 2][0] + f[i - 2][1] + f[i - 2][2]) % MOD;
#             f[i][1] = (f[i - 1][0] + f[i - 1][2]) % MOD;
#             f[i][2] = (f[i - 1][0] + f[i - 1][1]) % MOD;
#         return f[N][0]
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     inputnum = 3
#     print("输入为：", inputnum)
#     print("输出为：", solution.numTilings(inputnum))

# 反转一个3位整数
class Solution:
    # 参数number: 一个三位整数
    # 返回值: 反转后的数字
    def reverseInteger(self, number):
        h = int(number / 100)
        t = int(number % 100 / 10)
        z = int(number % 10)
        return (100 * z + 10 * t + h)


# 主函数
if __name__ == '__main__':
    solution = Solution()
    num = int(input('输入需要倒转的三位数字：'))
    ans = solution.reverseInteger(num)
    print("输入：", num)
    print("输出：", ans)
