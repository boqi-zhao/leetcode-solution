"""
LeetCode 416. 分割等和子集 测试用例
"""

import unittest
from solution import Solution


class TestCanPartition(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 5, 11, 5]
        result = self.solution.canPartition(nums)
        self.assertTrue(result)

    def test_example2(self):
        """测试示例 2"""
        nums = [1, 2, 3, 5]
        result = self.solution.canPartition(nums)
        self.assertFalse(result)

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        nums = [1]
        result = self.solution.canPartition(nums)
        self.assertFalse(result)

    def test_edge_case_two_equal_elements(self):
        """测试边界情况 - 两个相等元素"""
        nums = [1, 1]
        result = self.solution.canPartition(nums)
        self.assertTrue(result)

    def test_edge_case_odd_sum(self):
        """测试边界情况 - 总和为奇数"""
        nums = [1, 2, 4]
        result = self.solution.canPartition(nums)
        self.assertFalse(result)

    def test_edge_case_all_same_even_count(self):
        """测试边界情况 - 全部相同且数量为偶数"""
        nums = [2, 2, 2, 2]
        result = self.solution.canPartition(nums)
        self.assertTrue(result)

    def test_edge_case_all_same_odd_count(self):
        """测试边界情况 - 全部相同且数量为奇数"""
        nums = [2, 2, 2]
        result = self.solution.canPartition(nums)
        self.assertFalse(result)

    def test_edge_case_can_partition(self):
        """测试边界情况 - 可以分割的较长数组"""
        nums = [1, 2, 3, 4, 5, 6, 7]
        result = self.solution.canPartition(nums)
        self.assertTrue(result)

    def test_edge_case_cannot_partition_even_sum(self):
        """测试边界情况 - 总和为偶数但无法分割"""
        nums = [1, 2, 5]
        result = self.solution.canPartition(nums)
        self.assertFalse(result)

    def test_edge_case_large_values(self):
        """测试边界情况 - 较大元素值"""
        nums = [100, 100]
        result = self.solution.canPartition(nums)
        self.assertTrue(result)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestCanPartition.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
