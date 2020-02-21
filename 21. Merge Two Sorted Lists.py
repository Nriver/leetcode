# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-02-21 09:10:27
# @Last Modified by:   zengjq
# @Last Modified time: 2020-02-21 10:16:50

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # 这个解法比较慢但是省内存
    # Runtime: 40 ms, faster than 25.62% of Python3 online submissions for Merge Two Sorted Lists.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Input: 1->2->4, 1->3->4
        # Output: 1->1->2->3->4->4
        
        # 边界值判断
        if not l1:
            return l2
        if not l2:
            return l1
        
        # 初始化
        if l1.val < l2.val:
            r = ListNode(l1.val)
            l1 = l1.next
        else:
            r = ListNode(l2.val)
            l2 = l2.next

        # 比较
        r_tmp = r
        while (l1 and l2):
            if l1.val < l2.val:
                r_tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                r_tmp.next = ListNode(l2.val)
                l2 = l2.next
            r_tmp = r_tmp.next

        # 处理剩余数字
        while (l1):
            r_tmp.next = ListNode(l1.val)
            l1 = l1.next
            r_tmp = r_tmp.next
        while (l2):
            r_tmp.next = ListNode(l2.val)
            l2 = l2.next
            r_tmp = r_tmp.next

        return r

    # 优化上面的算法
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Input: 1->2->4, 1->3->4
        # Output: 1->1->2->3->4->4
        
        # 比较
        # 这里的优化 初始化一个空的节点, 不用自己判断l1和l2
        # 最后返回这个空节点的下一个值就行
        r_tmp = r = ListNode(None)
        while (l1 and l2):
            if l1.val < l2.val:
                r_tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                r_tmp.next = ListNode(l2.val)
                l2 = l2.next
            r_tmp = r_tmp.next

        # 处理剩余数字
        # 这里的优化 剩余数字直接把l1或者l2剩下的设为next就行, 用不着遍历
        r_tmp.next = l1 or l2

        return r.next


if __name__ == '__main__':
    # [1,2,4]
    # [1,3,4]
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()
    r = s.mergeTwoLists(l1, l2)
    print(r)
    while(r):
        print(r.val)
        r = r.next

    # [-9,3]
    # [5,7]
    l1 = ListNode(-9)
    l1.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(7)
    s = Solution()
    r = s.mergeTwoLists(l1, l2)
    print(r)
    while(r):
        print(r.val)
        r = r.next

