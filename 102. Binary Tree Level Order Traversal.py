# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 11:14:01
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-22 17:58:31

import collections


class Solution:
    # 速度 100% 内存 87%
    # 广度优先 不记录层数 并且使用deque

    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        res = []
        queue = collections.deque()

        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []

            for x in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current_level)
        return res

    # 97%
    # BFS breadth first search
    # 广度优先 记录层数
    def levelOrder2(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        queue = []
        if root == None:
            return []
        queue.append([root, 0])
        while queue:
            node, level = queue.pop(0)
            if len(res) == level:
                res.append([node.val, ])
            elif res[level]:
                res[level].append(node.val)
            else:
                res[level] = [node.val, ]
            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])
        return res


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
              )

solution = Solution()

for test_case in test_cases:
    print(solution.levelOrder(test_case))
