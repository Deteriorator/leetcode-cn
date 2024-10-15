#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    3-longest-substring-without-repeating-characters.py
   @Desc:     
   @Author:   Liang.org@gmail.com
   @Create:   2019.08.05   15:46
-------------------------------------------------------------------------------
   @Change:   2019.08.05
-------------------------------------------------------------------------------
"""


"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
执行结果：通过
显示详情
执行用时 :160 ms, 在所有 Python3 提交中击败了27.39%的用户
内存消耗 :14 MB, 在所有 Python3 提交中击败了5.01%的用户
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lists = []
        max_length = 0
        for i in s:
            if i not in lists:
                lists.append(i)
            else:
                lists = lists[lists.index(i)+1:]
                lists.append(i)
            max_length = max(len(lists), max_length)

        return max_length if max_length != 0 else len(s)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbbcdefghia"))
