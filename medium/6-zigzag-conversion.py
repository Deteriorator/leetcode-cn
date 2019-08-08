#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    6-zigzag-conversion.py
   @Desc:     
   @Author:   Liangz.org@gmail.com
   @Create:   2019.08.08   11:12
-------------------------------------------------------------------------------
   @Change:   2019.08.08
-------------------------------------------------------------------------------
"""
"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
执行结果：通过
显示详情
执行用时 :92 ms, 在所有 Python3 提交中击败了64.88%的用户
内存消耗 :14 MB, 在所有 Python3 提交中击败了7.68%的用户
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        i = 0
        ll = [''] * numRows
        while i < n:
            for line in range(numRows):
                if i < n:
                    ll[line] += s[i]
                    i += 1
            for line in range(numRows-2, 0, -1):
                if i < n:
                    ll[line] += s[i]
                    i += 1
        return ''.join(ll)


import unittest


class Test(unittest.TestCase):
    def test_result(self):
        result = Solution().convert('LEETCODEISHIRING', 4)
        self.assertEqual(result, 'LDREOEIIECIHNTSG')


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
