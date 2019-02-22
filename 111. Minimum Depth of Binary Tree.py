# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 11:14:01
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-22 19:35:20

import collections


class Solution:
    #
    # 广度优先 层层遍历

    # 100% mem 66%
    def minDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        min_level = 0
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            min_level += 1
            for x in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return min_level

    # 99% mem 23%
    # 分治 可以看作深度优先的优化
    def minDepth2(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth2(root.right)
        if not root.right:
            return 1 + self.minDepth2(root.left)
        return 1 + min(self.minDepth2(root.left), self.minDepth2(root.right))

    # 93% mem 14%
    # 深度优先
    def minDepth3(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        self.min_level = None
        self._dfs(root, 1)
        return self.min_level

    def _dfs(self, node, level):
        if not node:
            return
        if node.left:
            self._dfs(node.left, level + 1)
        if node.right:
            self._dfs(node.right, level + 1)
        if not node.left and not node.right:
            if not self.min_level:
                self.min_level = level
            else:
                self.min_level = min(self.min_level, level)

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
    print(solution.minDepth(test_case))
