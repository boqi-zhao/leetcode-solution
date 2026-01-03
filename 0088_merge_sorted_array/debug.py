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
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]
    
    # 在这里打断点调试
    solution.merge(nums1, m, nums2, n)
    
    print(f"输入: nums1 = {[1, 2, 3, 0, 0, 0]}, m = {m}, nums2 = {nums2}, n = {n}")
    print(f"输出: nums1 = {nums1}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums1 == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected = [1]
    
    # 在这里打断点调试
    solution.merge(nums1, m, nums2, n)
    
    print(f"输入: nums1 = {[1]}, m = {m}, nums2 = {nums2}, n = {n}")
    print(f"输出: nums1 = {nums1}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums1 == expected else '❌ 失败'}")


def test_example3():
    """测试示例 3"""
    solution = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected = [1]
    
    # 在这里打断点调试
    solution.merge(nums1, m, nums2, n)
    
    print(f"输入: nums1 = {[0]}, m = {m}, nums2 = {nums2}, n = {n}")
    print(f"输出: nums1 = {nums1}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums1 == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    nums1 = [1, 3, 5, 0, 0, 0]
    m = 3
    nums2 = [2, 4, 6]
    n = 3
    expected = [1, 2, 3, 4, 5, 6]
    
    # 在这里打断点调试
    solution.merge(nums1, m, nums2, n)
    
    print(f"输入: nums1 = {[1, 3, 5, 0, 0, 0]}, m = {m}, nums2 = {nums2}, n = {n}")
    print(f"输出: nums1 = {nums1}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if nums1 == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例
    
    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_example3()    # 运行示例 3
    # test_custom()      # 运行自定义测试

