# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-03 15:08:05
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-04 14:00:25

import sys

class Solution:

    # Runtime: 1708 ms, faster than 5.01% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Memory Usage: 18.5 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    def kthSmallest1(self, matrix, k: int) -> int:
        l = len(matrix)
        if k==1:
            return matrix[0][0]
        elif k==l*l:
            return matrix[l-1][l-1]
            
        i_list = [0] * l
        while k>0:
            # print(i_list)
            # 还有这个慢了
            tmp_list = [matrix[index][x] for index,x in enumerate(i_list)]
            if k==1:
                return min(tmp_list)
            small_i = tmp_list.index(min(tmp_list))
            if i_list[small_i] == l-1:
                # 应该是这里慢了
                i_list.pop(small_i)
                matrix.pop(small_i)
            else:
                i_list[small_i] += 1
            k -= 1


    # 比上面快了一些，记录下比较的数字，不过还是很慢
    # Runtime: 496 ms, faster than 5.01% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Memory Usage: 18.7 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    def kthSmallest2(self, matrix, k: int) -> int:
        l = len(matrix)
        if k==1:
            return matrix[0][0]
        elif k==l*l:
            return matrix[l-1][l-1]
            
        i_list = [0] * l
        cache_list = [matrix[index][0] for index in range(l)]
        while k>0:
            # print(cache_list)
            min_num = min(cache_list)
            # print('最小数', min_num)
            pos = cache_list.index(min_num)
            
            if i_list[pos] == l-1:
                
                # 两种方法时间差不多
                # 方法1
                # i_list[pos] += 1
                # cache_list[pos] = sys.maxsize
                # 方法2
                i_list.pop(pos)
                matrix.pop(pos)
                cache_list.pop(pos)

            else:
                i_list[pos] += 1
                cache_list[pos] = matrix[pos][i_list[pos]]
            k -= 1
            if k==0:
                return min_num

    # 利用sort的无脑方法 一行搞定
    # Runtime: 180 ms, faster than 83.31% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Memory Usage: 18.8 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Runtime: 184 ms, faster than 77.69% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Memory Usage: 18.8 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    def kthSmallest3(self, matrix, k: int) -> int:
        return sorted([y for x in matrix for y in x])[k-1]

    # 也不是特别快
    # Runtime: 216 ms, faster than 55.49% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Memory Usage: 18.8 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    def kthSmallest(self, matrix, k: int) -> int:
        # 用python3的heapq
        import heapq
        h = []
        for line in matrix:
            for x in line:
                heapq.heappush(h, x)

        while k>1:
            heapq.heappop(h)
            k-=1
        return heapq.heappop(h)




if __name__ == '__main__':
    s = Solution()
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ]
    k = 8
    print(s.kthSmallest(matrix, k))

    matrix = [
       [-5],
    ]
    k = 1
    print(s.kthSmallest(matrix, k))