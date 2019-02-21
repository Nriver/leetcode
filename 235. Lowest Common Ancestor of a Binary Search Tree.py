# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2019-02-21 10:16:00
# @Last Modified by:   Zengjq
# @Last Modified time: 2019-02-21 10:50:29

# 99%
# 教程 https://time.geekbang.org/course/detail/130-42708


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 使用递归内存消耗大
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 不使用递归 内存消耗很小 跟递归的执行效率差不多
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
