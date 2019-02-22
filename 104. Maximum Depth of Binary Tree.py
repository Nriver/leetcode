# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 11:14:01
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-22 19:28:22

import collections


class Solution:

    # 100% 内存 91%
    # 广度优先 层层遍历

    def maxDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        max_level = 0
        queue = collections.deque()
        queue.append(root)

        while queue:

            size = len(queue)
            max_level += 1
            for x in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_level

    # 99% mem 67%
    # 分治的方法 可以看成是深度优先的优化
    def maxDepth3(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        return 1 + max(self.maxDepth3(root.left), self.maxDepth3(root.right))

    # 99% 内存12%
    # 深度优先
    def maxDepth2(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        self.max_level = 0
        self._dfs(root, 1)
        return self.max_level

    def _dfs(self, node, level):
        if not node:
            return
        if node.left:
            self._dfs(node.left, level + 1)
        if node.right:
            self._dfs(node.right, level + 1)
        if not node.left and not node.right:
            self.max_level = max(self.max_level, level)

# Tree definition found in here
# https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


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
              )

solution = Solution()

for test_case in test_cases:
    print(solution.maxDepth(test_case))
