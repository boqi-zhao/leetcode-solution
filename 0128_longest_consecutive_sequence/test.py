"""
LeetCode 0128. 最长连续序列 测试用例
"""

import unittest
from solution import Solution


class TestLongestConsecutive(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [100, 4, 200, 1, 3, 2]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 4)

    def test_example2(self):
        """测试示例 2"""
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 9)

    def test_example3(self):
        """测试示例 3"""
        nums = [1, 0, 1, 2]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 3)

    def test_edge_case_empty_array(self):
        """测试边界情况 - 空数组"""
        nums = []
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 0)

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        nums = [1]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 1)

    def test_edge_case_duplicates(self):
        """测试边界情况 - 大量重复元素"""
        nums = [2, 2, 2, 2, 2]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 1)

    def test_edge_case_no_consecutive(self):
        """测试边界情况 - 无连续序列，每个元素独立"""
        nums = [10, 30, 50]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 1)

    def test_edge_case_negative_numbers(self):
        """测试边界情况 - 包含负数"""
        nums = [-1, -2, -3, 0, 1]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 5)

    def test_edge_case_two_sequences(self):
        """测试边界情况 - 两段不连续的序列"""
        nums = [1, 2, 3, 100, 101, 102, 103]
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestLongestConsecutive.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
