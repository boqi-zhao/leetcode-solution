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


def build_intersecting_lists(list_a, list_b, skip_a, skip_b):
    """根据题目评测方式构建两个可能相交的链表"""
    def build_chain(values):
        if not values:
            return None, None
        head = ListNode(values[0])
        tail = head
        for value in values[1:]:
            tail.next = ListNode(value)
            tail = tail.next
        return head, tail

    prefix_a = list_a[:skip_a]
    prefix_b = list_b[:skip_b]
    common_values = list_a[skip_a:]

    head_a, tail_a = build_chain(prefix_a)
    head_b, tail_b = build_chain(prefix_b)
    common_head, _ = build_chain(common_values)

    if tail_a:
        tail_a.next = common_head
    else:
        head_a = common_head

    if tail_b:
        tail_b.next = common_head
    else:
        head_b = common_head

    return head_a, head_b, common_head


def build_list(values):
    """构建单链表"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def list_to_values(head):
    """将链表转换为列表，便于打印"""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def test_example1():
    """测试示例 1"""
    solution = Solution()
    head_a, head_b, expected = build_intersecting_lists(
        [4, 1, 8, 4, 5],
        [5, 6, 1, 8, 4, 5],
        2,
        3,
    )

    # 在这里打断点调试
    result = solution.getIntersectionNode(head_a, head_b)

    print("输入:")
    print(f"  listA = [4, 1, 8, 4, 5], skipA = 2")
    print(f"  listB = [5, 6, 1, 8, 4, 5], skipB = 3")
    print(f"输出: result = {result.val if result else None}")
    print(f"期望: expected = {expected.val if expected else None}")
    print(f"结果: {'✅ 通过' if result is expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    head_a, head_b, expected = build_intersecting_lists(
        [1, 9, 1, 2, 4],
        [3, 2, 4],
        3,
        1,
    )

    result = solution.getIntersectionNode(head_a, head_b)

    print("输入:")
    print(f"  listA = [1, 9, 1, 2, 4], skipA = 3")
    print(f"  listB = [3, 2, 4], skipB = 1")
    print(f"输出: result = {result.val if result else None}")
    print(f"期望: expected = {expected.val if expected else None}")
    print(f"结果: {'✅ 通过' if result is expected else '❌ 失败'}")


def test_example3():
    """测试示例 3"""
    solution = Solution()
    head_a, head_b, expected = build_intersecting_lists(
        [2, 6, 4],
        [1, 5],
        3,
        2,
    )

    result = solution.getIntersectionNode(head_a, head_b)

    print("输入:")
    print(f"  listA = [2, 6, 4], listB = [1, 5], 不相交")
    print(f"输出: result = {result}")
    print(f"期望: expected = {expected}")
    print(f"结果: {'✅ 通过' if result is expected else '❌ 失败'}")


def test_intersection_at_head():
    """测试边界情况：从第一个节点开始相交"""
    solution = Solution()
    head_a, head_b, expected = build_intersecting_lists(
        [7, 8, 9],
        [7, 8, 9],
        0,
        0,
    )

    result = solution.getIntersectionNode(head_a, head_b)

    print("输入:")
    print(f"  listA = [7, 8, 9], listB = [7, 8, 9], skipA = 0, skipB = 0")
    print(f"输出: result = {result.val if result else None}")
    print(f"期望: expected = {expected.val if expected else None}")
    print(f"结果: {'✅ 通过' if result is expected else '❌ 失败'}")


def test_disjoint_same_values():
    """测试边界情况：值相同但节点不同"""
    solution = Solution()
    head_a = build_list([1, 2, 3])
    head_b = build_list([1, 2, 3])
    expected = None

    result = solution.getIntersectionNode(head_a, head_b)

    print("输入:")
    print(f"  listA = {list_to_values(head_a)}")
    print(f"  listB = {list_to_values(head_b)}（节点不同）")
    print(f"输出: result = {result}")
    print(f"期望: expected = {expected}")
    print(f"结果: {'✅ 通过' if result is expected else '❌ 失败'}")


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    head_a, head_b, expected = build_intersecting_lists(
        [1, 2, 3, 4],
        [9, 8, 4],
        3,
        2,
    )

    result = solution.getIntersectionNode(head_a, head_b)

    print("输入:")
    print(f"  listA = [1, 2, 3, 4], listB = [9, 8, 4], 在尾部节点 4 相交")
    print(f"输出: result = {result.val if result else None}")
    print(f"期望: expected = {expected.val if expected else None}")
    print(f"结果: {'✅ 通过' if result is expected else '❌ 失败'}")


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例

    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_example3()    # 运行示例 3
    # test_intersection_at_head()  # 从头部相交
    # test_disjoint_same_values()  # 值相同但不相交
    # test_custom()      # 运行自定义测试
