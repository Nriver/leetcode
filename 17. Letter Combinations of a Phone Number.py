# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-03 09:57:34
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-03 10:28:53

class Solution:

    # 一个字一个字的拼接
    # Runtime: 24 ms, faster than 88.15% of Python3 online submissions for Letter Combinations of a Phone Number.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
    # def letterCombinations(self, digits: str) -> List[str]:
    def letterCombinations(self, digits: str):
        if not digits:
            return digits
        res = []
        n_dict = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        res = n_dict[digits[0]]
        print(res)
        i = 1
        while(i < len(digits)):
            tmp = []
            for x in res:
                for y in n_dict[digits[i]]:
                    tmp.append(x+y)
            res = tmp
            i += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("233"))