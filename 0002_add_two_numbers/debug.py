#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
调试脚本 - 可以单独运行和调试单个测试用例
使用方法：
1. 直接在 IDE 中运行此文件（可以打断点）
2. 或者命令行运行：python debug.py
3. 修改下面的 test_case 变量来选择要调试的测试用例
"""

from solution import Solution, ListNode


def build_list(values):
    """根据列表构建单链表"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def list_to_values(head):
    """将单链表转换为列表"""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def test_example1():
    """测试示例 1"""
    solution = Solution()
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    expected = [7, 0, 8]

    # 在这里打断点调试
    result = solution.addTwoNumbers(l1, l2)

    print(f"输入: l1 = [2, 4, 3], l2 = [5, 6, 4]")
    print(f"输出: result = {list_to_values(result)}")
    print(f"期望: expected = {expected}")
    print(f"结果: {'✅ 通过' if list_to_values(result) == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    l1 = build_list([0])
    l2 = build_list([0])
    expected = [0]

    result = solution.addTwoNumbers(l1, l2)

    print(f"输入: l1 = [0], l2 = [0]")
    print(f"输出: result = {list_to_values(result)}")
    print(f"期望: expected = {expected}")
    print(f"结果: {'✅ 通过' if list_to_values(result) == expected else '❌ 失败'}")


def test_example3():
    """测试示例 3"""
    solution = Solution()
    l1 = build_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_list([9, 9, 9, 9])
    expected = [8, 9, 9, 9, 0, 0, 0, 1]

    result = solution.addTwoNumbers(l1, l2)

    print(f"输入: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]")
    print(f"输出: result = {list_to_values(result)}")
    print(f"期望: expected = {expected}")
    print(f"结果: {'✅ 通过' if list_to_values(result) == expected else '❌ 失败'}")


def test_carry_at_end():
    """测试边界情况：末尾产生进位"""
    solution = Solution()
    l1 = build_list([9, 9])
    l2 = build_list([1])
    expected = [0, 0, 1]

    result = solution.addTwoNumbers(l1, l2)

    print(f"输入: l1 = [9, 9], l2 = [1]")
    print(f"输出: result = {list_to_values(result)}")
    print(f"期望: expected = {expected}")
    print(f"结果: {'✅ 通过' if list_to_values(result) == expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    l1 = build_list([9, 9, 9])
    l2 = build_list([9, 9, 9])
    expected = [8, 9, 9, 1]

    result = solution.addTwoNumbers(l1, l2)

    print(f"输入: l1 = [9, 9, 9], l2 = [9, 9, 9]")
    print(f"输出: result = {list_to_values(result)}")
    print(f"期望: expected = {expected}")
    print(f"结果: {'✅ 通过' if list_to_values(result) == expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_example3()    # 运行示例 3
    # test_carry_at_end()  # 末尾进位
    # test_custom()      # 运行自定义测试
