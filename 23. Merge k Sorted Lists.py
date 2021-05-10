# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-05-21 13:35:29
# @Last Modified by:   zengjq
# @Last Modified time: 2020-05-22 09:26:43

# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # Runtime: 7696 ms, faster than 5.00% of Python3 online submissions for Merge k Sorted Lists.
    # Memory Usage: 17.2 MB, less than 24.24% of Python3 online submissions for Merge k Sorted Lists.
    def mergeKLists1(self, lists):
        if not lists:
            return None
        head = ListNode(None)
        res = head
        min_index = 0
        new_list = []
        pop_list = []
        for i,x in enumerate(lists):
            if not x:
                pop_list.append(i)
        for x in reversed(pop_list):
            lists.pop(x)
        while(lists):
            for i,x in enumerate(lists):
                if x.val < lists[min_index].val:
                    min_index = i
            head.next = ListNode(lists[min_index].val)
            head = head.next
            lists[min_index] = lists[min_index].next
            if lists[min_index] == None:
                lists.pop(min_index)
                min_index = 0
        return res.next


    # 参考https://leetcode.com/problems/merge-k-sorted-lists/discuss/560894/Python-3-simple-solution-using-array-beats-97
    # 这个算法先把所有的数取出来在list里面排序再生成结果
    # Runtime: 88 ms, faster than 99.29% of Python3 online submissions for Merge k Sorted Lists.
    # Memory Usage: 18.1 MB, less than 7.57% of Python3 online submissions for Merge k Sorted Lists.
    def mergeKLists(self, lists):
        if not lists:
            return None
        nums = []
        for x in lists:
            while(x):
                nums.append(x.val)
                x = x.next
        nums.sort()
        head = ListNode(None)
        tmp = head
        for x in nums:
            tmp.next = ListNode(x)
            tmp = tmp.next
        return head.next

if __name__ == '__main__':
    # [1,2,4]
    # [1,3,4]
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    s = Solution()
    r = s.mergeKLists([l1, l2, l3])
    print(r)
    while(r):
        print(r.val)
        r = r.next
        