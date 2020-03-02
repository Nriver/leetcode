# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-02 15:21:23
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-02 16:07:03

class Solution:

    # Runtime: 12 ms, faster than 100.00% of Python3 online submissions for Remove Element.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Element.
    # def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement1(self, nums, val) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

    def removeElement(self, nums, val) -> int:
        return 0

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3, 2, 2, 3], 3))
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))