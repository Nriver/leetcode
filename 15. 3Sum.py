# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-12-19 10:46:12
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-20 15:29:14

# 88%


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solutions = []
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    solutions.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return solutions


test_cases = ([0, 0, 0, 0],
              )

solution = Solution()

for test_case in test_cases:
    print(solution.threeSum(test_case))
