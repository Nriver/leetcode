# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-02-25 10:56:49
# @Last Modified by:   zengjq
# @Last Modified time: 2020-02-27 09:44:35

# 这个题目的理解和我想得有偏差
# 题目要的结果只要把nums中不重复的数字个数n返回，然后nums的前n个数是按顺序排的就行，多余的元素都不用去除。
# 我的理解是把重复的元素去除再返回n。

class Solution:

    # 倒序遍历 比较慢
    # Runtime: 96 ms, faster than 40.02% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates1(self, nums):
        if not nums:
            return 0
        last_digit = nums[-1]
        for x in range(len(nums)-2, -1, -1):
            c = nums[x]
            if c == last_digit:
                nums.pop(x)
            else:
                last_digit = c
        return len(nums)

    # 内置的set函数去重
    # Runtime: 80 ms, faster than 90.68% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates2(self, nums):
        # 注意这样写结果会报错，必须加上[:] 普通list的结果是一样的，LeetCode的这个List对象的实现应该比较特殊
        # nums = sorted(set(nums))
        nums[:] = sorted(set(nums))
        return len(nums)      

    # Runtime: 84 ms, faster than 76.93% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # Memory Usage: 14.6 MB, less than 90.98% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # 按照题目的意思不去重直接找不重复的数字
    # 等于是遇到不重复的数字就冒泡
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 1
        j = 0
        while i < len(nums):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                i += 1
            else:
                i += 1
        return j + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([1,2,2]))