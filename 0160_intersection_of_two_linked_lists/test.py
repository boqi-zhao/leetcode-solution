"""
LeetCode 0160. 相交链表 测试用例
"""

import unittest
from solution import Solution, ListNode


def build_intersecting_lists(list_a, list_b, skip_a, skip_b):
    """
    根据题目评测方式构建两个可能相交的链表。
    返回 (head_a, head_b, intersection_node)
    """
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


class TestGetIntersectionNode(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1：相交节点值为 8"""
        head_a, head_b, expected = build_intersecting_lists(
            [4, 1, 8, 4, 5],
            [5, 6, 1, 8, 4, 5],
            2,
            3,
        )
        result = self.solution.getIntersectionNode(head_a, head_b)
        self.assertIs(result, expected)
        self.assertEqual(result.val, 8)

    def test_example2(self):
        """测试示例 2：相交节点值为 2"""
        head_a, head_b, expected = build_intersecting_lists(
            [1, 9, 1, 2, 4],
            [3, 2, 4],
            3,
            1,
        )
        result = self.solution.getIntersectionNode(head_a, head_b)
        self.assertIs(result, expected)
        self.assertEqual(result.val, 2)

    def test_example3(self):
        """测试示例 3：两个链表不相交"""
        head_a, head_b, expected = build_intersecting_lists(
            [2, 6, 4],
            [1, 5],
            3,
            2,
        )
        result = self.solution.getIntersectionNode(head_a, head_b)
        self.assertIsNone(result)
        self.assertIsNone(expected)

    def test_intersection_at_head(self):
        """测试边界情况：从第一个节点开始相交"""
        head_a, head_b, expected = build_intersecting_lists(
            [7, 8, 9],
            [7, 8, 9],
            0,
            0,
        )
        result = self.solution.getIntersectionNode(head_a, head_b)
        self.assertIs(result, expected)
        self.assertIs(result, head_a)
        self.assertIs(result, head_b)

    def test_one_list_prefix_of_another(self):
        """测试边界情况：一个链表是另一个链表的前缀"""
        head_a, head_b, expected = build_intersecting_lists(
            [1, 2, 3],
            [2, 3],
            1,
            0,
        )
        result = self.solution.getIntersectionNode(head_a, head_b)
        self.assertIs(result, expected)
        self.assertEqual(result.val, 2)

    def test_single_node_intersection(self):
        """测试边界情况：相交部分只有一个节点"""
        head_a, head_b, expected = build_intersecting_lists(
            [5],
            [9, 5],
            0,
            1,
        )
        result = self.solution.getIntersectionNode(head_a, head_b)
        self.assertIs(result, expected)
        self.assertEqual(result.val, 5)

    def test_disjoint_same_values(self):
        """测试边界情况：值相同但节点不同，仍不相交"""
        head_a = build_list([1, 2, 3])
        head_b = build_list([1, 2, 3])
        result = self.solution.getIntersectionNode(head_a, head_b)
        self.assertIsNone(result)

    def test_disjoint_different_lengths(self):
        """测试边界情况：长度不同且不相交"""
        head_a = build_list([1, 2, 3, 4])
        head_b = build_list([5, 6])
        result = self.solution.getIntersectionNode(head_a, head_b)
        self.assertIsNone(result)

    def test_intersection_at_tail(self):
        """测试边界情况：仅在最后一个节点相交"""
        head_a, head_b, expected = build_intersecting_lists(
            [1, 2, 3, 4],
            [9, 8, 4],
            3,
            2,
        )
        result = self.solution.getIntersectionNode(head_a, head_b)
        self.assertIs(result, expected)
        self.assertEqual(result.val, 4)
        self.assertIsNone(result.next)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestGetIntersectionNode.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
