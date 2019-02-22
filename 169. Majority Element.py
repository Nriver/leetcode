# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 11:14:01
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-21 12:31:59


class Solution:

    # 99%
    def majorityElement(self, nums: 'List[int]') -> 'int':
        nums.sort()
        return nums[len(nums) // 2]

    # 70%
    def majorityElement2(self, nums: 'List[int]') -> 'int':
        counter = {}
        for x in nums:
            if x not in counter:
                counter[x] = 1
            else:
                counter[x] += 1
        res = nums[0]
        for x in counter:
            if counter[x] > counter[res]:
                res = x
        return res


test_cases = (
    [1],
    [3, 3, 4],
    [3, 2, 3],
    [2, 2, 1, 1, 1, 2, 2],
)

solution = Solution()

for test_case in test_cases:
    print(solution.majorityElement(test_case))
