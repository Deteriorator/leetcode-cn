# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     9-palindrome-number
   Description :
   Author :        Liangz
   Date：          2018/9/28
-------------------------------------------------
   Change Activity:
                   2019/8/4:
-------------------------------------------------
"""
__author__ = 'Liangz'

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

"""

"""
1. 使用字符串很简单
执行结果：通过
显示详情
执行用时 :84 ms, 在所有 Python3 提交中击败了91.45%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.01%的用户
"""
# class Solution(object):
#     def isPalindrome(self, x: int) -> bool:
#         """
#         :type x: int
#         :rtype: bool
#         """
#         return str(x) == str(x)[::-1]

"""
执行结果：通过
显示详情
执行用时 :112 ms, 在所有 Python3 提交中击败了45.90%的用户
内存消耗 :14 MB, 在所有 Python3 提交中击败了5.01%的用户
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        y = 0
        quotient = x
        while quotient != 0:
            remainder = quotient % 10
            y = y * 10 + remainder
            quotient = int(quotient / 10)
        return x == y


if __name__ == '__main__':
    # x = int(input())
    x = Solution()
    print(x.isPalindrome(1221))
