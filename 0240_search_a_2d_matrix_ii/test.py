"""
LeetCode 240. 搜索二维矩阵 II 测试用例
"""

import unittest
from solution import Solution


MATRIX = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]


class TestSearchMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        self.assertTrue(self.solution.searchMatrix(MATRIX, 5))

    def test_example2(self):
        """测试示例 2"""
        self.assertFalse(self.solution.searchMatrix(MATRIX, 20))

    def test_edge_case_single_element_found(self):
        """测试边界情况 - 单元素矩阵且目标存在"""
        self.assertTrue(self.solution.searchMatrix([[5]], 5))

    def test_edge_case_single_element_not_found(self):
        """测试边界情况 - 单元素矩阵且目标不存在"""
        self.assertFalse(self.solution.searchMatrix([[5]], 3))

    def test_edge_case_target_at_top_left(self):
        """测试边界情况 - 目标位于左上角"""
        self.assertTrue(self.solution.searchMatrix(MATRIX, 1))

    def test_edge_case_target_at_bottom_right(self):
        """测试边界情况 - 目标位于右下角"""
        self.assertTrue(self.solution.searchMatrix(MATRIX, 30))

    def test_edge_case_target_smaller_than_min(self):
        """测试边界情况 - 目标小于矩阵最小值"""
        self.assertFalse(self.solution.searchMatrix(MATRIX, 0))

    def test_edge_case_target_larger_than_max(self):
        """测试边界情况 - 目标大于矩阵最大值"""
        self.assertFalse(self.solution.searchMatrix(MATRIX, 31))

    def test_edge_case_single_row_found(self):
        """测试边界情况 - 单行矩阵且目标存在"""
        self.assertTrue(self.solution.searchMatrix([[1, 3, 5, 7]], 5))

    def test_edge_case_single_row_not_found(self):
        """测试边界情况 - 单行矩阵且目标不存在"""
        self.assertFalse(self.solution.searchMatrix([[1, 3, 5, 7]], 4))

    def test_edge_case_single_column_found(self):
        """测试边界情况 - 单列矩阵且目标存在"""
        self.assertTrue(self.solution.searchMatrix([[2], [4], [6], [8]], 6))

    def test_edge_case_single_column_not_found(self):
        """测试边界情况 - 单列矩阵且目标不存在"""
        self.assertFalse(self.solution.searchMatrix([[2], [4], [6], [8]], 5))

    def test_edge_case_negative_numbers(self):
        """测试边界情况 - 含负数"""
        matrix = [[-5, -3, -1], [-4, -2, 0], [-3, -1, 2]]
        self.assertTrue(self.solution.searchMatrix(matrix, -2))
        self.assertFalse(self.solution.searchMatrix(matrix, -6))

    def test_edge_case_target_on_diagonal_path(self):
        """测试边界情况 - 目标位于搜索路径中间"""
        self.assertTrue(self.solution.searchMatrix(MATRIX, 14))
        self.assertTrue(self.solution.searchMatrix(MATRIX, 18))


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestSearchMatrix.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
