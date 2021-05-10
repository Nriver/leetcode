# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 13:38:24
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 13:45:16
class Solution:

    # 92 mem 99
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

s = Solution()
print(s.climbStairs(10))