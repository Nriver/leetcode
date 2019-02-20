# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 11:07:45
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-20 12:22:52
# 97% faster


class Solution:

    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if not nums:
            return []
        res = []
        window = []
        for i, x in enumerate(nums):
            # 下标大于window的大小后开始移除左边超出window的数据
            if i >= k and window[0] <= i - k:
                window.pop(0)

            # 把window内数值小于x的数移除 这个-1很关键 可以保证下一次window向右移动时 x左边没有比x小的数
            while window and nums[window[-1]] <= x:
                window.pop()

            window.append(i)

            # 下标移动到window的长度就开始输出
            if i >= k - 1:
                res.append(nums[window[0]])

        return res


test_cases = (([1, 3, -1, -3, 5, 3, 6, 7], 3), ([1, 3, 1, 2, 0, 5], 3))

solution = Solution()

for test_case in test_cases:
    print(solution.maxSlidingWindow(test_case[0], test_case[1]))
