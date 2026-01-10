"""
LeetCode 274. H指数 测试用例
"""

import unittest
from solution import Solution


class TestHIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        citations = [3, 0, 6, 1, 5]
        expected = 3
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_example2(self):
        """测试示例 2"""
        citations = [1, 3, 1]
        expected = 1
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_empty_array(self):
        """测试空数组"""
        citations = []
        expected = 0
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_single_zero(self):
        """测试单个元素为 0"""
        citations = [0]
        expected = 0
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_single_one(self):
        """测试单个元素为 1"""
        citations = [1]
        expected = 1
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_all_zeros(self):
        """测试全为 0"""
        citations = [0, 0, 0, 0]
        expected = 0
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_all_ones(self):
        """测试全为 1"""
        citations = [1, 1, 1, 1]
        expected = 1
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_large_numbers(self):
        """测试大数值"""
        citations = [100, 100, 100]
        expected = 3
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_increasing_sequence(self):
        """测试递增序列"""
        citations = [1, 2, 3, 4, 5]
        expected = 3
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_decreasing_sequence(self):
        """测试递减序列"""
        citations = [5, 4, 3, 2, 1]
        expected = 3
        self.assertEqual(self.solution.hIndex(citations), expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestHIndex.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
