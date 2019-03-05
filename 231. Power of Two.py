# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 17:07:27
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-06 00:16:29

# leetcode没看到效率特别高的代码
# 主要这里学到的是 x&(x-1) 能把x转成2进制后最右边的一个1去掉
# 如果x是2的倍数 那去掉这个1就没数字 x&(x-1)的结果就是0了


class Solution:

    # 求导数的方法不可行53687091253687这个数求导数的结果不正确...
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     return math.log(n, 2).is_integer()

    # 65% mem 6%
    # 跟下面自己写的那个一直除2一样的效率
    # 但是代码看着更简洁
    def isPowerOfTwo1(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n / 2
        return n == 1

    # 65% mem 6%
    # 一直除2
    def isPowerOfTwo2(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while True:
            n, rem = divmod(n, 2)
            if rem != 0:
                return False
            if n == 1:
                return True

    # 63% mem 6%
    # 位运算 为什么效率不高?
    def isPowerOfTwo22(self, n: int) -> bool:
        if n <= 0:
            return False
        if (n & (n - 1)) == 0:
            return True
        return False

    # 更简洁的写法
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

    # leetcode上的一些神奇解法
    def isPowerOfTwo3(self, n):
        return -n & n == n > 0

    # 甚至还有这种...
    isPowerOfTwo4 = {1 << e for e in range(31)}.__contains__


test_cases = (1, 128, -123, 120,
              53687091253687)

solution = Solution()

for test_case in test_cases:
    print(solution.isPowerOfTwo(test_case))
