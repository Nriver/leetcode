# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 17:07:27
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-20 17:46:44

# 99%


class Solution:

    def romanToInt(self, s: 'str') -> 'int':
        r_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = r_map[s[-1]]

        for x in range(len(s) - 2, -1, -1):
            if r_map[s[x]] >= r_map[s[x + 1]]:
                res += r_map[s[x]]
            else:
                res -= r_map[s[x]]
        return res

test_cases = ("VII", "IV", "III", "MCMXCIV")

solution = Solution()

for test_case in test_cases:
    print(solution.romanToInt(test_case))
