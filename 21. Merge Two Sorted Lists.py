# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-02-21 09:10:27
# @Last Modified by:   zengjq
# @Last Modified time: 2020-02-21 10:02:21

# 这个解法比较慢但是省内存
# Runtime: 40 ms, faster than 25.62% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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

