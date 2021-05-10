# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 14:04:31
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 14:45:03

class Solution:

    # 90 mem 100
    # 把大数往nums1的末尾移动
    def merge(self, nums1, m, nums2, n):
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        nums1[:n] = nums2[:n]
        return nums1

if __name__ == '__main__':
    l1 = [1,2,3,0,0,0]
    l2 = [2,5,6]
    s = Solution()
    r = s.merge(l1,3,l2,3)
    print(r)
