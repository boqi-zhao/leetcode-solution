"""
LeetCode 55. 跳跃游戏 测试用例
"""

import unittest
from solution import Solution


class TestCanJump(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [2, 3, 1, 1, 4]
        expected = True
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        """测试示例 2"""
        nums = [3, 2, 1, 0, 4]
        expected = False
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case1(self):
        """测试边界情况1：单个元素"""
        nums = [0]
        expected = True
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case2(self):
        """测试边界情况2：两个元素，可以到达"""
        nums = [1, 0]
        expected = True
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case3(self):
        """测试边界情况3：两个元素，无法到达"""
        nums = [0, 1]
        expected = False
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case4(self):
        """测试边界情况4：所有元素都是0，但只有一个元素"""
        nums = [0]
        expected = True
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case5(self):
        """测试边界情况5：所有元素都是0，多个元素"""
        nums = [0, 0, 0]
        expected = False
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case6(self):
        """测试边界情况6：第一个元素为0，多个元素"""
        nums = [0, 2, 3]
        expected = False
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case7(self):
        """测试边界情况7：可以直接跳到末尾"""
        nums = [5, 0, 0, 0, 0]
        expected = True
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case8(self):
        """测试边界情况8：中间有0，但可以跳过"""
        nums = [2, 0, 0]
        expected = True
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case9(self):
        """测试边界情况9：递增数组"""
        nums = [1, 2, 3, 4, 5]
        expected = True
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)

    def test_edge_case10(self):
        """测试边界情况10：递减数组"""
        nums = [5, 4, 3, 2, 1, 0, 0]
        expected = False
        result = self.solution.canJump(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)

