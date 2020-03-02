# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-02 09:10:57
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-02 15:18:11

class Solution:

    # 题目是正则匹配整个字符串

    # 取值范围
    # s: a-z
    # p: a-z . *

    # 特殊符号意义
    # * 是0或n次重复前一个字母
    # . 是任意字符
    # .*是0或n个任意字符

    # 这道题应该用递归或者动态规划的思路去做
    # 一开始我尝试了逐个分析 结果越写越复杂 最后没有写出来

    # 参考答案 1 递归
    # Runtime: 1204 ms, faster than 25.86% of Python3 online submissions for Regular Expression Matching.
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Regular Expression Matching.
    def isMatch1(self, s: str, p: str) -> bool:
        if not p:
            return not s

        matched = False
        if s:
            if p[0] in [s[0], '.']:
                matched = True

        if len(p) > 1 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or (matched and self.isMatch(s[1:],p)))

        return matched and self.isMatch(s[1:], p[1:])

    # 参考答案 2 动态规划
    # 思路和上面的递归类似 但是这里有一个memo来对已经计算过的子问题的答案进行记录
    # 所以会比上面快很多
    # Runtime: 40 ms, faster than 85.69% of Python3 online submissions for Regular Expression Matching.
    # Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Regular Expression Matching.
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    # pattern遍历到最后了
                    # 如果s也在最后 说明匹配了。否则是失败了
                    ans = i == len(s)
                else:
                    matched = i < len(s) and p[j] in [s[i], '.']
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or (matched and dp(i+1, j))
                    else:
                        ans = matched and dp(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)

if __name__ == '__main__':
    s = Solution()

    # True
    print(s.isMatch('abc', 'a..'))

    # True
    print(s.isMatch('aaaa', 'a*'))

    # True
    print(s.isMatch('aaaba', 'a*ba'))

    # False
    print(s.isMatch('aaaba', 'a*'))

    # False
    print(s.isMatch('mississippi', 'mis*'))

    # True
    print(s.isMatch('mississippi', 'mis*is*ip*i'))
        
    # True
    print(s.isMatch('aabc', 'a*..'))

    # True
    print(s.isMatch('aaaa', 'a*.'))

    # True
    print(s.isMatch('aaaa', 'a*.a'))

    # True
    print(s.isMatch('ab','a.*'))

    # True
    print(s.isMatch('ab','a.*b'))

    # True
    print(s.isMatch('mississippi', 'mis*is*ip*.'))

    # True
    print(s.isMatch('ab','.*'))


