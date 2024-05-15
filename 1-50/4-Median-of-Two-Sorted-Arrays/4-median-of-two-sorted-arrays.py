#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    4-median-of-two-sorted-arrays.py
   @Desc:     
   @Author:   Liangz.org@gmail.com
   @Create:   2019.08.05   17:09
-------------------------------------------------------------------------------
   @Change:   2019.08.05
-------------------------------------------------------------------------------
"""

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
1. 简单粗暴法：不考虑时间复杂度
执行结果：通过
显示详情
执行用时 :244 ms, 在所有 Python3 提交中击败了5.24%的用户
内存消耗 :14.1 MB, 在所有 Python3 提交中击败了5.28%的用户
"""


# class Solution:
#     def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
#         nums1.extend(nums2)
#         nums1.sort()
#         if len(nums1) == 0:
#             raise ValueError
#         elif len(nums1) % 2 == 0:
#             result = (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
#             return result
#         else:
#             result = float(nums1[(len(nums1) - 1) // 2])
#             return result

"""
2. 官方解法：
执行结果：通过
显示详情
执行用时 :136 ms, 在所有 Python3 提交中击败了26.29%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.28%的用户
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2, 4]))
