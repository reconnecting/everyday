#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
author:jacob
created_date:2019/02/20
update:2019/02/20
"""

class Solution:
    """给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

        你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。"""
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x]==target-nums[y]:
                    if x!=y:
                        return x,y