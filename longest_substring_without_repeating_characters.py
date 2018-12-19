# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-12-19 18:13:39
# @Last Modified by:   Zengjq
# @Last Modified time: 2018-12-19 18:13:46


class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        m_start = 0
        m_end = 0
        m_set = set([])
        while(m_end < len(s) and m_start < len(s)):
            c = s[m_end]
            if c not in m_set:
                m_set.add(c)
                m_end += 1
                ret = max(m_end - m_start, ret)
            else:
                m_set.remove(s[m_start])
                m_start += 1
        return ret

solution = Solution()

test_cases = ("abcabcbb", "bbbbb", "pwwkew", "aab", "dvdf", "ohvhjdml", "jbpnbwwd", "gaaqfeqlqky", "hkcpmprxxxqw", "pmukfzdskwdyne", "xaxhifdzyuddj", "abba")
# test_cases = ("abba",)

for index, test_case in enumerate(test_cases):
    print('test_case', index)
    print(solution.lengthOfLongestSubstring(test_case))
