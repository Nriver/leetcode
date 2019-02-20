# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 17:07:27
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-20 19:25:48


# 60% -> 73%

class Solution:

    def longestPalindrome(self, s: 'str') -> 'str':
        result = ""
        for i in range(len(s)):
            lpd = self.do_expand(s, i, i)
            if len(lpd) > len(result):
                result = lpd

            lpd = self.do_expand(s, i, i + 1)
            if len(lpd) > len(result):
                result = lpd

        return result

    def do_expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]

test_cases = (
    "abcda",
    "ac",
    "abb",
    "babad",
    "babababd",
    "cbbd",
)

solution = Solution()

for test_case in test_cases:
    print(solution.longestPalindrome(test_case))
