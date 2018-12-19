# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-12-19 15:10:14
# @Last Modified by:   Zengjq
# @Last Modified time: 2018-12-19 15:10:19


class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        c_dict = {}
        c_start = 0
        c_end = 0
        t_dict = {}
        t_start = 0
        t_end = 0
        for index, c in enumerate(s):
            if t_dict == {}:
                if not c in c_dict:
                    c_dict[c] = index
                    c_end = index
                else:
                    if c_dict[c] == c_start:
                        c_dict[c] = index
                        c_start += 1
                        c_end = index
                    elif c_dict[c] == c_end:
                        t_start = index
                        t_end = index
                        t_dict[c] = index
                    else:
                        t_start = c_dict[c] + 1
                        t_end = index + 1
                        t_dict = {}
                        for x in range(t_start, t_end):
                            t_dict[s[x]] = x
            else:
                if c not in t_dict:
                    t_dict[c] = index
                    t_end = index + 1
                    if len(t_dict) >= len(c_dict):
                        c_dict = t_dict
                        c_start = t_start
                        c_end = t_end
                        t_dict = {}
                else:

                    if t_dict[c] == t_end:
                        t_start = index
                        t_end = index
                        t_dict = {c: index}
                    elif t_dict[c] == t_start:
                        t_dict[c] = index
                        t_start += 1
                        t_end = index
                    else:
                        t_start = t_dict[c] + 1
                        t_end = index + 1
                        t_dict = {}
                        for x in range(t_start, t_end):
                            t_dict[s[x]] = x

        return len(c_dict)

solution = Solution()

test_cases = ("abcabcbb", "bbbbb", "pwwkew", "aab", "dvdf", "ohvhjdml", "jbpnbwwd", "gaaqfeqlqky", "hkcpmprxxxqw", "pmukfzdskwdyne", "xaxhifdzyuddj")
test_cases = ("pmukfzdskwdyne",)

for index, test_case in enumerate(test_cases):
    print('test_case', index)
    print(solution.lengthOfLongestSubstring(test_case))
