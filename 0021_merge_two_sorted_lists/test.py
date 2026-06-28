"""
LeetCode 0021. 合并两个有序链表 测试用例
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


class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        l1 = build_list([1, 2, 4])
        l2 = build_list([1, 3, 4])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(list_to_values(result), [1, 1, 2, 3, 4, 4])

    def test_example2(self):
        """测试示例 2：两个空链表"""
        l1 = build_list([])
        l2 = build_list([])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertIsNone(result)
        self.assertEqual(list_to_values(result), [])

    def test_example3(self):
        """测试示例 3：一个空链表"""
        l1 = build_list([])
        l2 = build_list([0])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(list_to_values(result), [0])

    def test_one_empty_list(self):
        """测试边界情况：l2 为空"""
        l1 = build_list([1, 2, 3])
        l2 = build_list([])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(list_to_values(result), [1, 2, 3])

    def test_single_node_each(self):
        """测试边界情况：两个链表各一个节点"""
        l1 = build_list([2])
        l2 = build_list([1])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(list_to_values(result), [1, 2])

    def test_negative_values(self):
        """测试边界情况：包含负值"""
        l1 = build_list([-3, -1, 0])
        l2 = build_list([-2, 1])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(list_to_values(result), [-3, -2, -1, 0, 1])

    def test_extreme_values(self):
        """测试边界情况：极端节点值"""
        l1 = build_list([-100])
        l2 = build_list([100])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(list_to_values(result), [-100, 100])

    def test_l1_longer(self):
        """测试边界情况：l1 比 l2 长"""
        l1 = build_list([1, 2, 3, 4, 5])
        l2 = build_list([2, 4])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(list_to_values(result), [1, 2, 2, 3, 4, 4, 5])

    def test_duplicate_values(self):
        """测试边界情况：节点值重复"""
        l1 = build_list([1, 1, 1])
        l2 = build_list([1, 1])
        result = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(list_to_values(result), [1, 1, 1, 1, 1])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMergeTwoLists.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
