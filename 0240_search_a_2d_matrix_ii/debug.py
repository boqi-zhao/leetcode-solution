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


MATRIX = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]


def test_example1():
    """测试示例 1"""
    solution = Solution()
    matrix = MATRIX
    target = 5
    expected = True

    # 在这里打断点调试
    result = solution.searchMatrix(matrix, target)

    print(f"输入: matrix = {matrix}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    matrix = MATRIX
    target = 20
    expected = False

    result = solution.searchMatrix(matrix, target)

    print(f"输入: matrix = {matrix}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_edge_case_single_element():
    """测试边界情况 - 单元素矩阵"""
    solution = Solution()
    matrix = [[5]]
    target = 5
    expected = True

    result = solution.searchMatrix(matrix, target)

    print(f"输入: matrix = {matrix}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    matrix = [[-5, -3, -1], [-4, -2, 0], [-3, -1, 2]]
    target = -2
    expected = True

    result = solution.searchMatrix(matrix, target)

    print(f"输入: matrix = {matrix}, target = {target}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_edge_case_single_element()  # 运行单元素边界测试
    # test_custom()      # 运行自定义测试
