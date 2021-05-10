# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-05-22 09:27:18
# @Last Modified by:   zengjq
# @Last Modified time: 2020-05-22 09:59:05
# https://leetcode.com/problems/reverse-nodes-in-k-group/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # Runtime: 88 ms, faster than 8.36% of Python3 online submissions for Reverse Nodes in k-Group.
    # Memory Usage: 14.9 MB, less than 5.88% of Python3 online submissions for Reverse Nodes in k-Group.
    def reverseKGroup(self, head, k):
        if not head:
            return
        tmp_list = []
        res_list = []
        res = ListNode(None)
        tmp = res
        
        while(head):
            for x in range(k):
                reverse_flag = True
                if not head:
                    reverse_flag = False
                    break
                tmp_list.append(head)
                head = head.next
            if reverse_flag:
                for x in reversed(tmp_list):
                    res_list.append(x)
            else:
                for x in tmp_list:
                    res_list.append(x)
            tmp_list = []
        print(len(res_list))
        for x in res_list:
            tmp.next = x
            tmp = tmp.next
        tmp.next = None
        return res.next



if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(6)
    l1.next.next.next.next.next.next = ListNode(7)
    
    s = Solution()
    r = s.reverseKGroup(l1, 3)
    print(r)
    while(r):
        print(r.val)
        r = r.next