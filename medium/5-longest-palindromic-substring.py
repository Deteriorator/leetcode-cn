#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    5-longest-palindromic-substring.py
   @Desc:     
   @Author:   Liangz.org@gmail.com
   @Create:   2019.08.07   11:34
-------------------------------------------------------------------------------
   @Change:   2019.08.07
-------------------------------------------------------------------------------
"""

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
执行结果：通过
显示详情
执行用时 :6368 ms, 在所有 Python3 提交中击败了14.20%的用户
内存消耗 :22.4 MB, 在所有 Python3 提交中击败了5.09%的用户
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        longest = 1
        res = s[0]

        for right in range(1, len(s)):
            for left in range(right):
                if s[left] == s[right] and (right - left <=2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    current_len = right - left + 1
                    if current_len > longest:
                        longest = current_len
                        res = s[left: right + 1]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("ttttttttsssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"))
