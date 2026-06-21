"""
LeetCode 48. 旋转图像 测试用例
"""

import unittest
from solution import Solution


class TestRotate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_example2(self):
        """测试示例 2"""
        matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16],
        ]
        expected = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11],
        ]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        matrix = [[1]]
        expected = [[1]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_two_by_two(self):
        """测试边界情况 - 2x2 矩阵"""
        matrix = [[1, 2], [3, 4]]
        expected = [[3, 1], [4, 2]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_negative_numbers(self):
        """测试边界情况 - 含负数"""
        matrix = [[-1, -2], [-3, -4]]
        expected = [[-3, -1], [-4, -2]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_extreme_values(self):
        """测试边界情况 - 极端值"""
        matrix = [[1000, -1000], [-1000, 1000]]
        expected = [[-1000, 1000], [1000, -1000]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_edge_case_five_by_five(self):
        """测试边界情况 - 5x5 矩阵"""
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        expected = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5],
        ]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestRotate.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
