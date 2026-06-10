"""
LeetCode 152. 乘积最大子数组 测试用例
"""

import unittest
from solution import Solution


class TestMaxProduct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [2, 3, -2, 4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 6)

    def test_example2(self):
        """测试示例 2"""
        nums = [-2, 0, -1]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 0)

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        nums = [5]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 5)

    def test_edge_case_single_negative(self):
        """测试边界情况 - 单个负数"""
        nums = [-5]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, -5)

    def test_edge_case_two_negatives(self):
        """测试边界情况 - 两个相邻负数"""
        nums = [-2, -3]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 6)

    def test_edge_case_all_positive(self):
        """测试边界情况 - 全为正数"""
        nums = [1, 2, 3, 4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 24)

    def test_edge_case_contains_zero(self):
        """测试边界情况 - 包含零"""
        nums = [0, 2]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 2)

    def test_edge_case_negative_flip(self):
        """测试边界情况 - 负数使乘积由负转正"""
        nums = [-2, 3, -4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 24)

    def test_edge_case_three_negatives(self):
        """测试边界情况 - 三个负数"""
        nums = [-1, -2, -3]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 6)

    def test_edge_case_alternating_signs(self):
        """测试边界情况 - 正负交替"""
        nums = [3, -1, 4]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 4)

    def test_edge_case_multiple_zeros(self):
        """测试边界情况 - 多个零"""
        nums = [-1, 0, -2, 0, -3]
        result = self.solution.maxProduct(nums)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMaxProduct.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
