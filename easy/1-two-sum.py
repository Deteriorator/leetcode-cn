# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     1-two-sum
   Description :
   Author :        Liangz
   Date：          2018/9/25
-------------------------------------------------
   Change Activity:
                   2018/9/25:
-------------------------------------------------
"""
from typing import List

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            if (target - val) in nums[idx+1:]:
                return [idx, nums[idx+1:].index(target-val)+idx+1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    result = Solution()
    print(result.twoSum(nums, 9))
