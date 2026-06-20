"""
LeetCode 54. 螺旋矩阵 测试用例
"""

import unittest
from solution import Solution


class TestSpiralOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_example2(self):
        """测试示例 2"""
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        matrix = [[1]]
        expected = [1]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_edge_case_single_row(self):
        """测试边界情况 - 单行矩阵"""
        matrix = [[1, 2, 3, 4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_edge_case_single_column(self):
        """测试边界情况 - 单列矩阵"""
        matrix = [[1], [2], [3], [4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_edge_case_two_rows_one_column(self):
        """测试边界情况 - 2 行 1 列"""
        matrix = [[1], [2]]
        expected = [1, 2]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_edge_case_one_row_two_columns(self):
        """测试边界情况 - 1 行 2 列"""
        matrix = [[1, 2]]
        expected = [1, 2]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_edge_case_two_by_two(self):
        """测试边界情况 - 2x2 矩阵"""
        matrix = [[1, 2], [3, 4]]
        expected = [1, 2, 4, 3]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_edge_case_wide_matrix(self):
        """测试边界情况 - 宽矩阵（行数少于列数）"""
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [1, 2, 3, 6, 5, 4]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_edge_case_tall_matrix(self):
        """测试边界情况 - 高矩阵（行数多于列数）"""
        matrix = [[1, 2], [3, 4], [5, 6]]
        expected = [1, 2, 4, 6, 5, 3]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_edge_case_negative_numbers(self):
        """测试边界情况 - 含负数"""
        matrix = [[-1, -2], [-3, -4]]
        expected = [-1, -2, -4, -3]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestSpiralOrder.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
