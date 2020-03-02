# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-02 16:11:53
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-02 16:23:40

class Solution:

    # 结果会浮动
    # Runtime: 24 ms, faster than 91.28% of Python3 online submissions for Implement strStr().
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement strStr().
    # Runtime: 32 ms, faster than 47.05% of Python3 online submissions for Implement strStr().
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Implement strStr().
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            # 这个是个有意思的问题
            # print(haystack.replace('', '1111'))
            # print('1111h1111e1111l1111l1111o1111')
            return 0
        lh = len(haystack)
        ln = len(needle)
        for i in range(lh - ln + 1):
            is_match = True
            for j in range(ln):
                if haystack[i+j] != needle[j]:
                    is_match = False
                    break
            if is_match:
                return i

        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr('hello', 'll'))
    print(s.strStr('aaaaa', 'bba'))