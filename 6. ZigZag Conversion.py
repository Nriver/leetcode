# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-02-21 11:12:49
# @Last Modified by:   zengjq
# @Last Modified time: 2020-02-25 10:01:38

class Solution:

    # 很慢的算法
    # Runtime: 3276 ms, faster than 5.00% of Python3 online submissions for ZigZag Conversion.
    # Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.
    def convert1(self, s: str, numRows: int) -> str:
        # numRows = 3

        result = []
        for x in range(numRows):
            result.append([])
        len_s = len(s)
        if numRows == 1:
            return s
        # 尝试推算一行一行公式结果发现太复杂，还是简单粗暴的遍历就行

        # 0   |4   |8     |12
        # 1 3 |5 7 |9  11 |13
        # 2   |6   |10    |14

        # 0     |6       |12       |18
        # 1   5 |7    11 |13    17 |
        # 2 4   |8 10    |14 16    |
        # 3     |9       |15       |

        for x in range(len_s):
            for remainder in range(numRows):
                # 一个循环的数
                slot_count = 2*numRows - 2
                if x % slot_count == remainder or x % slot_count == (slot_count - remainder):
                    result[remainder].append(x)

        print(result)

        result_str = ''
        for line in result:
            for x in line:
                result_str += s[x]

        return result_str

    # 优化 比之前快了一些
    # Runtime: 72 ms, faster than 33.85% of Python3 online submissions for ZigZag Conversion.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.
    def convert2(self, s: str, numRows: int) -> str:

        result = []
        for x in range(numRows):
            result.append([])
        len_s = len(s)
        if numRows == 1:
            return s

        slot_count = 2*numRows - 2
        for x in range(len_s):
            # 一个循环的数
            remainder = x % slot_count
            if remainder>=numRows:
                remainder = slot_count - remainder
            result[remainder].append(x)

        print(result)

        result_str = ''
        for line in result:
            for x in line:
                result_str += s[x]

        return result_str

    # 再优化 把(numRows*2-2)循环 改成触碰边界反向
    # Runtime: 44 ms, faster than 98.42% of Python3 online submissions for ZigZag Conversion.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [''] * numRows
        len_s = len(s)

        row = 0
        step = 1

        for x in s:
            res[row] += x

            # 这里是关键 之前想复杂了，其实只要在边界判断就行，用不着判断范围内的值
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.convert('A', 1))
    print(s.convert('PAYPALISHIRING', 3))
    print(s.convert('PAYPALISHIRING', 4))
    print(s.convert('PAYPALISHIRING', 5))

    # [[0, 4, 8, 12], [1, 3, 5, 7, 9, 11, 13], [2, 6, 10]]
    # PAHNAPLSIIGYIR
    # [[0, 6, 12], [1, 5, 7, 11, 13], [2, 4, 8, 10], [3, 9]]
    # PINALSIGYAHRPI
    # [[0, 8], [1, 7, 9], [2, 6, 10], [3, 5, 11, 13], [4, 12]]
    # PHASIYIRPLIGAN