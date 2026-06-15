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
    s = "cbaebabacd"
    p = "abc"
    expected = [0, 6]

    # 在这里打断点调试
    result = solution.findAnagrams(s, p)

    print(f"输入: s = {s!r}, p = {p!r}")
    print(f"输出: result = {sorted(result)}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if sorted(result) == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    s = "abab"
    p = "ab"
    expected = [0, 1, 2]

    # 在这里打断点调试
    result = solution.findAnagrams(s, p)

    print(f"输入: s = {s!r}, p = {p!r}")
    print(f"输出: result = {sorted(result)}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if sorted(result) == expected else '❌ 失败'}")


def test_s_shorter_than_p():
    """测试 s 长度小于 p"""
    solution = Solution()
    s = "a"
    p = "ab"
    expected = []

    # 在这里打断点调试
    result = solution.findAnagrams(s, p)

    print(f"输入: s = {s!r}, p = {p!r}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_no_match():
    """测试不存在异位词"""
    solution = Solution()
    s = "aaaa"
    p = "ab"
    expected = []

    # 在这里打断点调试
    result = solution.findAnagrams(s, p)

    print(f"输入: s = {s!r}, p = {p!r}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    s = "ababab"
    p = "aba"
    expected = [0, 2]

    # 在这里打断点调试
    result = solution.findAnagrams(s, p)

    print(f"输入: s = {s!r}, p = {p!r}")
    print(f"输出: result = {sorted(result)}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if sorted(result) == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_s_shorter_than_p()  # 测试 s 长度小于 p
    # test_no_match()    # 测试不存在异位词
    # test_custom()      # 运行自定义测试
