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
    n = 2
    expected = 2

    # 在这里打断点调试
    result = solution.climbStairs(n)

    print(f"输入: n = {n}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    n = 3
    expected = 3

    result = solution.climbStairs(n)

    print(f"输入: n = {n}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_min():
    """测试边界情况 - 最小值 n=1"""
    solution = Solution()
    n = 1
    expected = 1

    result = solution.climbStairs(n)

    print(f"输入: n = {n}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_n4():
    """测试边界情况 - n=4"""
    solution = Solution()
    n = 4
    expected = 5

    result = solution.climbStairs(n)

    print(f"输入: n = {n}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_max():
    """测试边界情况 - 最大值 n=45"""
    solution = Solution()
    n = 45
    expected = 1836311903

    result = solution.climbStairs(n)

    print(f"输入: n = {n}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    n = 10
    expected = 89

    result = solution.climbStairs(n)

    print(f"输入: n = {n}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_edge_case_min()   # 运行边界情况 - 最小值
    # test_edge_case_n4()    # 运行边界情况 - n=4
    # test_edge_case_max()   # 运行边界情况 - 最大值
    # test_custom()      # 运行自定义测试
