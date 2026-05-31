"""
LeetCode 0056. 合并区间 测试用例
"""

import unittest
from solution import Solution


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 6], [8, 10], [15, 18]])

    def test_example2(self):
        """测试示例 2"""
        intervals = [[1, 4], [4, 5]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 5]])

    def test_example3(self):
        """测试示例 3 - 未排序输入"""
        intervals = [[4, 7], [1, 4]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 7]])

    def test_edge_case_single_interval(self):
        """测试边界情况 - 单个区间"""
        intervals = [[1, 5]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 5]])

    def test_edge_case_no_overlap(self):
        """测试边界情况 - 无重叠区间"""
        intervals = [[1, 2], [3, 4], [5, 6]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6]])

    def test_edge_case_all_merge_into_one(self):
        """测试边界情况 - 全部合并为一个区间"""
        intervals = [[1, 4], [2, 5], [3, 6]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 6]])

    def test_edge_case_one_contains_another(self):
        """测试边界情况 - 一个区间完全包含另一个"""
        intervals = [[1, 10], [2, 3], [4, 8]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 10]])

    def test_edge_case_same_start_different_end(self):
        """测试边界情况 - 相同起点不同终点"""
        intervals = [[1, 3], [1, 5], [1, 2]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 5]])

    def test_edge_case_point_intervals(self):
        """测试边界情况 - 退化为点的区间"""
        intervals = [[1, 1], [1, 2], [2, 2]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 2]])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMerge.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
