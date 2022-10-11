test1 = [a * a for a in range(1, 10)]
print(test1)
# test2九九乘法表
print('\n'.join([' '.join([f"{j}*{i}={i*j}"for j in range(1, i+1)])for i in range(1, 10)]))
for m in range(1, 10):
    for n in range(1, m + 1):
        print(f"%s*%s=%s" % (n, m, m * n), end=' ')
    print()


def test3(z):
    if z < 10:
        for o in range(1, z + 1):
            print(f"{o}*{z}={o * z}", end='\t')
        print()
        test3(z+1)


test3(1)


class Solution:
    # 参数N为整数
    # 返回整数
    def numTilings(self, N):
        if N < 3:
            return N
        MOD = 1000000007
        f = [[0, 0, 0] for i in range(N + 1)]
        f[0][0] = f[1][0] = f[1][1] = f[1][2] = 1
        for i in range(2, N + 1):
            f[i][0] = (f[i - 1][0] + f[i - 2][0] + f[i - 2][1] + f[i - 2][2]) % MOD;
            f[i][1] = (f[i - 1][0] + f[i - 1][2]) % MOD;
            f[i][2] = (f[i - 1][0] + f[i - 1][1]) % MOD;
        return f[N][0]


if __name__ == '__main__':
    solution = Solution()
    inputnum = 3
    print("输入为：", inputnum)
    print("输出为：", solution.numTilings(inputnum))
