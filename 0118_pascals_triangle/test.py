"""
LeetCode 0118. 杨辉三角 测试用例
"""

import unittest
from solution import Solution


class TestGenerate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        num_rows = 5
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        result = self.solution.generate(num_rows)
        self.assertEqual(result, expected)

    def test_example2(self):
        """测试示例 2"""
        num_rows = 1
        expected = [[1]]
        result = self.solution.generate(num_rows)
        self.assertEqual(result, expected)

    def test_edge_case_two_rows(self):
        """测试边界情况 - numRows=2"""
        num_rows = 2
        expected = [[1], [1, 1]]
        result = self.solution.generate(num_rows)
        self.assertEqual(result, expected)

    def test_edge_case_three_rows(self):
        """测试边界情况 - numRows=3"""
        num_rows = 3
        expected = [[1], [1, 1], [1, 2, 1]]
        result = self.solution.generate(num_rows)
        self.assertEqual(result, expected)

    def test_edge_case_max_rows(self):
        """测试边界情况 - 最大值 numRows=30"""
        num_rows = 30
        result = self.solution.generate(num_rows)
        self.assertEqual(len(result), 30)
        for i, row in enumerate(result):
            self.assertEqual(len(row), i + 1)
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)
        self.assertEqual(result[4], [1, 4, 6, 4, 1])
        self.assertEqual(result[29][14], 77558760)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestGenerate.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
