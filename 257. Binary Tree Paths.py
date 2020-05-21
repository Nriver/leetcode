# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-05-20 09:58:33
# @Last Modified by:   zengjq
# @Last Modified time: 2020-05-21 10:43:27

# https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
class Solution:

    # Runtime: 48 ms, faster than 7.78% of Python3 online submissions for Binary Tree Paths.
    # Memory Usage: 13.8 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
    def binaryTreePaths1(self, root):
        if not root:
            return []
        head = root
        paths = []
        def helper(node, path):
            if node == None:
                return
            elif node.left == None and node.right == None:
                path = path + str(node.val)
                paths.append(path)
            helper(node.left, path + str(node.val) + '->')
            helper(node.right, path + str(node.val) + '->')
        helper(root, '')
        return paths

    # Runtime: 36 ms, faster than 34.73% of Python3 online submissions for Binary Tree Paths.
    # Memory Usage: 13.8 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
    def binaryTreePaths2(self, root):
        if not root:
            return []
        paths = []
        def helper(node, path):
            if node.left:
                helper(node.left, path + str(node.val) + '->')
            if node.right:
                helper(node.right, path + str(node.val) + '->')
            if not node.left and not node.right:
                path = path + str(node.val)
                paths.append(path)
                return
        helper(root, '')
        return paths

    # Runtime: 56 ms, faster than 6.33% of Python3 online submissions for Binary Tree Paths.
    # Memory Usage: 14 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
    def binaryTreePaths3(self, root):
        # 这个解法很简洁
        if not root:
            return []
        result = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        result += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        return result or [str(root.val)]

    # Runtime: 28 ms, faster than 87.58% of Python3 online submissions for Binary Tree Paths.
    # Memory Usage: 13.8 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
    # Runtime: 44 ms, faster than 9.66% of Python3 online submissions for Binary Tree Paths.
    # Memory Usage: 14 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
    # 这个在binaryTreePaths2的基础上做了一点点改动
    # 把重复的字符串拼接给提前拼好 避免重复拼接
    # 把有return的if判断提前也有一点点作用
    def binaryTreePaths(self, root):
        if not root:
            return []
        paths = []
        def helper(node, path):
            if not node.left and not node.right:
                path = path + str(node.val)
                paths.append(path)
                return
            # 提前拼接 减少运算次数
            path = path + str(node.val) + '->'
            if node.left:
                helper(node.left, path)
            if node.right:
                helper(node.right, path)
        helper(root, '')
        return paths


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(string):
    if string == '[]':
        return None
    nodes = [None if val.strip() == 'null' else TreeNode(int(val.strip()))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


test_cases = (deserialize('[3,9,20,null,null,15,7]'),
              deserialize('[]'),
              deserialize('[1, null, 2]'),
              deserialize('[3,9,20,null,null,15,7]'),
              deserialize('[1,2,3,null,5]'),
              )

solution = Solution()

for test_case in test_cases:
    print(solution.binaryTreePaths(test_case))
