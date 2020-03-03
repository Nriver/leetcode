# -*- coding: utf-8 -*-
# @Author: zengjq
# @Date:   2020-03-03 14:19:23
# @Last Modified by:   zengjq
# @Last Modified time: 2020-03-03 14:27:25

class Solution:

    # 执行时间会变
    # Runtime: 20 ms, faster than 97.50% of Python3 online submissions for Day of the Year.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Day of the Year.
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        # 闰年
        if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
            m_days = [31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            m_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        return sum(m_days[:month-1]) + day

if __name__ == '__main__':
    s = Solution()
    print(s.dayOfYear('2019-01-09'))
    print(s.dayOfYear('2019-02-10'))
    print(s.dayOfYear('2003-03-01'))
    print(s.dayOfYear('2004-03-01'))