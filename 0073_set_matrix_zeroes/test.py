"""
LeetCode 73. 矩阵置零 测试用例
"""

import copy
import unittest
from solution import Solution


class TestSetZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_example2(self):
        """测试示例 2"""
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_single_element_zero(self):
        """测试边界情况 - 单个元素为 0"""
        matrix = [[0]]
        expected = [[0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_single_element_nonzero(self):
        """测试边界情况 - 单个元素非零"""
        matrix = [[5]]
        expected = [[5]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_single_row(self):
        """测试边界情况 - 单行矩阵"""
        matrix = [[1, 0, 3]]
        expected = [[0, 0, 0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_single_column(self):
        """测试边界情况 - 单列矩阵"""
        matrix = [[1], [0], [3]]
        expected = [[0], [0], [0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_no_zeros(self):
        """测试边界情况 - 矩阵中无零"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = copy.deepcopy(matrix)
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_all_zeros(self):
        """测试边界情况 - 全零矩阵"""
        matrix = [[0, 0], [0, 0]]
        expected = [[0, 0], [0, 0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_zero_in_first_row(self):
        """测试边界情况 - 零位于第一行"""
        matrix = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[0, 0, 0], [0, 5, 6], [0, 8, 9]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_zero_in_first_column(self):
        """测试边界情况 - 零位于第一列"""
        matrix = [[1, 2, 3], [0, 5, 6], [7, 8, 9]]
        expected = [[0, 2, 3], [0, 0, 0], [0, 8, 9]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_multiple_zeros(self):
        """测试边界情况 - 多个零"""
        matrix = [[1, 0, 1], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_negative_numbers(self):
        """测试边界情况 - 含负数"""
        matrix = [[-1, 2, 0], [3, -4, 5]]
        expected = [[0, 0, 0], [0, -4, 0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestSetZeroes.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
