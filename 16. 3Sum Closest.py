# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-02 17:32:12
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-03 09:40:50


class Solution:

    # 太慢 运行超时
    # 这个方法是把所有的组合都算一遍
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    def threeSumClosest1(self, nums, target: int) -> int:
        ln = len(nums)
        memo = {}
        for i in range(ln):
            for j in range(i+1, ln):
                for k in range(j+1, ln):
                    s = nums[i] + nums[j] + nums[k]
                    memo[abs(s-target)] = s
        return memo[min(memo.keys())]

    # 参考答案
    # 这个方法用的是two pointer
    # Runtime: 112 ms, faster than 84.61% of Python3 online submissions for 3Sum Closest.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        diff = float('inf')
        res = 0
        for i in range(len(nums)-1):
            j = i + 1
            k = len(nums) - 1
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                new_diff = abs(s - target)
                if new_diff < diff:
                    diff = new_diff
                    res = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return res
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))

    nums = [36,38,95,-89,-86,-19,63,-8,12,90,15,-84,48,50,88,88,-29,-2,99,-97,60,88,30,64,-28,-87,2,78,87,97,77,63,77,62,89,57,39,-36,39,-43,86,76,32,-71,-46,58,18,-27,52,-68,-79,-54,0,18,-88,72,-57,95,-66,73,-99,33,-16,43,81,40,0,-8,-15,6,87,-43,92,-64,68,1,-32,15,-60,-49,35,31,49,-70,65,0,-87,27,12,2,-94,79,4,41,19,-37,-79,-22,7,-25,-67,-56,34,-64,-7,-58,2,26,98,2,23,2,7,62,49,-18,44,-1,91,56,64,-98,-84,38,23,63,-80,14,56,-100,-62,19,24,-16,18,-78,-52,47,99,82,-91,-34,76,89,-56,-35,-72,-90,41,43,-43,6,-95,-63,-70,-81,-55,-63,-28,-61,-72,68,-50,72,-28,83,67,99,41,54,73,-4,14,-91,51,93,46,32,-49,87,-84,-13,57,12,74,42,33,39,-79,-56,-46,-53,-74,-88,55,-65,-75,-89,-56,97,100,7,84,79,8,24,48,-46,-95,76,73,-87,85,45,-8,-69]
    print(s.threeSumClosest(nums, 171))
