"""
LeetCode 0206. 反转链表 测试用例
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


class TestReverseList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        head = build_list([1, 2, 3, 4, 5])
        result = self.solution.reverseList(head)
        self.assertEqual(list_to_values(result), [5, 4, 3, 2, 1])

    def test_example2(self):
        """测试示例 2"""
        head = build_list([1, 2])
        result = self.solution.reverseList(head)
        self.assertEqual(list_to_values(result), [2, 1])

    def test_example3(self):
        """测试示例 3：空链表"""
        head = build_list([])
        result = self.solution.reverseList(head)
        self.assertIsNone(result)
        self.assertEqual(list_to_values(result), [])

    def test_single_node(self):
        """测试边界情况：单个节点"""
        head = build_list([42])
        result = self.solution.reverseList(head)
        self.assertEqual(list_to_values(result), [42])

    def test_negative_values(self):
        """测试边界情况：包含负值"""
        head = build_list([-1, 0, 1])
        result = self.solution.reverseList(head)
        self.assertEqual(list_to_values(result), [1, 0, -1])

    def test_extreme_values(self):
        """测试边界情况：极端节点值"""
        head = build_list([-5000, 5000])
        result = self.solution.reverseList(head)
        self.assertEqual(list_to_values(result), [5000, -5000])

    def test_duplicate_values(self):
        """测试边界情况：节点值重复"""
        head = build_list([1, 1, 2, 2])
        result = self.solution.reverseList(head)
        self.assertEqual(list_to_values(result), [2, 2, 1, 1])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestReverseList.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
