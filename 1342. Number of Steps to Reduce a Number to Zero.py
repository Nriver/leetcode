# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-02-21 10:19:11
# @Last Modified by:   zengjq
# @Last Modified time: 2020-02-21 10:37:16

class Solution:

    # Runtime: 20 ms, faster than 96.38% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    def numberOfSteps (self, num: int) -> int:
        counter = 0
        while num != 0:
            if num % 2 == 0:
                num = num/2
            else:
                num = num -1
            counter += 1
        return counter

    # 用内置的divmod函数结果比上面的要慢
    # Runtime: 32 ms, faster than 19.69% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    def numberOfSteps2 (self, num: int) -> int:
        counter = 0
        while num != 0:
            q, r = divmod(num, 2)
            if r:
                num -= 1
            else:
                num = q
                
            counter += 1
        return counter

    # 另外一种优化
    def numberOfSteps3 (self, num: int) -> int:
        counter = 0
        while num != 0:
            if num % 2 == 0 or num == 1:
                counter += 1
            else:
                # 减1再除2合起来，计数器一次性加2
                counter += 2
            num = num//2
        return counter


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSteps3(14))
    print(s.numberOfSteps3(8))
    print(s.numberOfSteps3(123))
