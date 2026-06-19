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
    s = "ADOBECODEBANC"
    t = "ABC"
    expected = "BANC"

    # 在这里打断点调试
    result = solution.minWindow(s, t)

    print(f"输入: s = {s!r}, t = {t!r}")
    print(f"输出: result = {result!r}")
    print(f"期望: {expected!r}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    s = "a"
    t = "a"
    expected = "a"

    result = solution.minWindow(s, t)

    print(f"输入: s = {s!r}, t = {t!r}")
    print(f"输出: result = {result!r}")
    print(f"期望: {expected!r}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example3():
    """测试示例 3"""
    solution = Solution()
    s = "a"
    t = "aa"
    expected = ""

    result = solution.minWindow(s, t)

    print(f"输入: s = {s!r}, t = {t!r}")
    print(f"输出: result = {result!r}")
    print(f"期望: {expected!r}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_duplicate_chars_in_t():
    """测试边界情况 - t 含重复字符"""
    solution = Solution()
    s = "bbaac"
    t = "aba"
    expected = "baa"

    result = solution.minWindow(s, t)

    print(f"输入: s = {s!r}, t = {t!r}")
    print(f"输出: result = {result!r}")
    print(f"期望: {expected!r}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_no_valid_window():
    """测试边界情况 - s 中缺少 t 的字符"""
    solution = Solution()
    s = "abc"
    t = "def"
    expected = ""

    result = solution.minWindow(s, t)

    print(f"输入: s = {s!r}, t = {t!r}")
    print(f"输出: result = {result!r}")
    print(f"期望: {expected!r}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    s = "bba"
    t = "ab"
    expected = "ba"

    result = solution.minWindow(s, t)

    print(f"输入: s = {s!r}, t = {t!r}")
    print(f"输出: result = {result!r}")
    print(f"期望: {expected!r}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_example3()    # 运行示例 3
    # test_edge_case_duplicate_chars_in_t()  # 运行边界情况 - t 含重复字符
    # test_edge_case_no_valid_window()       # 运行边界情况 - 无有效窗口
    # test_custom()      # 运行自定义测试
