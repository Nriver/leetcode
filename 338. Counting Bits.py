# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 17:07:27
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-03-06 00:14:23

# leetcode 有更好的解法但是太难想了


class Solution:

    # 28% mem 5%
    def countBits(self, num: int):
        res = []
        for x in range(num + 1):
            counter = 0
            while x != 0:
                x = x & (x - 1)
                counter += 1
            res.append(counter)
        return res


test_cases = (2, 3,)

solution = Solution()

for test_case in test_cases:
    print(solution.countBits(test_case))
