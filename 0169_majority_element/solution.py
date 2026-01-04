"""
LeetCode 169. 多数元素 (Majority Element)

题目描述：
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2

提示：
- n == nums.length
- 1 <= n <= 5 * 10⁴
- -10⁹ <= nums[i] <= 10⁹
- 输入保证数组中一定有一个多数元素。

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for i in range(len(nums)):
            if not d.get(nums[i]):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        for k, v in d.items():
            if v > len(nums) / 2:
                return k


