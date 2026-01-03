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
    nums = [1, 1, 1, 2, 2, 3]
    expected_length = 5
    expected_nums = [1, 1, 2, 2, 3]
    
    # 在这里打断点调试
    result = solution.removeDuplicates(nums)
    
    print(f"输入: nums = {[1, 1, 1, 2, 2, 3]}")
    print(f"输出: result = {result}, nums = {nums[:result]}")
    print(f"期望: length = {expected_length}, nums = {expected_nums}")
    print(f"结果: {'✅ 通过' if result == expected_length and nums[:result] == expected_nums else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    expected_length = 7
    expected_nums = [0, 0, 1, 1, 2, 3, 3]
    
    # 在这里打断点调试
    result = solution.removeDuplicates(nums)
    
    print(f"输入: nums = {[0, 0, 1, 1, 1, 1, 2, 3, 3]}")
    print(f"输出: result = {result}, nums = {nums[:result]}")
    print(f"期望: length = {expected_length}, nums = {expected_nums}")
    print(f"结果: {'✅ 通过' if result == expected_length and nums[:result] == expected_nums else '❌ 失败'}")


def test_all_same():
    """测试所有元素相同且超过两个"""
    solution = Solution()
    nums = [2, 2, 2, 2, 2]
    expected_length = 2
    expected_nums = [2, 2]
    
    # 在这里打断点调试
    result = solution.removeDuplicates(nums)
    
    print(f"输入: nums = {[2, 2, 2, 2, 2]}")
    print(f"输出: result = {result}, nums = {nums[:result]}")
    print(f"期望: length = {expected_length}, nums = {expected_nums}")
    print(f"结果: {'✅ 通过' if result == expected_length and nums[:result] == expected_nums else '❌ 失败'}")


def test_mixed():
    """测试混合重复情况"""
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 4]
    expected_length = 7
    expected_nums = [1, 1, 2, 2, 3, 3, 4]
    
    # 在这里打断点调试
    result = solution.removeDuplicates(nums)
    
    print(f"输入: nums = {[1, 1, 1, 2, 2, 2, 2, 3, 3, 4]}")
    print(f"输出: result = {result}, nums = {nums[:result]}")
    print(f"期望: length = {expected_length}, nums = {expected_nums}")
    print(f"结果: {'✅ 通过' if result == expected_length and nums[:result] == expected_nums else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    expected_length = 5
    expected_nums = [1, 2, 3, 4, 5]
    
    # 在这里打断点调试
    result = solution.removeDuplicates(nums)
    
    print(f"输入: nums = {[1, 2, 3, 4, 5]}")
    print(f"输出: result = {result}, nums = {nums[:result]}")
    print(f"期望: length = {expected_length}, nums = {expected_nums}")
    print(f"结果: {'✅ 通过' if result == expected_length and nums[:result] == expected_nums else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例
    
    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_all_same()     # 测试所有元素相同
    # test_mixed()        # 测试混合重复情况
    # test_custom()       # 运行自定义测试

