"""
LeetCode 0239. 滑动窗口最大值 测试用例
"""

import unittest
from solution import Solution


class TestMaxSlidingWindow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual(
            self.solution.maxSlidingWindow(nums, k), [3, 3, 5, 5, 6, 7]
        )

    def test_example2(self):
        """测试示例 2"""
        nums = [1]
        k = 1
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), [1])

    def test_k_equals_length(self):
        """测试窗口大小等于数组长度"""
        nums = [4, 2, 9, 1]
        k = 4
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), [9])

    def test_two_elements(self):
        """测试两个元素的数组"""
        nums = [1, 2]
        k = 2
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), [2])

    def test_decreasing_sequence(self):
        """测试单调递减序列"""
        nums = [5, 4, 3, 2, 1]
        k = 2
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), [5, 4, 3, 2])

    def test_all_same(self):
        """测试所有元素相同"""
        nums = [3, 3, 3, 3]
        k = 2
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), [3, 3, 3])

    def test_negative_numbers(self):
        """测试包含负数"""
        nums = [-1, -2, -3, -4]
        k = 2
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), [-1, -2, -3])

    def test_increasing_sequence(self):
        """测试单调递增序列"""
        nums = [1, 2, 3, 4, 5]
        k = 3
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), [3, 4, 5])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMaxSlidingWindow.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
