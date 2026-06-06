"""
LeetCode 0198. 打家劫舍 测试用例
"""

import unittest
from solution import Solution


class TestRob(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 2, 3, 1]
        expected = 4
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        """测试示例 2"""
        nums = [2, 7, 9, 3, 1]
        expected = 12
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        nums = [5]
        expected = 5
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_edge_case_two_elements(self):
        """测试边界情况 - 两个元素"""
        nums = [2, 1]
        expected = 2
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_edge_case_all_zeros(self):
        """测试边界情况 - 全为 0"""
        nums = [0, 0, 0, 0]
        expected = 0
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_edge_case_alternating(self):
        """测试边界情况 - 交替金额"""
        nums = [1, 2, 1, 2, 1]
        expected = 4
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_edge_case_max_value(self):
        """测试边界情况 - 最大金额 400"""
        nums = [400, 0, 400]
        expected = 800
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_edge_case_skip_middle(self):
        """测试边界情况 - 跳过中间较大值"""
        nums = [2, 1, 1, 2]
        expected = 4
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestRob.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
