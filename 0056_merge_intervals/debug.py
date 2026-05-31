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
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]

    # 在这里打断点调试
    result = solution.merge(intervals)

    print(f"输入: intervals = {intervals}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    intervals = [[1, 4], [4, 5]]
    expected = [[1, 5]]

    result = solution.merge(intervals)

    print(f"输入: intervals = {intervals}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example3():
    """测试示例 3 - 未排序输入"""
    solution = Solution()
    intervals = [[4, 7], [1, 4]]
    expected = [[1, 7]]

    result = solution.merge(intervals)

    print(f"输入: intervals = {intervals}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_single_interval():
    """测试边界情况 - 单个区间"""
    solution = Solution()
    intervals = [[1, 5]]
    expected = [[1, 5]]

    result = solution.merge(intervals)

    print(f"输入: intervals = {intervals}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_no_overlap():
    """测试边界情况 - 无重叠区间"""
    solution = Solution()
    intervals = [[1, 2], [3, 4], [5, 6]]
    expected = [[1, 2], [3, 4], [5, 6]]

    result = solution.merge(intervals)

    print(f"输入: intervals = {intervals}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_all_merge_into_one():
    """测试边界情况 - 全部合并为一个区间"""
    solution = Solution()
    intervals = [[1, 4], [2, 5], [3, 6]]
    expected = [[1, 6]]

    result = solution.merge(intervals)

    print(f"输入: intervals = {intervals}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    intervals = [[1, 10], [2, 3], [4, 8]]
    expected = [[1, 10]]

    result = solution.merge(intervals)

    print(f"输入: intervals = {intervals}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_example3()    # 运行示例 3
    # test_edge_case_single_interval()   # 运行边界情况 - 单个区间
    # test_edge_case_no_overlap()        # 运行边界情况 - 无重叠
    # test_edge_case_all_merge_into_one()  # 运行边界情况 - 全部合并
    # test_custom()      # 运行自定义测试
