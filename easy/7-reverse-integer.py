# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     7-reverse-integer
   Description :
   Author :        Liangz
   Date：          2018/9/25
-------------------------------------------------
   Change Activity:
                   2019/8/3:
-------------------------------------------------
"""

"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，
如果反转后的整数溢出，则返回 0。
"""


# 执行结果：通过
# 显示详情
# 执行用时 :56 ms, 在所有 Python3 提交中击败了55.30%的用户
# 内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.21%的用户

class Solution(object):
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if -2 ** 31 <= x <= 2 ** 31 - 1:
            if x > 0:
                a = str(x)[::-1]
                a = int(a)
                if -2 ** 31 <= a <= 2 ** 31 - 1:
                    return a
                else:
                    return 0
            elif x == 0:
                return 0
            else:
                a = abs(x)
                a = str(a)[::-1]
                a = int(a)
                if -2 ** 31 <= a <= 2 ** 31 - 1:
                    return 0-a
                else:
                    return 0
        else:
            return 0


# import math
#
#
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         if x > 0:
#             a = self.num_reverse(x)
#             if a > math.pow(2, 31) - 1:
#                 return 0
#             else:
#                 return a
#         else:
#             a = abs(x)
#             b = self.num_reverse(a)
#             if b < -math.pow(2, 31):
#                 return 0
#             else:
#                 return 0-b
#
#     def num_reverse(self, x):
#         ret = []
#         for a in str(x):
#             ret.append(a)
#         if ret[-1] == '0':
#             ret.remove(ret[-1])
#             ret.reverse()
#             x = ''.join(ret)
#             return int(x)
#         else:
#             ret.reverse()
#             x = ''.join(ret)
#             return int(x)


# class Solution:
#     def reverse(self, x: int) -> int:
#         str_x = str(x)[::-1]
#         y = ''
#         if str_x[-1] == '-':
#             y = '-'
#         y += str_x.rstrip('-').lstrip('0')
#         if (-2 ** 31) < x < (2 ** 31 - 1):
#             return int(y)
#         else:
#             return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))
