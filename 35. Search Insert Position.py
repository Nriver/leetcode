# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-03 11:37:02
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-03 11:43:28

class Solution:

    # Runtime: 44 ms, faster than 91.99% of Python3 online submissions for Search Insert Position.
    # Memory Usage: 13.6 MB, less than 74.63% of Python3 online submissions for Search Insert Position.
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target: int) -> int:
        i = 0
        end = len(nums)
        while i<end:
            if nums[i] >= target:
                break
            i += 1
        return i

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 0))
    print(s.searchInsert([1,3,5,6], 7))