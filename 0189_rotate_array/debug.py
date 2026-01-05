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
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    expected = [5, 6, 7, 1, 2, 3, 4]
    original_nums = nums.copy()
    
    # 在这里打断点调试
    solution.rotate(nums, k)
    
    print(f"输入: nums = {original_nums}, k = {k}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    nums = [-1, -100, 3, 99]
    k = 2
    expected = [3, 99, -1, -100]
    original_nums = nums.copy()
    
    # 在这里打断点调试
    solution.rotate(nums, k)
    
    print(f"输入: nums = {original_nums}, k = {k}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


def test_k_greater_than_length():
    """测试 k 大于数组长度"""
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 7
    expected = [4, 5, 1, 2, 3]
    original_nums = nums.copy()
    
    # 在这里打断点调试
    solution.rotate(nums, k)
    
    print(f"输入: nums = {original_nums}, k = {k}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    nums = [1, 2, 3]
    k = 1
    expected = [3, 1, 2]
    original_nums = nums.copy()
    
    # 在这里打断点调试
    solution.rotate(nums, k)
    
    print(f"输入: nums = {original_nums}, k = {k}")
    print(f"输出: nums = {nums}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例
    
    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_k_greater_than_length()  # 测试 k 大于数组长度
    # test_custom()      # 运行自定义测试

