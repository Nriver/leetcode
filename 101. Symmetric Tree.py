# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 15:10:26
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 15:21:09
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

    # 93 mem 100
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        p = root.left
        q = root.right
        return self.helper(p, q)

    def helper(self, p, q):
        if p and q:
            return (p.val == q.val) and self.helper(p.left, q.right) and self.helper(p.right, q.left)
        return p is None and q is None


s = Solution()

print(s.isSymmetric(deserialize('[1,2,3]')))
print(s.isSymmetric(deserialize('[1,2,2,3,4,4,3]')))
print(s.isSymmetric(deserialize('[]')))