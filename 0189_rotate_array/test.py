"""
LeetCode 189. 轮转数组 测试用例
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

    def test_single_element(self):
        """测试单个元素"""
        nums = [1]
        k = 10
        expected = [1]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_k_zero(self):
        """测试 k 为 0"""
        nums = [1, 2, 3, 4, 5]
        k = 0
        expected = [1, 2, 3, 4, 5]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_k_equals_length(self):
        """测试 k 等于数组长度"""
        nums = [1, 2, 3, 4, 5]
        k = 5
        expected = [1, 2, 3, 4, 5]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_k_greater_than_length(self):
        """测试 k 大于数组长度"""
        nums = [1, 2, 3, 4, 5]
        k = 7
        expected = [4, 5, 1, 2, 3]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_k_one(self):
        """测试 k = 1"""
        nums = [1, 2, 3, 4, 5]
        k = 1
        expected = [5, 1, 2, 3, 4]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_two_elements(self):
        """测试两个元素"""
        nums = [1, 2]
        k = 1
        expected = [2, 1]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_negative_numbers(self):
        """测试负数"""
        nums = [-1, -2, -3, -4, -5]
        k = 2
        expected = [-4, -5, -1, -2, -3]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_mixed_numbers(self):
        """测试混合正负数"""
        nums = [-1, 0, 1, 2, 3]
        k = 3
        expected = [1, 2, 3, -1, 0]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_large_k(self):
        """测试很大的 k 值"""
        nums = [1, 2, 3, 4, 5]
        k = 100000
        expected = [1, 2, 3, 4, 5]
        self.solution.rotate(nums, k)
        self.assertEqual(nums, expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestRotate.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)

