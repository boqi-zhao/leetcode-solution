"""
LeetCode 0042. 接雨水 测试用例
"""

import unittest
from solution import Solution


class TestTrap(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        result = self.solution.trap(height)
        self.assertEqual(result, 6)

    def test_example2(self):
        """测试示例 2"""
        height = [4, 2, 0, 3, 2, 5]
        result = self.solution.trap(height)
        self.assertEqual(result, 9)

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        height = [5]
        result = self.solution.trap(height)
        self.assertEqual(result, 0)

    def test_edge_case_two_elements(self):
        """测试边界情况 - 两个元素"""
        height = [2, 3]
        result = self.solution.trap(height)
        self.assertEqual(result, 0)

    def test_edge_case_flat(self):
        """测试边界情况 - 平坦地形"""
        height = [3, 3, 3, 3]
        result = self.solution.trap(height)
        self.assertEqual(result, 0)

    def test_edge_case_monotonic_increasing(self):
        """测试边界情况 - 单调递增"""
        height = [1, 2, 3, 4, 5]
        result = self.solution.trap(height)
        self.assertEqual(result, 0)

    def test_edge_case_monotonic_decreasing(self):
        """测试边界情况 - 单调递减"""
        height = [5, 4, 3, 2, 1]
        result = self.solution.trap(height)
        self.assertEqual(result, 0)

    def test_edge_case_valley(self):
        """测试边界情况 - 简单凹槽"""
        height = [3, 0, 3]
        result = self.solution.trap(height)
        self.assertEqual(result, 3)

    def test_edge_case_all_zeros(self):
        """测试边界情况 - 全零"""
        height = [0, 0, 0]
        result = self.solution.trap(height)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestTrap.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
