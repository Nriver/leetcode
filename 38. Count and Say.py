# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-19 17:38:52
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 10:10:28


# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221

class Solution:

    # 35% mem 99%
    def countAndSay1(self, n):
        res = ''
        if not n:
            return res
        if n==1:
            return "1"
        res = '1'
        for _ in range(n-1):
            res = self.sub_count(res)
        return res

    def sub_count(self, s):
        # print(s)
        res = ''
        prev = s[0]
        count = 0
        for x in s:
            if x==prev:
                count += 1
            else:
                res += f'{count}{prev}'
                prev = x
                count = 1
        res += f'{count}{prev}'

        return res

    # 94%-59% mem 99%
    def countAndSay(self, n):
        res = ''
        if not n:
            return res
        if n==1:
            return "1"
        res = '1'
        for _ in range(n-1):
            tmp = ''
            prev = res[0]
            count = 0
            for x in res:
                if x==prev:
                    count += 1
                else:
                    tmp += f'{count}{prev}'
                    prev = x
                    count = 1
            tmp += f'{count}{prev}'
            res = tmp
        return res

s = Solution()
print(s.countAndSay(4))