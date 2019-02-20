# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 17:07:27
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-20 17:19:05

# 99%


class Solution:

    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

test_cases = (121, -123, 120)

solution = Solution()

for test_case in test_cases:
    print(solution.isPalindrome(test_case))
