# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 13:48:07
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 14:02:40

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # 94 mem 100
    def deleteDuplicates1(self, head):
        if not head:
            return
        h = c = prev = head
        while c.next:
            c = c.next
            if prev.val == c.val:
                prev.next = c.next
            else:
                prev = c
        return h

    # 58 mem 100
    def deleteDuplicates(self, head):
        if not head:
            return
        c = head
        while c.next:
            if c.val == c.next.val:
                c.next = c.next.next
            else:
                c = c.next
        return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(3)

    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(1)
    s = Solution()
    r = s.deleteDuplicates(l1)
    print(r)
    while(r):
        print(r.val)
        r = r.next
