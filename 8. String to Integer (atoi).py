# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-02-21 10:39:57
# @Last Modified by:   zengjq
# @Last Modified time: 2020-02-21 11:08:25

class Solution:

    # Runtime: 28 ms, faster than 89.35% of Python3 online submissions for String to Integer (atoi).
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for String to Integer (atoi).
    def myAtoi(self, str: str) -> int:

        valid = {
            '+': 1,
            '-': 1,
            '0': 1,
            '1': 1,
            '2': 1,
            '3': 1,
            '4': 1,
            '5': 1,
            '6': 1,
            '7': 1,
            '8': 1,
            '9': 1,
        }
        r = '0'
        str = str.strip()
        negative = False
        for index, s in enumerate(str):
            if not valid.get(s):
                break
            if index == 0:
                if s == '+':
                    negative = False
                elif s == '-':
                    negative = True
                else:
                    r = s
            elif index > 0 and s in ['+','-']:
                break
            else:
                r += s

        r = int(r)
        if negative:
            r = -r

        if r>2147483647:
            return 2147483647
        if r<-2147483648:
            return -2147483648
        return r

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('42'))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("+-2"))
