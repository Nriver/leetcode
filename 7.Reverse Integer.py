# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 10:30:18
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-20 11:03:39

# The same code could have different rank result, so try submit to leetcode more than once did change the rank.
# https://leetcode.com/submissions/detail/209197753/


class Solution:

    def reverse(self, x: 'int') -> 'int':
        res = 0
        is_negative = False
        # deal with negative, treat as positive numbers
        if x < 0:
            is_negative = True
            x = -x
        while(True):
            # get lowest digit one by one
            x, rem = divmod(x, 10)
            res = res * 10 + rem
            if x == 0:
                break
        if is_negative:
            res = -res
        if res > (2 ** 31 - 1) or res < (-2 ** 31):
            return 0
        return res

test_cases = (123, -123, 120)

solution = Solution()

for test_case in test_cases:
    print(solution.reverse(test_case))
