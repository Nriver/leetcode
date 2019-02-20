# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 17:07:27
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-20 17:59:50

# 98%
# 题目简单就是边界值和特殊情况很烦人


class Solution:

    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if len(strs) == 0:
            return ""

        sample = strs.pop()
        if sample == "":
            return ""

        common_prefix = ""
        for i, x in enumerate(sample):
            for y in strs:
                if y == "":
                    return ""
                if len(y) < i + 1 or y[i] != x:
                    return common_prefix
            common_prefix += x
        return common_prefix

test_cases = (["", "b"], ["flower", "flow", "flight"], ["dog", "racecar", "car"], ["aaa", "aa", "aaa"])

solution = Solution()

for test_case in test_cases:
    print(solution.longestCommonPrefix(test_case))
