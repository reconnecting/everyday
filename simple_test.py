#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
author:jacob
created_date:2019/02/20
update:2019/03/05
"""


class Solution():
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

    def twoSum_dict_function(self, nums, target):
        # 这个方法是hash方法
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_value = {}
        for index, value in enumerate(nums):
            another_num = target - value
            if another_num in index_value:
                return [index_value[another_num], index]
            index_value[nums] = index
        return None

    def two_list_plus(self, a, b):
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

    def lengthOfLongestSubstring(self, s):
        # 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        # 自己的答案时间复杂度太高了
        """
        :param s: str
        :return: int
        """
        if s == "":
            print(len(s))
            return len(s)
        else:
            result = []
            for x in range(len(s)):
                for y in range(x + 1, len(s) + 1):
                    new = s[x:y:]
                    if len(new) == len(set(new)):
                        result.append(len(new))
            print(max(result))
            return max(result)

    def lengthOfLongestSubstring_pass(self, s):
        # 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        # 这个时间复杂度孩子可以
        """
        :param s: str
        :return: int
        """
        if s == "":
            print(len(s))
            return len(s)
        else:
            dict_str = {}
            # 定义一个max_lan,来放每次循环的最大值，并最终返回
            max_len = 0
            start_str = 0
            # 这个循环，如果没有重复，则一直进行下去
            for i in range(len(s)):
                # 这个判断，一旦有重复字母，那起始计算长度的点将会从重复字母处增加一个单位
                if s[i] in dict_str and dict_str[s[i]] >= start_str:
                    start_str = dict_str[s[i]] + 1
                    print(s[start_str::])
                # 如果有
                this_time_max_len = i - start_str + 1
                dict_str[s[i]] = i
                max_len = max(this_time_max_len, max_len)
            print(max_len)
            return max_len

    def findMedianSortedArrays(self, nums1, nums2):
        # 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
        # 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
        # 自己写的答案时间复杂度为(n+m)logN，不对，需要优化
        """
        :param nums1: list
        :param nums2: list
        :return: float（中位数）
        """
        num = nums1 + nums2
        num = sorted(num)
        if len(num) == 1:
            return num[0]
        if len(num) % 2 == 0:
            print((num[int(len(num) / 2)] + num[int(len(num) / 2) - 1]) / 2)
            return (num[int(len(num) / 2)] + num[int(len(num) / 2) - 1]) / 2
        else:
            print((num[int(len(num) / 2)] + num[int(len(num) / 2)]) / 2)
            return num[int(len(num) / 2)]

    def longestPalindrome(self, s):
        # 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
        # 暴力法再次失败，呜呜呜
        """
        :param s: str
        :return: str
        """
        if s == "":
            return ""
        result = []
        for x in range(len(s)):
            for y in range(x + 1, len(s) + 1):
                new = s[x:y:]
                sort_new = new[::-1]
                # print(sort_new)
                if new == sort_new:
                    result.append(new)
        length = []
        for x in range(len(result)):
            length.append(len(result[x]))
        a = max(length)
        print(result[length.index(a)])
        return result[length.index(a)]

    def threeSum(self, nums):
        # 这个暴力法，时间复杂度太高了，需要改进
        """
        :param nums: 
        :return: 
        """
        result = []
        num1 = []
        num2 = []
        num3 = []
        result_new = []
        if len(nums) < 3:
            return []
        if len(nums) == nums.count(0):
            return [[0, 0, 0]]
        for x in nums:
            if x > 0:
                num1.append(x)
            if x < 0:
                num2.append(x)
            if x == 0:
                num3.append(x)
        if len(num3) == 0:
            print(u"没有0")
            if sum(nums) == 0 and len(nums) == 3:
                return [nums]
            for x, vx in enumerate(num1):
                if x + 1 > len(num1) - 1:
                    break
                for j, vj in enumerate(num1[x + 1:]):
                    if -(vx + vj) in num2:
                        result.append([vx, vj, -(vx + vj)])
            for x, vx in enumerate(num2):
                if x + 1 > len(num2) - 1:
                    break
                for j, vj in enumerate(num2[x + 1:]):
                    if -(vx + vj) in num1:
                        result.append([vx, vj, -(vx + vj)])
            for i in result:
                c = sorted(i)
                if c not in result_new:
                    result_new.append(c)
            print(result_new)
            return result_new
        if len(num3) == 1 or len(num3) == 2:
            print(u"有一个或者两个0")
            for x in num1:
                for y in num2:
                    if x + y == 0:
                        result.append([x, 0, y])
            if len(num1) >= 2:
                for x, vx in enumerate(num1):
                    if x + 1 > len(num1) - 1:
                        break
                    for j, vj in enumerate(num1[x + 1:]):
                        if -(vx + vj) in num2:
                            result.append([vx, vj, -(vx + vj)])
            if len(num2) >= 2:
                for x, vx in enumerate(num2):
                    if x + 1 > len(num2) - 1:
                        break
                    for j, vj in enumerate(num2[x + 1:]):
                        if -(vx + vj) in num1:
                            result.append([vx, vj, -(vx + vj)])
            for i in result:
                c = sorted(i)
                print(c)
                if c not in result_new:
                    result_new.append(c)
            return result_new
        else:
            print(u"三个0")
            for x in num1:
                for y in num2:
                    if x + y == 0:
                        result.append([x, 0, y])
            for x, vx in enumerate(num1):
                if x + 1 > len(num1) - 1:
                    break
                for j, vj in enumerate(num1[x + 1:]):
                    if -(vx + vj) in num2:
                        result.append([vx, vj, -(vx + vj)])
            for x, vx in enumerate(num2):
                if x + 1 > len(num2) - 1:
                    break
                for j, vj in enumerate(num2[x + 1:]):
                    if -(vx + vj) in num1:
                        result.append([vx, vj, -(vx + vj)])
            for i in result:
                c = sorted(i)
                if c not in result_new:
                    result_new.append(c)
            result_new.append([0, 0, 0])
            print(result_new)
            return result_new

    def removeDuplicates(self, nums):
        # 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
        # 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
        """
        :param nums:
        :return:
        """
        n = len(nums)
        i = 0
        for x in range(n):
            if x < n - 1 and nums[x - i] == nums[x + 1 - i]:
                nums.remove(nums[x - i])
                i = i + 1
        print(nums)
        return len(nums)

    def removeElement(self, nums, val):
        """
        :param nums: 
        :param val: 
        :return: 
        """
        for x in range(len(nums)):
            # print(x)
            if val in nums:
                nums.remove(val)
        return nums

    def isPalindrome(self, x):
        # 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
        """
        :param x: 
        :return: bool
        """
        if x >= 0 and int(str(x)[::-1]) == x:
            return True
        else:
            return False

    def singleNumber_1(self, nums):
        # 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        """
        :param nums 
        :return: 
        """
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber_2(self, nums):
        # 使用异或，一个循环搞定
        """
        :param nums: 
        :return: 
        """
        n = 0
        for x in nums:
            n = n ^ nums
        return n

    def reverseString(self, s):
        # 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
        # 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
        # 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
        """
        :param s:
        :return:
        """
        return s.reverse()

    def majorityElement_1(self, nums):
        # 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
        # 你可以假设数组是非空的，并且给定的数组总是存在众数。
        """
        :param nums:
        :return:
        """
        a = len(nums) // 2
        b = sorted(nums)
        print(b[a])
        return b[a]

    def majorityElement_2(self, nums):
        # 这个时间复杂度比较高
        for x in nums:
            if nums.count(x) > len(nums) / 2:
                print(x)
                return x

    def multiply(self, num1, num2):
        # 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
        """
        :param num1:
        :param num2:
        :return:
        """
        return str(int(num1) * int(num2))

    def subsets(self, nums):
        # 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）
        # 此题的精妙之处在于，把每次的新子集都加上新的数，就是完整的子集了
        """
        :param nums:
        :return:
        """
        output = [[]]
        for x in range(len(nums)):
            for j in range(len(output)):
                print(j)
                output.append(output[j] + [nums[x]])  # 每次新的子集都加上新的数字
        print(output)
        return output

if __name__ == '__main__':
    test = Solution()
    test.lengthOfLongestSubstring_pass("yreqqy6753100p;..nhioplngfdvbkjhtub8tt77v6rc6e5yctswaadfgghjklmnbvcxzwertyuio")
