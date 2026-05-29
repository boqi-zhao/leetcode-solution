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
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected = 6

    # 在这里打断点调试
    result = solution.trap(height)

    print(f"输入: height = {height}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    height = [4, 2, 0, 3, 2, 5]
    expected = 9

    result = solution.trap(height)

    print(f"输入: height = {height}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_valley():
    """测试边界情况 - 简单凹槽"""
    solution = Solution()
    height = [3, 0, 3]
    expected = 3

    result = solution.trap(height)

    print(f"输入: height = {height}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_single_element():
    """测试边界情况 - 单个元素"""
    solution = Solution()
    height = [5]
    expected = 0

    result = solution.trap(height)

    print(f"输入: height = {height}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_monotonic_increasing():
    """测试边界情况 - 单调递增"""
    solution = Solution()
    height = [1, 2, 3, 4, 5]
    expected = 0

    result = solution.trap(height)

    print(f"输入: height = {height}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    height = [4, 2, 0, 3, 2, 5]
    expected = 9

    result = solution.trap(height)

    print(f"输入: height = {height}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_edge_case_valley()              # 运行边界情况 - 简单凹槽
    # test_edge_case_single_element()      # 运行边界情况 - 单个元素
    # test_edge_case_monotonic_increasing()  # 运行边界情况 - 单调递增
    # test_custom()      # 运行自定义测试
