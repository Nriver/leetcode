# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-03 10:44:39
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-03 11:25:14

from common_class import ListNode

class Solution:


    # Runtime: 28 ms, faster than 83.77% of Python3 online submissions for Remove Nth Node From End of List.
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        res = head
        nodes = []
        while True:
            nodes.append(head)
            if not head.next:
                break
            head = head.next
        if n==1:
            # 去掉最后一个
            nodes[-2].next = None
        elif len(nodes) == n:
            # 去掉第一个
            res = nodes[1]
        else:
            # 去掉中间的
            nodes[-n-1].next = nodes[-n+1]

        # head = res
        # while True:
        #     print(head.val)
        #     if not head.next:
        #         break
        #     head = head.next

        return res

if __name__ == '__main__':
    s = Solution()

    # test_case = [1,2,3,4,5]
    # l1 = ListNode(0)
    # l1_start_cursor = l1
    # for x in test_case:
    #     l1.next = ListNode(x)
    #     l1 = l1.next
    # s.removeNthFromEnd(l1_start_cursor.next, 2)

    test_case = [1,2]
    l1 = ListNode(0)
    l1_start_cursor = l1
    for x in test_case:
        l1.next = ListNode(x)
        l1 = l1.next
    s.removeNthFromEnd(l1_start_cursor.next, 1)

    test_case = [1,2]
    l1 = ListNode(0)
    l1_start_cursor = l1
    for x in test_case:
        l1.next = ListNode(x)
        l1 = l1.next
    s.removeNthFromEnd(l1_start_cursor.next, 2)