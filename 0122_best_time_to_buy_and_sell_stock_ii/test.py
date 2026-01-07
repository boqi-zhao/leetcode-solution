"""
LeetCode 122. 买卖股票的最佳时机 II 测试用例
"""

import unittest
from solution import Solution


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_example2(self):
        """测试示例 2"""
        prices = [1, 2, 3, 4, 5]
        expected = 4
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_example3(self):
        """测试示例 3"""
        prices = [7, 6, 4, 3, 1]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_edge_case1(self):
        """测试边界情况1：单个元素"""
        prices = [5]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_edge_case2(self):
        """测试边界情况2：两个元素，价格上涨"""
        prices = [1, 2]
        expected = 1
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_edge_case3(self):
        """测试边界情况3：两个元素，价格下跌"""
        prices = [2, 1]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_edge_case4(self):
        """测试边界情况4：所有价格相同"""
        prices = [3, 3, 3, 3, 3]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_edge_case5(self):
        """测试边界情况5：多次买卖"""
        prices = [3, 2, 6, 5, 0, 3]
        expected = 7
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_edge_case6(self):
        """测试边界情况6：连续上涨"""
        prices = [1, 2, 3, 4, 5, 6]
        expected = 5
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_edge_case7(self):
        """测试边界情况7：连续下跌"""
        prices = [6, 5, 4, 3, 2, 1]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)

