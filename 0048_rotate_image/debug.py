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
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # 在这里打断点调试
    solution.rotate(matrix)

    print(f"输入: matrix = {[[1, 2, 3], [4, 5, 6], [7, 8, 9]]}")
    print(f"输出: matrix = {matrix}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if matrix == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16],
    ]
    expected = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11],
    ]

    solution.rotate(matrix)

    print(f"输入: matrix = {[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]}")
    print(f"输出: matrix = {matrix}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if matrix == expected else '❌ 失败'}")


def test_edge_case_two_by_two():
    """测试边界情况 - 2x2 矩阵"""
    solution = Solution()
    matrix = [[1, 2], [3, 4]]
    expected = [[3, 1], [4, 2]]

    solution.rotate(matrix)

    print(f"输入: matrix = {[[1, 2], [3, 4]]}")
    print(f"输出: matrix = {matrix}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if matrix == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    matrix = [[1]]
    expected = [[1]]

    solution.rotate(matrix)

    print(f"输入: matrix = {[[1]]}")
    print(f"输出: matrix = {matrix}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if matrix == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_edge_case_two_by_two()  # 运行 2x2 边界测试
    # test_custom()      # 运行自定义测试
