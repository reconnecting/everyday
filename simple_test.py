#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
author:jacob
created_date:2019/02/20
update:2019/02/21
"""


class Solution:
    """给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

        你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。"""

    def twoSum(self, nums, target):
        # 比较笨拙的方法，有改进空间
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] == target - nums[y]:
                    if x != y:
                        return x, y

    def two_list_plus(self,a, b):
        """
        :param a: list
        :param b: list
        :return: list
        """
        # 原题目是listnode，被我改成了两个列表…………………………无语！！！！
        a = a[::-1]
        b = b[::-1]
        sum_a = []
        sum_b = []
        print(a, b)
        n = len(a) - 1
        for x in a:
            index_value1 = x * (10 ** n)
            sum_a.append(index_value1)
            n = n - 1
        m = len(b) - 1
        for x in b:
            index_value2 = x * (10 ** m)
            sum_b.append(index_value2)
            m = m - 1
        finalsum = []
        for x in range(len(a)):
            finalsum.append(sum_b[x] + sum_a[x])
        h = len(a) - 1
        result_list = []
        for x in finalsum:
            value = x / (10 ** h)
            result_list.append(int(value))
            h -= 1
        print(result_list)
        return result_list


if __name__ == '__main__':
    pass
