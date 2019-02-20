# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-12-19 10:46:12
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-20 17:00:12


class Solution:

    # 100% 递归最快
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        # 注意最开始启动递归的时候传的最大和最小值都要是None
        return self.isValid(root, None, None)

    def isValid(self, root, min, max):
        if (root == None):
            return True
        if (min != None and root.val <= min):
            return False
        if (max != None and root.val >= max):
            return False
        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)

    # 58% solution
    # 中序遍历 慢
    # def isValidBST(self, root: 'TreeNode') -> 'bool':
    #     ret = self.inorder(root)
    #     return ret == sorted(list(set(ret)))

    # def inorder(self, root):
    #     if root is None:
    #         return []
    #     return self.inorder(root.left) + [root.val] + self.inorder(root.right)


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
    if string == '{}':
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


test_cases = (deserialize('[2, 1, 3]'),
              deserialize('[5, 1, 4, null, null, 3, 6]'),
              )

solution = Solution()

for test_case in test_cases:
    print(solution.isValidBST(test_case))
