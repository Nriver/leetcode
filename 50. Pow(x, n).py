# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 11:14:01
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-21 12:04:42


# 教程 https://time.geekbang.org/course/detail/130-42711


class Solution:
    # 100% 速度 98% 内存 最优解

    def myPow(self, x: 'float', n: 'int') -> 'float':
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

    def myPow1(self, x: 'float', n: 'int') -> 'float':
        return x ** n

    def myPow2(self, x: 'float', n: 'int') -> 'float':
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow2(x, -n)
        if n % 2:
            return x * self.myPow2(x, n - 1)
        return self.myPow2(x * x, n / 2)


test_cases = ([2, 4],
              [3, 3],
              )

solution = Solution()

for test_case in test_cases:
    print(solution.myPow3(test_case[0], test_case[1]))
