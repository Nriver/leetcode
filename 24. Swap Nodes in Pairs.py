# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-04 15:06:47
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-04 17:51:06

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # 遍历解法 很慢
    # Runtime: 224 ms, faster than 5.51% of Python3 online submissions for Swap Nodes in Pairs.
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
    def swapPairs1(self, head: ListNode) -> ListNode:
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        if not head or not head.next:
            return head

        # 末尾加几个空的值来处理最后两个数
        loop_count = len(nodes)
        nodes = nodes + [None, None, None]

        print(nodes)
        for i in range(loop_count):
            if i % 2==0:
                if nodes[i+3] is None:
                    nodes[i].next = nodes[i+2]
                else:
                    nodes[i].next = nodes[i+3]
            else:
                nodes[i].next = nodes[i-1]
        return nodes[1]

    # 取出所有node再交换位置
    # Runtime: 28 ms, faster than 72.80% of Python3 online submissions for Swap Nodes in Pairs.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        # 有了nodes直接换位置就行了
        # 交换次数是长度的一半取整
        swap_count = len(nodes) // 2
        for x in range(swap_count):
            nodes[2*x], nodes[2*x+1] = nodes[2*x+1], nodes[2*x]
        for x in range(len(nodes)-1):
            nodes[x].next = nodes[x+1]
        # 最后一个没有下一个了
        nodes[-1].next = None
        return nodes[0]

    # 比较直观的解法
    # 时间变化较大 20-32ms
    # Runtime: 20 ms, faster than 97.80% of Python3 online submissions for Swap Nodes in Pairs.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
    def swapPairs3(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nodes = []
        p = head
        new_head = p.next

        while True:
            # 原始顺序 p p1 p2 p3
            p1 = p.next
            if p1 is None:
                # print('p1 none')
                break
            p2 = p1.next
            if p2 is None:
                # print('p2 none')
                # p p1 None
                # 对应 [1, 2]
                # 转换成
                # p1 p None
                p1.next = p
                p.next = None
                break
            p3 = p2.next
            if p3 is None:
                # print('p3 none')
                # p p1 p2 None
                # 对应 [1, 2, 3]
                # 转换成
                # p1 p p2 None
                p1.next = p
                p.next = p2
                p2.next = None
                break

            # 变成 p1 p p3 p2
            p1.next = p
            p.next = p3

            # 下一个循环
            p = p2
        return new_head


    # 一个参考答案
    # https://leetcode.com/problems/swap-nodes-in-pairs/discuss/486804/Python-Simple-Solution-Memory-usage-less-than-100
    # 和上面我写的解法类似, 不过更简洁
    # 它加了一个空的node, 使得起点提前了一个, 每次只需要换中间两个, 这个过程更简洁
    # 由于重点只交换p和p1
    # 所以只要prev, p, p1有效就行, p2是None都没问题
    # prev p p1 p2
    # prev p1 p p2
    # Runtime: 24 ms, faster than 91.57% of Python3 online submissions for Swap Nodes in Pairs.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev and prev.next and prev.next.next:
            p = prev.next
            p1 = p.next
            p2 = p1.next
            # 交换
            prev.next = p1
            p1.next = p
            p.next = p2
            # 准备下一个循环
            # 注意这里不要写成了prev = p2
            # 这个算法是每次移动两个位置
            prev = p

        return dummy.next



if __name__ == '__main__':
    s = Solution()
    # test_cases = ([1, 2, 3, 4, 5], [1,2,4], [1,3,4])
    test_cases = ([1, 2, 3, 4, 5, 6],)
    # test_cases = ([1, 2],)
    # test_cases = ([1, 2, 3],)
    for test_case in test_cases:
        l1 = ListNode(0)
        head = l1
        for x in test_case:
            l1.next = ListNode(x)
            l1 = l1.next
        res = s.swapPairs(head.next)
        while(res):
            print(res.val)
            res = res.next