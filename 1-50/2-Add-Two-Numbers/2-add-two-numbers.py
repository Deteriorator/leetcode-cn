#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    2-add-two-numbers.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2019.08.05   9:38
-------------------------------------------------------------------------------
   @Change:   2019.08.05
-------------------------------------------------------------------------------
"""


"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存
储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     sum = l1.val + l2.val
    #     l3 = ListNode(sum % 10)
    #     l3.next = ListNode(sum // 10)
    #     n1 = l1.next
    #     n2 = l2.next
    #     n3 = l3
    #     while True:
    #         if n1 and n2:
    #             sum = n1.val + n2.val + n3.next.val
    #             n3.next.val = sum % 10
    #             n3.next.next = ListNode(sum // 10)
    #             n1 = n1.next
    #             n2 = n2.next
    #             n3 = n3.next
    #         elif n1 and (not n2):
    #             sum = n1.val + n3.next.val
    #             n3.next.val = sum % 10
    #             n3.next.next = ListNode(sum // 10)
    #             n1 = n1.next
    #             n3 = n3.next
    #         elif (not n1) and n2:
    #             sum = n2.val + n3.next.val
    #             n3.next.val = sum % 10
    #             n3.next.next = ListNode(sum // 10)
    #             n2 = n3.next
    #             n3 = n3.next
    #         else:
    #             if n3.next.val == 0:
    #                 n3.next = None
    #             break
    #     return l3

"""
执行结果：通过
显示详情
执行用时 :76 ms, 在所有 Python3 提交中击败了99.81%的用户
内存消耗 :14 MB, 在所有 Python3 提交中击败了5.06%的用户
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        curr = result
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = carry + x + y
            curr.next = ListNode(sum % 10)
            carry = sum // 10
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return result.next


if __name__ == '__main__':
    s = Solution()
