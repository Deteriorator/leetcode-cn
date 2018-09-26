# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     1002-WriteTheNum
   Description :
   Author :        Liangz
   Date：          2018/9/26
-------------------------------------------------
   Change Activity:
                   2018/9/26:
-------------------------------------------------
"""
__author__ = 'Liangz'

"""
1002 写出这个数 （20 分）
读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

输入格式：
每个测试输入包含 1 个测试用例，即给出自然数 n 的值。这里保证 n 小于 10
​100
​​ 。

输出格式：
在一行内输出 n 的各位数字之和的每一位，拼音数字间有 1 空格，但一行中最后一个拼音数字后没有空格。

输入样例：
1234567890987654321123456789
输出样例：
yi san wu
"""

dic = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
n = input('请输入正整数：')
length = len(n)
num = int(n)
nums = []
if num < 10**100:
    nums = [int(i) for i in n]
result = sum(nums)
n_sum = [index for index in str(result)]
for i in range(len(n_sum)):
    j = int(n_sum[i])
    k  = dic[j]
    print(k, end=' ')



