# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-03 11:49:21
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-03 14:17:29

class Solution:

    # Runtime: 28 ms, faster than 99.07% of Python3 online submissions for Pancake Sorting.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pancake Sorting.
    # Runtime: 36 ms, faster than 89.88% of Python3 online submissions for Pancake Sorting.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pancake Sorting.
    # def pancakeSort(self, A: List[int]) -> List[int]:
    def pancakeSort(self, A):
        if not A:
            return []
        target = sorted(A)
        res = []
        loop_count = len(A)
        # print(A)
        for x in range(loop_count, 0, -1):
            # print('整理数字', x)
            pos = A.index(x)
            if (x == pos+1):
                # 说明正好在正确的位置上不需要修改了
                continue
            if pos != 0:
                A[:pos+1] = A[pos::-1]
                # print(A)
                res.append(pos+1)

            A[:x] = A[x-1::-1]
            # print(A)
            res.append(x)

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.pancakeSort([3,2,4,1]))
    print(s.pancakeSort([3,2,1,4]))