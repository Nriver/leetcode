# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 17:04:13
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-22 09:06:50

class Solution:
    # 注意sub array是指连续的某几个数

    # 太慢
    def numOfSubarrays1(self, arr):
        res = 0
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)+1):
                if sum(arr[i:j]) % 2 == 1:
                    res += 1
        return res

    def numOfSubarrays1(self, arr):


s = Solution()
# print(s.numOfSubarrays([1, 3, 5]))
# print(s.numOfSubarrays([2, 4, 6]))
# print(s.numOfSubarrays([1,2,3,4,5,6,7]))
print(s.numOfSubarrays([26,42,38,88,85,25,7,33,22,63,31,29,85,51,86,76,67,45,46,61,87,49,58,23,69,37,34,71,17,82,91,33,75,9,69,60,34,95,73,80,92,12,95,35,1,71,53,32,10,36,51,20,86,46,10,88,54,80,18,55,36,46,13,4,81,100,68,15,27,49,72,47,20,94,30,46,46,2,72,12,88,72,72,62,6,12,80,96,56,54,49,6,23,34,55,65,75,12,83,12,47,46,9,38,41,40,76,100,36,7,2,23,41,66,89,95,24,20,41,26,73,26,91,15,35,68,96,85,67,39,68,6,59,49,87,13,31,50,97,62,47,37,7,27,20,83,7,71,1,12,12,6,54,26,19,99,53,16,29,36,36,81,92,49,10,43,16,29,4,75,37,52,54,36,76,84,15,91,96,50,15,25,42,42,65,16,89,7,9,70,27,36,50,15,81,30,12,88,46,54,22,13,58,5,1,40,14,73,60,56,96,89,75,29,26,70,22,79,10,97,86,45,99,19,94,49,55,12,19,33,69,91,16,1,91,48,73,29,71,11,91,74,46,32,62,28,22,23,10,91,74,81,17,90,11,61,40,16,5,49,10,8,22,26,95,26,72,3,87,19,78,63,43,86,81,56,74,16,75,78,73,59,3,73,32,36,69,17,86,14,48,74,47,83,6,79,21,38,26,69,23,74,53,43,61,99,100,24,30,87,19,88,61,95,23,77,39,20,12,37,64,25,99,98,63,52,56,39,3,9,49,80,93,83,95,66,98,94,79,49,53,27,44,8,60,38,87,3,32,64,94,74,12,40,57,72,18,25,93,45,10,72,38,25,87,58,76,79,60,59,6,91,18,23,47,18,61,51,41,53,69,100,82,39,19,28,32,33,81,78,37,85,40,66,59,40,22,68,36,11,61,28,12,33,35,12,29,13,76,36,9,21,3,14,37,4,26,50,80,58,13,1,41,99,95,7,39,37,16,22,1,28,90,18,82,21,2,44,53,12,24,51,34,56,80,93,79,32,92,52,46,5,76,88,66,11,92,30,46,79,3,93,97,75,16,71,33,86,52,36,76,25,52,29,61,43,81,27,35,68,49,55,79,46,70,21,25,37,51,50,47,58,36,20,72,72,92,89,98,51,100,65,83,93,22,44,36,26,5,35,87,69,72,39,54,57,41,97,32,50,92,54,88,56,76,98,47,65,42,13,87,18,23,79,15,17,20,77,53,75,7,52,89,100,4,77,34,30,40,51,33,67,76,18,24,18,36,67,1,18,87,12,33,1,95,76,80,7,18,92,45,52,60,36,46,5,100,56,90,47,69,76,96,97,76,64,27,44,78,11,91,93,51,24,74,49,49,86,70,88,34,53,40,37,76,94,4,28,73,66,54,90,41,43,21,72,69,11,41,24,96,95,87,12,3,100,12,18,44,8,2,71,20,74,31,46,84,92,25,92,98,4,10,4,43,72,100,31,69,29,36,70,56,92,13,85,94,79,98,8,87,50,31,30,92,23,36,64,35,48,18,83,29,58,45,20,20,84,38,18,65,44,96,100,73,36,86,56,58,45,95,26,30,34,78,15,32,27,46,48,94,21,59,53,73,27,11,51,76,4,61,99,61,88,88,31,85,25,7,17,4,78,66,20,48,12,97,51,82,6,61,69,97,47,18,89,2,31,76,69,87,5,26,97,9,58,21,4,25,96,54,93,8,2,38,18,38,44,48,46,77,50]))