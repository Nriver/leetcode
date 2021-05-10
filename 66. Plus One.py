# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 11:53:58
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 11:56:41
class Solution:

    # 66 mem 99
    def plusOne(self, digits):
        n = 0
        for x in digits:
            n = 10*n + x
        n += 1
        return[int(x) for x in str(n)]

s = Solution()
print(s.plusOne([4,3,2,9]))