# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-02 16:28:09
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-02 16:55:50
class Solution:

    # 时间会变动
    # Runtime: 40 ms, faster than 92.32% of Python3 online submissions for Integer to Roman.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Integer to Roman.
    # Runtime: 44 ms, faster than 82.73% of Python3 online submissions for Integer to Roman.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Integer to Roman.
    def intToRoman(self, num: int) -> str:
        r_dict = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M',
        }

        # 分解数字
        rs = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        q_list = []
        res = ''
        for index, r in enumerate(rs):
            q = num // r
            q_list.append(q)
            if q > 0:
                num = num - q * r
                res += q_list[index] * r_dict[r]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
    print(s.intToRoman(3999))
