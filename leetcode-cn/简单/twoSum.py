# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     twoSum
   Description :
   Author :        Liangz
   Date：          2018/9/25
-------------------------------------------------
   Change Activity:
                   2018/9/25:
-------------------------------------------------
"""
__author__ = 'Liangz'

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
nums = []
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = []
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)

        return result     # 在LeetCode-cn返回用return，不要print


if __name__ == '__main__':
    nums = [2,7,11,15]
    result = Solution()
    print(result.twoSum(nums, 9))
