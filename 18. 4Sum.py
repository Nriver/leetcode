# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-05 11:28:42
# @Last Modified by:   zengjq
# @Last Modified time: 2020-05-21 11:54:57

# https://leetcode.com/problems/4sum/

# 我自己写的n sum通用解法，不过执行速度太慢，leetcode执行超时，里面有很多可以优化的地方
class Solution:

    # 可以转换成threeSum问题, twoSum,一直降级
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def fourSum(self, nums, target: int):
        # nums.sort()
        if len(nums) < 4:
            return []
        print(nums)
        res = self.nSum(nums, target, 4, [], [])
        return res

    def nSum(self, nums, target, size, num_stack, result):
        # print('nums', nums, 'num_stack', num_stack)
        if size == 1:
            if target in nums:
                num_stack.append(target)
                num_stack.sort()
                if num_stack not in result:
                    result.append(num_stack)
                return result
        else:
            for x in range(len(nums)):
                num = nums[x]
                new_nums = nums[:x]+nums[x+1:]
                sub_num_stack = [num,]
                sub_num_stack.extend(num_stack)
                result = self.nSum(new_nums, target-num, size-1, sub_num_stack, result)
        return result


class Solution:
    # 尝试用排序做

    # Runtime: 6572 ms, faster than 5.03% of Python3 online submissions for 4Sum.
    # Memory Usage: 14.1 MB, less than 7.14% of Python3 online submissions for 4Sum.
    def fourSum1(self, nums, target: int):
        if not nums:
            return []
        res = set()
        nums.sort()
        L = len(nums)
        for i in range(0, L-3):
            a = nums[i]
            if a * 4 > target:
                break
            for j in range(i+1, L-2):
                b = nums[j]
                if a + b * 3 > target:
                    break
                for k in range(j+1, L-1):
                    c = nums[k]
                    if a + b + c * 2 > target:
                        break
                    for l in range(k+1, L):
                        d = nums[l]
                        if (a + b + c + d) == target:
                            res.add((a,b,c,d))
        return res

    # 优化 最内层遍历改成用dict查找
    # Runtime: 828 ms, faster than 54.55% of Python3 online submissions for 4Sum.
    # Memory Usage: 13.8 MB, less than 7.14% of Python3 online submissions for 4Sum.
    def fourSum2(self, nums, target: int):
        if not nums:
            return []
        res = set()
        nums.sort()
        L = len(nums)
        N = {j:i for i,j in enumerate(nums)}
        for i in range(0, L-3):
            a = nums[i]
            if a * 4 > target:
                break
            for j in range(i+1, L-2):
                b = nums[j]
                if a + b * 3 > target:
                    break
                for k in range(j+1, L-1):
                    c = nums[k]
                    if a + b + c * 2 > target:
                        break
                    d = target - ( a + b + c )
                    if d in N and N[d] > k:
                        res.add((a, b, c, d))
        return res

    # 再优化 把当前的数和最大的几个数组成一组 如果还达不到 就不再深入 直接进入下一个循环
    # 
    # Runtime: 48 ms, faster than 99.86% of Python3 online submissions for 4Sum.
    # Memory Usage: 13.9 MB, less than 7.14% of Python3 online submissions for 4Sum.
    # Runtime: 56 ms, faster than 99.47% of Python3 online submissions for 4Sum.
    # Memory Usage: 14 MB, less than 7.14% of Python3 online submissions for 4Sum.
    # Runtime: 80 ms, faster than 97.29% of Python3 online submissions for 4Sum.
    # Memory Usage: 13.9 MB, less than 7.14% of Python3 online submissions for 4Sum.
    def fourSum(self, nums, target: int):
        if not nums or len(nums) < 4:
            return []
        res = set()
        nums.sort()
        L = len(nums)
        N = {j:i for i,j in enumerate(nums)}
        M_1 = nums[-1]
        M_2 = nums[-2]
        M_3 = nums[-3]
        for i in range(0, L-3):
            a = nums[i]
            if (a + M_3 + M_2 + M_1) < target:
                continue
            if 4 * a > target:
                break
            for j in range(i+1, L-2):
                b = nums[j]
                if (a + b + M_2 + M_1) < target:
                    continue
                if a + 3 * b > target:
                    break
                for k in range(j+1, L-1):
                    c = nums[k]
                    if a + b + 2 * c > target:
                        break
                    d = target - ( a + b + c )
                    if d in N and N[d] > k:
                        res.add((a, b, c, d))
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(s.fourSum([0, 0, 0, 0], 0))

    # nums = [-489,-487,-471,-464,-451,-421,-414,-405,-396,-355,-354,-350,-336,-335,-334,-307,-298,-296,-295,-287,-267,-256,-247,-231,-170,-130,-120,-109,-96,-80,-78,-71,-63,-56,-44,-43,-13,2,9,18,31,36,39,43,49,49,50,61,68,73,99,107,112,113,120,121,173,180,185,190,203,210,233,246,258,296,319,340,345,370,371,378,395,418,436,444,447,451,460,485]
    # target = 2926
    # print(s.fourSum(nums, target))