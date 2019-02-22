# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 11:14:01
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-22 16:54:21

# 99%


class Solution:

    def maxProfit(self, prices: 'List[int]') -> 'int':
        res = 0
        for x in range(len(prices) - 1):
            if prices[x] < prices[x + 1]:
                res += prices[x + 1] - prices[x]
        return res

test_cases = ([7, 1, 5, 3, 6, 4],
              [1, 2, 3, 4, 5],
              )

solution = Solution()

for test_case in test_cases:
    print(solution.maxProfit(test_case))
