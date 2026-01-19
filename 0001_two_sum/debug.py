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
    # 输入数据
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]  # 或 [1, 0]
    
    # 在这里打断点调试
    result = solution.twoSum(nums, target)
    
    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected} (或 [1, 0])")
    # 验证结果
    if result in [[0, 1], [1, 0]] and nums[result[0]] + nums[result[1]] == target:
        print(f"结果: ✅ 通过")
    else:
        print(f"结果: ❌ 失败")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    # 输入数据
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]  # 或 [2, 1]
    
    # 在这里打断点调试
    result = solution.twoSum(nums, target)
    
    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected} (或 [2, 1])")
    # 验证结果
    if result in [[1, 2], [2, 1]] and nums[result[0]] + nums[result[1]] == target:
        print(f"结果: ✅ 通过")
    else:
        print(f"结果: ❌ 失败")


def test_example3():
    """测试示例 3"""
    solution = Solution()
    # 输入数据
    nums = [3, 3]
    target = 6
    expected = [0, 1]  # 或 [1, 0]
    
    # 在这里打断点调试
    result = solution.twoSum(nums, target)
    
    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected} (或 [1, 0])")
    # 验证结果
    if result in [[0, 1], [1, 0]] and nums[result[0]] + nums[result[1]] == target:
        print(f"结果: ✅ 通过")
    else:
        print(f"结果: ❌ 失败")


def test_minimum_length():
    """测试最小长度（2个元素）"""
    solution = Solution()
    # 输入数据
    nums = [1, 2]
    target = 3
    expected = [0, 1]  # 或 [1, 0]
    
    # 在这里打断点调试
    result = solution.twoSum(nums, target)
    
    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected} (或 [1, 0])")
    # 验证结果
    if result in [[0, 1], [1, 0]] and nums[result[0]] + nums[result[1]] == target:
        print(f"结果: ✅ 通过")
    else:
        print(f"结果: ❌ 失败")


def test_negative_numbers():
    """测试负数"""
    solution = Solution()
    # 输入数据
    nums = [-1, -2, -3, -4, -5]
    target = -8
    expected = [2, 4]  # 或 [4, 2]
    
    # 在这里打断点调试
    result = solution.twoSum(nums, target)
    
    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected} (或 [4, 2])")
    # 验证结果
    if result in [[2, 4], [4, 2]] and nums[result[0]] + nums[result[1]] == target:
        print(f"结果: ✅ 通过")
    else:
        print(f"结果: ❌ 失败")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    # 输入数据
    nums = [1, 5, 3, 7, 9]
    target = 10
    expected = [1, 3]  # 或 [3, 1]
    
    # 在这里打断点调试
    result = solution.twoSum(nums, target)
    
    print(f"输入: nums = {nums}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected} (或 [3, 1])")
    # 验证结果
    if result in [[1, 3], [3, 1]] and nums[result[0]] + nums[result[1]] == target:
        print(f"结果: ✅ 通过")
    else:
        print(f"结果: ❌ 失败")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例
    
    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_example3()    # 运行示例 3
    # test_minimum_length()  # 测试最小长度
    # test_negative_numbers()  # 测试负数
    # test_custom()      # 运行自定义测试
