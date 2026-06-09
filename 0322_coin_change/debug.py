#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
调试脚本 - 可以单独运行和调试单个测试用例
使用方法：
1. 直接在 IDE 中运行此文件（可以打断点）
2. 或者命令行运行：python debug.py
3. 修改下面的测试函数调用来选择要调试的测试用例
"""

from solution import Solution


def test_example1():
    """测试示例 1"""
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    expected = 3

    # 在这里打断点调试
    result = solution.coinChange(coins, amount)

    print(f"输入: coins = {coins}, amount = {amount}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    coins = [2]
    amount = 3
    expected = -1

    result = solution.coinChange(coins, amount)

    print(f"输入: coins = {coins}, amount = {amount}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example3():
    """测试示例 3"""
    solution = Solution()
    coins = [1]
    amount = 0
    expected = 0

    result = solution.coinChange(coins, amount)

    print(f"输入: coins = {coins}, amount = {amount}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_greedy_fails():
    """测试边界情况 - 贪心策略不最优"""
    solution = Solution()
    coins = [1, 3, 4]
    amount = 6
    expected = 2

    result = solution.coinChange(coins, amount)

    print(f"输入: coins = {coins}, amount = {amount}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_impossible():
    """测试边界情况 - 无法凑成金额"""
    solution = Solution()
    coins = [3]
    amount = 2
    expected = -1

    result = solution.coinChange(coins, amount)

    print(f"输入: coins = {coins}, amount = {amount}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    coins = [1, 5, 10, 25]
    amount = 30
    expected = 2

    result = solution.coinChange(coins, amount)

    print(f"输入: coins = {coins}, amount = {amount}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_example3()    # 运行示例 3
    # test_edge_case_greedy_fails()  # 运行边界情况 - 贪心不最优
    # test_edge_case_impossible()    # 运行边界情况 - 无法凑成
    # test_custom()      # 运行自定义测试
