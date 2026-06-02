"""
LeetCode 0041. 缺失的第一个正数 测试用例
"""

import unittest
from solution import Solution


class TestFirstMissingPositive(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 2, 0]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 3)

    def test_example2(self):
        """测试示例 2"""
        nums = [3, 4, -1, 1]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 2)

    def test_example3(self):
        """测试示例 3"""
        nums = [7, 8, 9, 11, 12]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 1)

    def test_edge_case_single_element_one(self):
        """测试边界情况 - 单个元素 1"""
        nums = [1]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 2)

    def test_edge_case_single_element_other(self):
        """测试边界情况 - 单个元素非 1"""
        nums = [2]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 1)

    def test_edge_case_all_negative(self):
        """测试边界情况 - 全为负数"""
        nums = [-1, -2, -3]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 1)

    def test_edge_case_all_consecutive(self):
        """测试边界情况 - 连续正整数 1 到 n"""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 6)

    def test_edge_case_with_duplicates(self):
        """测试边界情况 - 含重复元素"""
        nums = [1, 1]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 2)

    def test_edge_case_with_zero(self):
        """测试边界情况 - 含零"""
        nums = [0]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 1)

    def test_edge_case_missing_middle(self):
        """测试边界情况 - 中间缺失正数"""
        nums = [1, 3, 4, 5]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 2)

    def test_edge_case_large_values(self):
        """测试边界情况 - 大数值不影响结果"""
        nums = [1000000, 2000000, 3000000]
        result = self.solution.firstMissingPositive(nums)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestFirstMissingPositive.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
