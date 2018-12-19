# -*- coding: utf-8 -*-
# @Author: Zengjq
# @Date:   2018-12-19 12:43:08
# @Last Modified by:   Zengjq
# @Last Modified time: 2018-12-19 12:43:16

# Definition for singly-linked list.


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_node = ListNode(0)
        start_cursor = sum_node
        carry = 0
        last_carry = 0
        digit_sum = 0
        while(True):
            if l1 is None:
                l1_digit = 0
            else:
                l1_digit = l1.val
                l1 = l1.next

            if l2 is None:
                l2_digit = 0
            else:
                l2_digit = l2.val
                l2 = l2.next

            carry, digit_sum = divmod(l1_digit + l2_digit + last_carry, 10)
            sum_node.next = ListNode(digit_sum)
            sum_node = sum_node.next
            last_carry = carry
            if l1 is None and l2 is None and carry == 0:
                break
        return start_cursor.next

test_cases = ([2, 4, 3], [5, 6, 4]), ([5], [5]), ([1], [9, 9])

for index, test_case in enumerate(test_cases):
    print('test_case', index)
    l1 = ListNode(0)
    l1_start_cursor = l1
    for x in test_case[0]:
        l1.next = ListNode(x)
        l1 = l1.next

    l2 = ListNode(0)
    l2_start_cursor = l2
    for x in test_case[1]:
        l2.next = ListNode(x)
        l2 = l2.next

    solution = Solution()
    ret = solution.addTwoNumbers(l1_start_cursor, l2_start_cursor)
    while(True):
        if ret.next is None:
            break
        ret = ret.next
        print(ret.val)
