"""
LeetCode 0189. 轮转数组 测试用例
"""

import unittest
from solution import Solution


class TestRotate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_example2(self):
        """测试示例 2"""
        nums = [-1, -100, 3, 99]
        k = 2
        expected = [3, 99, -1, -100]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_edge_case_k_zero(self):
        """测试边界情况 - k 为 0，数组不变"""
        nums = [1, 2, 3]
        k = 0
        expected = [1, 2, 3]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        nums = [42]
        k = 5
        expected = [42]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_edge_case_k_equals_length(self):
        """测试边界情况 - k 等于数组长度，数组不变"""
        nums = [1, 2, 3, 4]
        k = 4
        expected = [1, 2, 3, 4]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_edge_case_k_greater_than_length(self):
        """测试边界情况 - k 大于数组长度，等价于 k % n"""
        nums = [1, 2, 3]
        k = 4
        expected = [3, 1, 2]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_edge_case_two_elements(self):
        """测试边界情况 - 两个元素"""
        nums = [1, 2]
        k = 1
        expected = [2, 1]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_edge_case_full_rotate_minus_one(self):
        """测试边界情况 - k 为 n-1"""
        nums = [1, 2, 3, 4]
        k = 3
        expected = [2, 3, 4, 1]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestRotate.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
