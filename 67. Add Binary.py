# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 12:01:58
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 12:06:03
class Solution:

    # 75 mem 99
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, base=2) + int(b, base=2))

s = Solution()
print(s.addBinary('11','1'))