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
    # 输入数据
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    
    # 在这里打断点调试
    result = solution.groupAnagrams(strs)
    
    # 对结果进行标准化处理：每个子列表排序，然后整个结果排序
    normalized_result = sorted([sorted(group) for group in result])
    normalized_expected = sorted([sorted(group) for group in expected])
    
    print(f"输入: strs = {strs}")
    print(f"输出: result = {result}")
    print(f"标准化输出: {normalized_result}")
    print(f"期望: {expected}")
    print(f"标准化期望: {normalized_expected}")
    print(f"结果: {'✅ 通过' if normalized_result == normalized_expected else '❌ 失败'}")


def test_example2():
    """测试示例 2 - 空字符串"""
    solution = Solution()
    strs = [""]
    expected = [[""]]
    
    result = solution.groupAnagrams(strs)
    
    print(f"输入: strs = {strs}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example3():
    """测试示例 3 - 单个字符"""
    solution = Solution()
    strs = ["a"]
    expected = [["a"]]
    
    result = solution.groupAnagrams(strs)
    
    print(f"输入: strs = {strs}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_empty_array():
    """测试边界情况 - 空数组"""
    solution = Solution()
    strs = []
    expected = []
    
    result = solution.groupAnagrams(strs)
    
    print(f"输入: strs = {strs}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_single_group():
    """测试边界情况 - 所有字符串都是异位词"""
    solution = Solution()
    strs = ["abc", "bca", "cab"]
    expected = [["abc", "bca", "cab"]]
    
    result = solution.groupAnagrams(strs)
    normalized_result = sorted([sorted(group) for group in result])
    normalized_expected = sorted([sorted(group) for group in expected])
    
    print(f"输入: strs = {strs}")
    print(f"输出: result = {result}")
    print(f"标准化输出: {normalized_result}")
    print(f"期望: {expected}")
    print(f"标准化期望: {normalized_expected}")
    print(f"结果: {'✅ 通过' if normalized_result == normalized_expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    strs = ["listen", "silent", "enlist", "hello", "world"]
    expected = [["listen", "silent", "enlist"], ["hello"], ["world"]]
    
    result = solution.groupAnagrams(strs)
    normalized_result = sorted([sorted(group) for group in result])
    normalized_expected = sorted([sorted(group) for group in expected])
    
    print(f"输入: strs = {strs}")
    print(f"输出: result = {result}")
    print(f"标准化输出: {normalized_result}")
    print(f"期望: {expected}")
    print(f"标准化期望: {normalized_expected}")
    print(f"结果: {'✅ 通过' if normalized_result == normalized_expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例
    
    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_example3()    # 运行示例 3
    # test_edge_case_empty_array()      # 运行边界情况 - 空数组
    # test_edge_case_single_group()     # 运行边界情况 - 所有字符串都是异位词
    # test_custom()      # 运行自定义测试
