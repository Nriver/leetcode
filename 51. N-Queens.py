# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 11:14:01
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-23 00:12:31

# 教程 https://time.geekbang.org/course/detail/130-67638


class Solution:

    # 99% mem 35%
    # 这个解 真牛
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        results = []

        def DFS(queens, xy_sum, xy_diff):
            y = len(queens)
            if y == n:
                results.append(queens)
                return None
            for x in range(n):
                if x not in queens and x + y not in xy_sum and x - y not in xy_diff:
                    DFS(queens + [x], xy_sum + [x + y], xy_diff + [x - y])
        DFS([], [], [])
        return [['.' * x + 'Q' + '.' * (n - x - 1) for x in result] for result in results]

    # 75% mem 29%
    # 自己写的
    def solveNQueens2(self, n: 'int') -> 'List[List[str]]':
        self.results = []
        self.n = n
        self.solve([], [], 0)
        return self.results

    def solve(self, cols, queens, current_line):
        for x in range(self.n):
            # 终止条件 结束查找
            if len(queens) == self.n:
                result = ['.' * self.n] * self.n
                for x, y in queens:
                    result[y] = result[y][: x] + 'Q' + result[y][x + 1:]
                self.results.append(result)
                return

            if x in cols:
                continue
            is_valid = True
            for y, z in queens:
                if (y + z == x + current_line) or (y - x == z - current_line):
                    is_valid = False
                    break
            if is_valid:
                self.solve(cols + [x, ], queens + [[x, current_line], ], current_line + 1)


test_cases = (
    4,
)

solution = Solution()

for test_case in test_cases:
    print(solution.solveNQueens(test_case))
