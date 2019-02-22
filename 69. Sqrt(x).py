# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 17:07:27
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-23 02:51:24


class Solution:

    # 这个虽然不是解 但是是根据精度来逼近计算
    def mySqrt(self, x: 'int') -> 'int':
        if x == 1 or x == 0:
            return x
        l, r = 0, x
        while l <= r:
            if r - l < 0.1:
                return l
            mid = (l + r) / 2
            sq = mid * mid
            if sq == x:
                return mid
            if sq > x:
                r = mid
            else:
                l = mid

    # 94% mem 35%
    def mySqrt2(self, x: 'int') -> 'int':
        if x == 1 or x == 0:
            return x
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid
            sq_l = (mid + 1) * (mid + 1)
            if sq <= x and sq_l > x:
                return mid
            if sq > x and sq_l > x:
                r = mid
            else:
                l = mid


test_cases = (121, 9, 120)

solution = Solution()

for test_case in test_cases:
    print(solution.mySqrt(test_case))
