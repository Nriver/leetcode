# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 15:23:40
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 16:10:22

class Solution:

    # 79 mem 100
    def subsets1(self, nums):
        res = []
        l = len(nums)
        # 转换成一个二进制过滤器问题
        for x in range(2 ** l):
            selectors = [int(y) for y in bin(x)[2:].zfill(l)]
            subset = list(d for d, s in zip(nums, selectors) if s)
            # print(subset)
            res.append(subset)
        return res

    # 别人的答案
    # 这个很巧妙
    def subsets(self, nums):
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets]
        return subsets



s = Solution()
s.subsets([1,2,3])
        