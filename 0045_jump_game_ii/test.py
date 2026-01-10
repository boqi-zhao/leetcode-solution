"""
LeetCode 45. 跳跃游戏 II 测试用例
"""

import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [2, 3, 1, 1, 4]
        expected = 2
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        """测试示例 2"""
        nums = [2, 3, 0, 1, 4]
        expected = 2
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        """测试单个元素 - 已经在目标位置"""
        nums = [0]
        expected = 0
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_two_elements(self):
        """测试两个元素"""
        nums = [1, 2]
        expected = 1
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_no_jump_needed(self):
        """测试不需要跳跃（起点直接可达终点）"""
        nums = [5, 0, 0, 0, 0]
        expected = 1
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_minimum_jumps(self):
        """测试最小跳跃次数 - 每次只能跳一格"""
        nums = [1, 1, 1, 1, 1]
        expected = 4
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_mixed_jumps(self):
        """测试混合跳跃值"""
        nums = [1, 2, 1, 1, 1]
        expected = 3
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_large_jump_in_middle(self):
        """测试中间有大的跳跃值"""
        nums = [2, 1, 3, 1, 1, 1]
        expected = 2
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_zero_in_middle(self):
        """测试中间有零（但能跳过）"""
        nums = [2, 0, 2, 0, 1]
        expected = 2
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_longer_array(self):
        """测试较长的数组"""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = 4
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_all_same_large_jumps(self):
        """测试所有元素都很大"""
        nums = [10, 10, 10, 10, 10]
        expected = 1
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)

    def test_optimal_path(self):
        """测试需要找到最优路径"""
        nums = [3, 2, 1, 1, 4]
        expected = 2
        result = self.solution.jump(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
