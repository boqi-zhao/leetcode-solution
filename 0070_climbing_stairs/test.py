"""
LeetCode 0070. 爬楼梯 测试用例
"""

import unittest
from solution import Solution


class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        n = 2
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 2)

    def test_example2(self):
        """测试示例 2"""
        n = 3
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 3)

    def test_edge_case_min(self):
        """测试边界情况 - 最小值 n=1"""
        n = 1
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 1)

    def test_edge_case_n4(self):
        """测试边界情况 - n=4"""
        n = 4
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 5)

    def test_edge_case_n5(self):
        """测试边界情况 - n=5"""
        n = 5
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 8)

    def test_edge_case_max(self):
        """测试边界情况 - 最大值 n=45"""
        n = 45
        result = self.solution.climbStairs(n)
        self.assertEqual(result, 1836311903)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestClimbStairs.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
