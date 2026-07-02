"""
LeetCode 0025. K 个一组翻转链表 测试用例
"""

import unittest
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


class TestReverseKGroup(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        head = build_list([1, 2, 3, 4, 5])
        result = self.solution.reverseKGroup(head, 2)
        self.assertEqual(list_to_values(result), [2, 1, 4, 3, 5])

    def test_example2(self):
        """测试示例 2"""
        head = build_list([1, 2, 3, 4, 5])
        result = self.solution.reverseKGroup(head, 3)
        self.assertEqual(list_to_values(result), [3, 2, 1, 4, 5])

    def test_single_node(self):
        """测试边界情况：单个节点"""
        head = build_list([1])
        result = self.solution.reverseKGroup(head, 1)
        self.assertEqual(list_to_values(result), [1])

    def test_k_equals_length(self):
        """测试边界情况：k 等于链表长度，整链翻转"""
        head = build_list([1, 2, 3, 4])
        result = self.solution.reverseKGroup(head, 4)
        self.assertEqual(list_to_values(result), [4, 3, 2, 1])

    def test_k_equals_one(self):
        """测试边界情况：k 为 1，链表不变"""
        head = build_list([1, 2, 3, 4, 5])
        result = self.solution.reverseKGroup(head, 1)
        self.assertEqual(list_to_values(result), [1, 2, 3, 4, 5])

    def test_remainder_nodes(self):
        """测试边界情况：剩余节点不足 k 个时保持原序"""
        head = build_list([1, 2, 3, 4, 5, 6, 7])
        result = self.solution.reverseKGroup(head, 3)
        self.assertEqual(list_to_values(result), [3, 2, 1, 6, 5, 4, 7])

    def test_two_nodes_k_two(self):
        """测试边界情况：两个节点且 k 为 2"""
        head = build_list([1, 2])
        result = self.solution.reverseKGroup(head, 2)
        self.assertEqual(list_to_values(result), [2, 1])

    def test_extreme_values(self):
        """测试边界情况：极端节点值"""
        head = build_list([0, 1000, 500])
        result = self.solution.reverseKGroup(head, 2)
        self.assertEqual(list_to_values(result), [1000, 0, 500])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestReverseKGroup.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
