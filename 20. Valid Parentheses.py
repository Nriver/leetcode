# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-02-25 10:03:45
# @Last Modified by:   zengjq
# @Last Modified time: 2020-02-25 10:52:06
class Solution:

    # 压栈 先进先出
    # Runtime: 28 ms, faster than 71.92% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
    def isValid(self, s: str) -> bool:
        p_list = []
        for x in s:
            if x == '(':
                p_list.append(')')
            elif x == '[':
                p_list.append(']')
            elif x == '{':
                p_list.append('}')
            elif not p_list:
                # 循环过程中栈空了 说明结束的括号多了
                return False
            elif x in [')',']','}'] and x != p_list.pop():
                # 括号类型不匹配 说明是错误的格式
                return False
        # 循环结束栈没空 说明开始的括号多了 没有全部闭合
        if p_list:
            return False
        return True

    # 用list和dict代替精简代码
    # Runtime: 28 ms, faster than 71.92% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
    def isValid2(self, s: str) -> bool:
        p_stack = []
        p_dict = {'(':')','[':']','{':'}'}
        p_open = ['(','[','{']
        p_close = [')',']','}']
        for x in s:
            if x in p_open:
                p_stack.append(p_dict[x])
            elif x in p_close:
                # 循环过程中栈空了 说明结束的括号多了
                if not p_stack:
                    return False
                # 括号类型不匹配 说明是错误的格式
                if x != p_stack.pop():
                    return False
        # 循环结束栈没空 说明开始的括号多了 没有全部闭合
        if p_stack:
            return False
        return True


    # 优化循环中的if语句位置 能跳出循环的if判断越早越好
    # Runtime: 24 ms, faster than 90.45% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
    def isValid(self, s: str) -> bool:
        p_stack = []
        p_dict = {'(':')','[':']','{':'}'}
        p_open = ['(','[','{']
        p_close = [')',']','}']
        for x in s:
            if x in p_open:
                p_stack.append(p_dict[x])
            # 循环过程中栈空了 说明结束的括号多了
            elif not p_stack:
                return False
            # 括号类型不匹配 说明是错误的格式
            elif x in p_close and x != p_stack.pop():
                return False
        # 循环结束栈没空 说明开始的括号多了 没有全部闭合
        if p_stack:
            return False

        return True

if __name__ == '__main__':
    s = Solution()
    # print(s.isValid('()'))
    # print(s.isValid('(]'))
    # print(s.isValid('()[]{}'))
    # print(s.isValid('([)]'))
    print(s.isValid(']'))
