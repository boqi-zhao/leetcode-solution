"""
LeetCode 322. 零钱兑换 测试用例
"""

import unittest
from solution import Solution


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        coins = [1, 2, 5]
        amount = 11
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 3)

    def test_example2(self):
        """测试示例 2"""
        coins = [2]
        amount = 3
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, -1)

    def test_example3(self):
        """测试示例 3"""
        coins = [1]
        amount = 0
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 0)

    def test_edge_case_amount_zero(self):
        """测试边界情况 - amount 为 0"""
        coins = [1, 2, 5]
        amount = 0
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 0)

    def test_edge_case_single_coin_exact(self):
        """测试边界情况 - 单种硬币恰好凑成金额"""
        coins = [5]
        amount = 5
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 1)

    def test_edge_case_single_coin_impossible(self):
        """测试边界情况 - 单种硬币无法凑成金额"""
        coins = [3]
        amount = 2
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, -1)

    def test_edge_case_greedy_fails(self):
        """测试边界情况 - 贪心策略不最优（需动态规划）"""
        coins = [1, 3, 4]
        amount = 6
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 2)

    def test_edge_case_all_ones(self):
        """测试边界情况 - 仅面额为 1 的硬币"""
        coins = [1]
        amount = 10
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 10)

    def test_edge_case_large_amount(self):
        """测试边界情况 - 较大金额"""
        coins = [1, 2, 5]
        amount = 100
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 20)

    def test_edge_case_multiple_coins_min(self):
        """测试边界情况 - 多种硬币取最少枚数"""
        coins = [1, 5, 10, 25]
        amount = 30
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestCoinChange.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
