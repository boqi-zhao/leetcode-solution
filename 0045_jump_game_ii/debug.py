#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
调试脚本 - 可以单独运行和调试单个测试用例
使用方法：
1. 直接在 IDE 中运行此文件（可以打断点）
2. 或者命令行运行：python debug.py
3. 修改下面的 test_case 变量来选择要调试的测试用例
"""

from solution import Solution


def test_example1():
    """测试示例 1"""
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    expected = 2

    # 在这里打断点调试
    result = solution.jump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    nums = [2, 3, 0, 1, 4]
    expected = 2

    # 在这里打断点调试
    result = solution.jump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case1():
    """测试边界情况1：单个元素"""
    solution = Solution()
    nums = [0]
    expected = 0

    # 在这里打断点调试
    result = solution.jump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case2():
    """测试边界情况2：两个元素"""
    solution = Solution()
    nums = [1, 0]
    expected = 1

    # 在这里打断点调试
    result = solution.jump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case3():
    """测试边界情况3：三个元素，需要两步"""
    solution = Solution()
    nums = [1, 1, 1]
    expected = 2

    # 在这里打断点调试
    result = solution.jump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case4():
    """测试边界情况4：可以直接跳到末尾"""
    solution = Solution()
    nums = [5, 0, 0, 0, 0]
    expected = 1

    # 在这里打断点调试
    result = solution.jump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    nums = [1, 2, 1, 1, 1]
    expected = 3

    # 在这里打断点调试
    result = solution.jump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_edge_case1()  # 运行边界情况1
    # test_edge_case2()  # 运行边界情况2
    # test_edge_case3()  # 运行边界情况3
    # test_edge_case4()  # 运行边界情况4
    # test_custom()      # 运行自定义测试

