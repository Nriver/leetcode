# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-03 14:28:48
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-03 14:38:16

class Solution:

    # Runtime: 52 ms, faster than 85.22% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    def smallerNumbersThanCurrent(self, nums):
        s = sorted(nums)
        rank = {}
        # print(s)
        for x in range(len(s)-1, 0, -1):
            # print(x)
            if s[x] != s [x-1]:
                if s[x] not in rank:
                    rank[s[x]] = x
        # print(rank)

        res = []
        for x in nums:
            res.append(rank.setdefault(x, 0))

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.smallerNumbersThanCurrent([8,1,2,2,3]))
    print(s.smallerNumbersThanCurrent([7,7,7,7,7]))