"""
LeetCode 0560. 和为 K 的子数组 测试用例
"""

import unittest
from solution import Solution


class TestSubarraySum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 1, 1]
        k = 2
        self.assertEqual(self.solution.subarraySum(nums, k), 2)

    def test_example2(self):
        """测试示例 2"""
        nums = [1, 2, 3]
        k = 3
        self.assertEqual(self.solution.subarraySum(nums, k), 2)

    def test_single_element_match(self):
        """测试单元素且和等于 k"""
        nums = [5]
        k = 5
        self.assertEqual(self.solution.subarraySum(nums, k), 1)

    def test_single_element_no_match(self):
        """测试单元素且和不等于 k"""
        nums = [5]
        k = 3
        self.assertEqual(self.solution.subarraySum(nums, k), 0)

    def test_negative_numbers(self):
        """测试包含负数的情况"""
        nums = [1, -1, 0]
        k = 0
        self.assertEqual(self.solution.subarraySum(nums, k), 3)

    def test_all_zeros(self):
        """测试全零数组"""
        nums = [0, 0, 0]
        k = 0
        self.assertEqual(self.solution.subarraySum(nums, k), 6)

    def test_no_subarray(self):
        """测试不存在和为 k 的子数组"""
        nums = [1, 2, 3]
        k = 10
        self.assertEqual(self.solution.subarraySum(nums, k), 0)

    def test_negative_k(self):
        """测试 k 为负数"""
        nums = [1, -2, 1]
        k = -1
        self.assertEqual(self.solution.subarraySum(nums, k), 2)

    def test_classic_prefix_sum(self):
        """测试经典前缀和用例"""
        nums = [3, 4, 7, 2, -3, 1, 4, 2]
        k = 7
        self.assertEqual(self.solution.subarraySum(nums, k), 4)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestSubarraySum.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
