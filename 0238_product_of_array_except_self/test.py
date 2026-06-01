"""
LeetCode 0238. 除了自身以外数组的乘积 测试用例
"""

import unittest
from solution import Solution


class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 2, 3, 4]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [24, 12, 8, 6])

    def test_example2(self):
        """测试示例 2"""
        nums = [-1, 1, 0, -3, 3]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [0, 0, 9, 0, 0])

    def test_edge_case_two_elements(self):
        """测试边界情况 - 最小长度 2"""
        nums = [2, 3]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [3, 2])

    def test_edge_case_all_ones(self):
        """测试边界情况 - 全为 1"""
        nums = [1, 1, 1, 1]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [1, 1, 1, 1])

    def test_edge_case_negative_numbers(self):
        """测试边界情况 - 含负数且无零"""
        nums = [2, -3, 4]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [-12, 8, -6])

    def test_edge_case_multiple_zeros(self):
        """测试边界情况 - 多个零"""
        nums = [0, 0, 1, 2]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [0, 0, 0, 0])

    def test_edge_case_single_zero(self):
        """测试边界情况 - 单个零"""
        nums = [1, 2, 0, 4]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [0, 0, 8, 0])

    def test_edge_case_all_negative(self):
        """测试边界情况 - 全为负数"""
        nums = [-2, -3, -4]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [12, 8, 6])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestProductExceptSelf.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
