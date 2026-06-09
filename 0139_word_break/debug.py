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
    s = "leetcode"
    wordDict = ["leet", "code"]
    expected = True

    # 在这里打断点调试
    result = solution.wordBreak(s, wordDict)

    print(f"输入: s = {s!r}, wordDict = {wordDict}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    expected = True

    result = solution.wordBreak(s, wordDict)

    print(f"输入: s = {s!r}, wordDict = {wordDict}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example3():
    """测试示例 3"""
    solution = Solution()
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    expected = False

    result = solution.wordBreak(s, wordDict)

    print(f"输入: s = {s!r}, wordDict = {wordDict}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_prefix_trap():
    """测试边界情况 - 前缀陷阱"""
    solution = Solution()
    s = "cars"
    wordDict = ["car", "ca", "rs"]
    expected = True

    result = solution.wordBreak(s, wordDict)

    print(f"输入: s = {s!r}, wordDict = {wordDict}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_reuse_word():
    """测试边界情况 - 重复使用同一单词"""
    solution = Solution()
    s = "aaaa"
    wordDict = ["aa"]
    expected = True

    result = solution.wordBreak(s, wordDict)

    print(f"输入: s = {s!r}, wordDict = {wordDict}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    expected = True

    result = solution.wordBreak(s, wordDict)

    print(f"输入: s = {s!r}, wordDict = {wordDict}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_example3()    # 运行示例 3
    # test_edge_case_prefix_trap()  # 运行边界情况 - 前缀陷阱
    # test_edge_case_reuse_word()   # 运行边界情况 - 重复使用单词
    # test_custom()      # 运行自定义测试
