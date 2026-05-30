"""
LeetCode 0053. 最大子数组和 测试用例
"""

import unittest
from solution import Solution


class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, 6)

    def test_example2(self):
        """测试示例 2"""
        nums = [1]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, 1)

    def test_example3(self):
        """测试示例 3"""
        nums = [5, 4, -1, 7, 8]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, 23)

    def test_edge_case_all_negative(self):
        """测试边界情况 - 全为负数"""
        nums = [-3, -1, -2]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, -1)

    def test_edge_case_all_positive(self):
        """测试边界情况 - 全为正数"""
        nums = [1, 2, 3, 4]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, 10)

    def test_edge_case_mixed_with_negative_sum_prefix(self):
        """测试边界情况 - 前缀和为负应丢弃"""
        nums = [-2, 1, -3, 4]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, 4)

    def test_edge_case_single_negative(self):
        """测试边界情况 - 单个负数"""
        nums = [-5]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, -5)

    def test_edge_case_alternating(self):
        """测试边界情况 - 正负交替"""
        nums = [1, -2, 3, -4, 5]
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMaxSubArray.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
