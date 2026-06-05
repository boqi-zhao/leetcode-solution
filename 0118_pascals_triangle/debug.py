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
    num_rows = 5
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    # 在这里打断点调试
    result = solution.generate(num_rows)

    print(f"输入: numRows = {num_rows}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    num_rows = 1
    expected = [[1]]

    result = solution.generate(num_rows)

    print(f"输入: numRows = {num_rows}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_two_rows():
    """测试边界情况 - numRows=2"""
    solution = Solution()
    num_rows = 2
    expected = [[1], [1, 1]]

    result = solution.generate(num_rows)

    print(f"输入: numRows = {num_rows}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_three_rows():
    """测试边界情况 - numRows=3"""
    solution = Solution()
    num_rows = 3
    expected = [[1], [1, 1], [1, 2, 1]]

    result = solution.generate(num_rows)

    print(f"输入: numRows = {num_rows}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_max_rows():
    """测试边界情况 - 最大值 numRows=30"""
    solution = Solution()
    num_rows = 30

    result = solution.generate(num_rows)

    print(f"输入: numRows = {num_rows}")
    print(f"输出行数: {len(result)}")
    print(f"第 5 行: {result[4] if len(result) >= 5 else 'N/A'}")
    print(f"第 30 行中间元素 result[29][14]: {result[29][14] if len(result) >= 30 else 'N/A'}")
    print(f"期望行数: 30, 第 5 行 [1,4,6,4,1], 第 30 行中间 77558760")
    ok = (
        len(result) == 30
        and result[4] == [1, 4, 6, 4, 1]
        and result[29][14] == 77558760
    )
    print(f"结果: {'✅ 通过' if ok else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    num_rows = 4
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

    result = solution.generate(num_rows)

    print(f"输入: numRows = {num_rows}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_edge_case_two_rows()    # 运行边界情况 - numRows=2
    # test_edge_case_three_rows()  # 运行边界情况 - numRows=3
    # test_edge_case_max_rows()    # 运行边界情况 - 最大值
    # test_custom()      # 运行自定义测试
