# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 11:07:45
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-20 13:17:22


# counter.get(x,1)的执行效率会比
# if x not in counter:
#   return 1
# else:
#   return counter[x]
# 要低
# 每写一个get(x,0) 这个结果就慢4ms

class Solution:

    # 81%
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        if len(s) != len(t):
            return False
        counter = {}
        for x in s:
            if x not in counter:
                counter[x] = 1
            else:
                counter[x] += 1

        for x in t:
            if x in counter and counter[x] != 0:
                counter[x] = counter[x] - 1
            else:
                return False

        return True

test_cases = (("anagram", "nagaram"), ("rat", "car"), ("ab", "a"), ("a", "ab"), ("aa", "a"))

solution = Solution()

for test_case in test_cases:
    print(solution.isAnagram(test_case[0], test_case[1]))
