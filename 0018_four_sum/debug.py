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


def normalize_quadruplets(quadruplets):
    """将四元组列表标准化：每个四元组内部排序，整体再排序"""
    return sorted([sorted(q) for q in quadruplets])


def test_example1():
    """测试示例 1"""
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    # 在这里打断点调试
    result = solution.fourSum(nums, target)

    normalized_result = normalize_quadruplets(result)
    normalized_expected = normalize_quadruplets(expected)

    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"标准化输出: {normalized_result}")
    print(f"标准化期望: {normalized_expected}")
    print(f"结果: {'✅ 通过' if normalized_result == normalized_expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    nums = [2, 2, 2, 2, 2]
    target = 8
    expected = [[2, 2, 2, 2]]

    result = solution.fourSum(nums, target)

    normalized_result = normalize_quadruplets(result)
    normalized_expected = normalize_quadruplets(expected)

    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"标准化输出: {normalized_result}")
    print(f"标准化期望: {normalized_expected}")
    print(f"结果: {'✅ 通过' if normalized_result == normalized_expected else '❌ 失败'}")


def test_edge_case_no_solution():
    """测试边界情况 - 无解"""
    solution = Solution()
    nums = [1, 2, 3, 4]
    target = 100
    expected = []

    result = solution.fourSum(nums, target)

    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_all_zeros():
    """测试边界情况 - 全零"""
    solution = Solution()
    nums = [0, 0, 0, 0]
    target = 0
    expected = [[0, 0, 0, 0]]

    result = solution.fourSum(nums, target)

    normalized_result = normalize_quadruplets(result)
    normalized_expected = normalize_quadruplets(expected)

    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"标准化输出: {normalized_result}")
    print(f"标准化期望: {normalized_expected}")
    print(f"结果: {'✅ 通过' if normalized_result == normalized_expected else '❌ 失败'}")


def test_edge_case_duplicates():
    """测试边界情况 - 含重复元素"""
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2, -1, -2]
    target = 0
    expected = [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, -1, 0, 2],
        [-1, 0, 0, 1],
    ]

    result = solution.fourSum(nums, target)

    normalized_result = normalize_quadruplets(result)
    normalized_expected = normalize_quadruplets(expected)

    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"标准化输出: {normalized_result}")
    print(f"标准化期望: {normalized_expected}")
    print(f"结果: {'✅ 通过' if normalized_result == normalized_expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    nums = [-2, -1, 0, 1, 2]
    target = -5
    expected = []

    result = solution.fourSum(nums, target)

    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_edge_case_no_solution()   # 运行边界情况 - 无解
    # test_edge_case_all_zeros()     # 运行边界情况 - 全零
    # test_edge_case_duplicates()    # 运行边界情况 - 含重复元素
    # test_custom()      # 运行自定义测试
