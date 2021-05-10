# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 16:12:10
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 16:22:16
class Solution:

    # 92 mem 53
    def minFlips1(self, target: str) -> int:
        prev = '0'
        res = 0
        for x in target:
            if x != prev:
                res += 1
                prev = x
        return res



s = Solution()
print(s.minFlips('10111'))
print(s.minFlips('001011101'))