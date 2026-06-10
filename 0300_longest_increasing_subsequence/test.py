"""
LeetCode 300. 最长递增子序列 测试用例
"""

import unittest
from solution import Solution


class TestLengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 4)

    def test_example2(self):
        """测试示例 2"""
        nums = [0, 1, 0, 3, 2, 3]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 4)

    def test_example3(self):
        """测试示例 3"""
        nums = [7, 7, 7, 7, 7, 7, 7]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 1)

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        nums = [42]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 1)

    def test_edge_case_strictly_increasing(self):
        """测试边界情况 - 严格递增数组"""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 5)

    def test_edge_case_strictly_decreasing(self):
        """测试边界情况 - 严格递减数组"""
        nums = [5, 4, 3, 2, 1]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 1)

    def test_edge_case_two_elements_increasing(self):
        """测试边界情况 - 两个元素递增"""
        nums = [1, 2]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 2)

    def test_edge_case_two_elements_decreasing(self):
        """测试边界情况 - 两个元素递减"""
        nums = [2, 1]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 1)

    def test_edge_case_negative_numbers(self):
        """测试边界情况 - 包含负数"""
        nums = [-2, -1, -3, 0, 1]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 4)

    def test_edge_case_alternating(self):
        """测试边界情况 - 交替升降"""
        nums = [1, 3, 2, 4, 3, 5]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 4)

    def test_edge_case_extreme_values(self):
        """测试边界情况 - 极端数值"""
        nums = [-10000, 0, 10000]
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestLengthOfLIS.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
