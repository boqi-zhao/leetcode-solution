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
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]

    # 在这里打断点调试
    solution.moveZeroes(nums)

    print(f"输入: nums = {[0, 1, 0, 3, 12]}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    nums = [0]
    expected = [0]

    solution.moveZeroes(nums)

    print(f"输入: nums = {[0]}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


def test_edge_case_no_zeros():
    """测试边界情况 - 没有零"""
    solution = Solution()
    nums = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]

    solution.moveZeroes(nums)

    print(f"输入: nums = {[1, 2, 3, 4]}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


def test_edge_case_all_zeros():
    """测试边界情况 - 全是零"""
    solution = Solution()
    nums = [0, 0, 0]
    expected = [0, 0, 0]

    solution.moveZeroes(nums)

    print(f"输入: nums = {[0, 0, 0]}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


def test_edge_case_alternating():
    """测试边界情况 - 零与非零交替"""
    solution = Solution()
    nums = [0, 1, 0, 2, 0, 3]
    expected = [1, 2, 3, 0, 0, 0]

    solution.moveZeroes(nums)

    print(f"输入: nums = {[0, 1, 0, 2, 0, 3]}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    nums = [-1, 0, 2, 0, -3]
    expected = [-1, 2, -3, 0, 0]

    solution.moveZeroes(nums)

    print(f"输入: nums = {[-1, 0, 2, 0, -3]}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_edge_case_no_zeros()       # 运行边界情况 - 没有零
    # test_edge_case_all_zeros()      # 运行边界情况 - 全是零
    # test_edge_case_alternating()    # 运行边界情况 - 零与非零交替
    # test_custom()      # 运行自定义测试
