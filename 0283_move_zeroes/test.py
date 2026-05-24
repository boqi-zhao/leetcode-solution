"""
LeetCode 0283. 移动零 测试用例
"""

import unittest
from solution import Solution


class TestMoveZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_example2(self):
        """测试示例 2"""
        nums = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0])

    def test_edge_case_no_zeros(self):
        """测试边界情况 - 没有零"""
        nums = [1, 2, 3, 4]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_edge_case_all_zeros(self):
        """测试边界情况 - 全是零"""
        nums = [0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0])

    def test_edge_case_single_nonzero(self):
        """测试边界情况 - 单个非零元素"""
        nums = [5]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [5])

    def test_edge_case_zeros_at_end(self):
        """测试边界情况 - 零已在末尾"""
        nums = [1, 2, 3, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

    def test_edge_case_zeros_at_start(self):
        """测试边界情况 - 零在开头"""
        nums = [0, 0, 1, 2, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0])

    def test_edge_case_alternating(self):
        """测试边界情况 - 零与非零交替"""
        nums = [0, 1, 0, 2, 0, 3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def test_edge_case_negative_numbers(self):
        """测试边界情况 - 包含负数"""
        nums = [-1, 0, 2, 0, -3]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [-1, 2, -3, 0, 0])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMoveZeroes.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
