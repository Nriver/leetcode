# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 11:14:01
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-22 22:00:42


class Solution:
    # 100% mem 29%

    def generateParenthesis(self, n: 'int') -> 'List[str]':
        self.results = []
        self.gen(n, 0, 0, "")
        return self.results

    def gen(self, n, l, r, res):
        if l == n and r == n:
            self.results.append(res)
        if l < n:
            self.gen(n, l + 1, r, res + '(')
        if r < n and r < l:
            self.gen(n, l, r + 1, res + ')')

test_cases = (1,
              2,
              3,
              )

solution = Solution()

for test_case in test_cases:
    print(solution.generateParenthesis(test_case))
