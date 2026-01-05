"""
LeetCode 121. 买卖股票的最佳时机 测试用例
"""

import unittest
from solution import Solution


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_example2(self):
        """测试示例 2"""
        prices = [7, 6, 4, 3, 1]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_single_element(self):
        """测试边界情况1：单个元素"""
        prices = [5]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_two_elements_profit(self):
        """测试边界情况2：两个元素，有利润"""
        prices = [1, 2]
        expected = 1
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_two_elements_no_profit(self):
        """测试边界情况3：两个元素，无利润"""
        prices = [2, 1]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_all_same_price(self):
        """测试边界情况4：所有价格相同"""
        prices = [3, 3, 3, 3, 3]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_ascending_prices(self):
        """测试边界情况5：价格递增"""
        prices = [1, 2, 3, 4, 5]
        expected = 4
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_descending_prices(self):
        """测试边界情况6：价格递减"""
        prices = [5, 4, 3, 2, 1]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_price_fluctuation(self):
        """测试边界情况7：价格波动"""
        prices = [2, 4, 1, 3, 5]
        expected = 4
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_min_price_at_end(self):
        """测试边界情况8：最低价在最后"""
        prices = [3, 2, 6, 5, 0, 3]
        expected = 4
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_max_profit_at_beginning(self):
        """测试边界情况9：最大利润在开头"""
        prices = [1, 2, 3, 4, 5, 6, 7]
        expected = 6
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMaxProfit.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)

