# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 14:50:13
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 15:08:25
# Definition for a binary tree node.
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

class Solution:
    # 80 mem 99
    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if (p is None) ^ (q is None):
            return False
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 80 mem 99
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is None and q is None

s = Solution()


print(s.isSameTree(deserialize('[1,2,3]'), deserialize('[1,3,2]')))