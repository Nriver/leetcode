# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-12-19 10:46:12
# @Last Modified by:   Zengjq
# @Last Modified time: 2018-12-19 10:46:47


class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for x in range(len(nums)):
            num = nums[x]
            ret = nums_dict.get(target - num, None)
            if ret is not None and ret != x:
                return [ret, x]
            nums_dict[num] = x


test_cases = (([3, 2, 4], 6),
              ([2, 7, 11, 15], 9),
              ([3, 3], 6))

solution = Solution()

for test_case in test_cases:
    print(solution.twoSum(test_case[0], test_case[1]))
