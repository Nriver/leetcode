# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 10:16:00
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-21 10:40:43

# 93%
# 教程 https://time.geekbang.org/course/detail/130-42708


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root == None or root == p or root == q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left == None:
            return right
        if right == None:
            return left
        if left != None and right != None:
            return root
