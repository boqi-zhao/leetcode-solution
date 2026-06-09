"""
LeetCode 279. 完全平方数 测试用例
"""

import unittest
from solution import Solution


class TestNumSquares(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        n = 12
        result = self.solution.numSquares(n)
        self.assertEqual(result, 3)

    def test_example2(self):
        """测试示例 2"""
        n = 13
        result = self.solution.numSquares(n)
        self.assertEqual(result, 2)

    def test_edge_case_min(self):
        """测试边界情况 - 最小值 n=1"""
        n = 1
        result = self.solution.numSquares(n)
        self.assertEqual(result, 1)

    def test_edge_case_perfect_square(self):
        """测试边界情况 - n 本身是完全平方数"""
        n = 4
        result = self.solution.numSquares(n)
        self.assertEqual(result, 1)

    def test_edge_case_small(self):
        """测试边界情况 - 小数值 n=2"""
        n = 2
        result = self.solution.numSquares(n)
        self.assertEqual(result, 2)

    def test_edge_case_n5(self):
        """测试边界情况 - n=5"""
        n = 5
        result = self.solution.numSquares(n)
        self.assertEqual(result, 2)

    def test_edge_case_n7(self):
        """测试边界情况 - n=7（需要 4 个完全平方数）"""
        n = 7
        result = self.solution.numSquares(n)
        self.assertEqual(result, 4)

    def test_edge_case_large_perfect_square(self):
        """测试边界情况 - 大完全平方数 n=100"""
        n = 100
        result = self.solution.numSquares(n)
        self.assertEqual(result, 1)

    def test_edge_case_max(self):
        """测试边界情况 - 最大值 n=10000"""
        n = 10000
        result = self.solution.numSquares(n)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestNumSquares.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
