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
    expected = True

    # 在这里打断点调试
    result = solution.canJump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    nums = [3, 2, 1, 0, 4]
    expected = False

    # 在这里打断点调试
    result = solution.canJump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case1():
    """测试边界情况1：单个元素"""
    solution = Solution()
    nums = [0]
    expected = True

    # 在这里打断点调试
    result = solution.canJump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case2():
    """测试边界情况2：两个元素，可以到达"""
    solution = Solution()
    nums = [1, 0]
    expected = True

    # 在这里打断点调试
    result = solution.canJump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case3():
    """测试边界情况3：两个元素，无法到达"""
    solution = Solution()
    nums = [0, 1]
    expected = False

    # 在这里打断点调试
    result = solution.canJump(nums)

    print(f"输入: nums = {nums}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    nums = [2, 0, 0]
    expected = True

    # 在这里打断点调试
    result = solution.canJump(nums)

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
    # test_custom()      # 运行自定义测试

