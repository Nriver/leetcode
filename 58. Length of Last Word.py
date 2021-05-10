# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-10-21 11:33:54
# @Last Modified by:   zengjq
# @Last Modified time: 2020-10-21 11:40:05
class Solution:
    # 94 mem 100
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().rsplit(' ', 1)[-1])

s = Solution()
s.lengthOfLastWord('helloworld')