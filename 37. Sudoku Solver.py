# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-20 17:07:27
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-23 01:28:25

# 检验数独是否有效
# 注意 有效的数独不一定是有解
# 教程 https://time.geekbang.org/course/detail/130-67639


class Solution:

    # 5%
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        print(board)

    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        rows = [set([]) for _ in range(9)]
        cols = [set([]) for _ in range(9)]
        nines = [[set([]) for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                s = board[row][col]
                if s != '.':
                    if s in rows[col] or s in cols[row] or s in nines[row // 3][col // 3]:
                        return False
                    rows[col].add(s)
                    cols[row].add(s)
                    nines[row // 3][col // 3].add(s)
        return True

    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for s in range(1, 10):
                        board[row][col] = str(s)
                        if self.isValidSudoku(board):
                            if(self.solve(board)):
                                return True
                        board[row][col] = '.'
                    return False
        return True

test_cases = (
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ],
)

solution = Solution()

for test_case in test_cases:
    print(solution.solveSudoku(test_case))
