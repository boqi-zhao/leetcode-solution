"""
LeetCode 0024. 两两交换链表中的节点 测试用例
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


class TestSwapPairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        head = build_list([1, 2, 3, 4])
        result = self.solution.swapPairs(head)
        self.assertEqual(list_to_values(result), [2, 1, 4, 3])

    def test_example2(self):
        """测试示例 2：空链表"""
        head = build_list([])
        result = self.solution.swapPairs(head)
        self.assertIsNone(result)
        self.assertEqual(list_to_values(result), [])

    def test_example3(self):
        """测试示例 3：单个节点"""
        head = build_list([1])
        result = self.solution.swapPairs(head)
        self.assertEqual(list_to_values(result), [1])

    def test_two_nodes(self):
        """测试边界情况：两个节点"""
        head = build_list([1, 2])
        result = self.solution.swapPairs(head)
        self.assertEqual(list_to_values(result), [2, 1])

    def test_odd_length(self):
        """测试边界情况：奇数个节点"""
        head = build_list([1, 2, 3])
        result = self.solution.swapPairs(head)
        self.assertEqual(list_to_values(result), [2, 1, 3])

    def test_five_nodes(self):
        """测试边界情况：五个节点"""
        head = build_list([1, 2, 3, 4, 5])
        result = self.solution.swapPairs(head)
        self.assertEqual(list_to_values(result), [2, 1, 4, 3, 5])

    def test_extreme_values(self):
        """测试边界情况：极端节点值"""
        head = build_list([0, 100])
        result = self.solution.swapPairs(head)
        self.assertEqual(list_to_values(result), [100, 0])

    def test_all_same_values(self):
        """测试边界情况：节点值相同"""
        head = build_list([5, 5, 5, 5])
        result = self.solution.swapPairs(head)
        self.assertEqual(list_to_values(result), [5, 5, 5, 5])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestSwapPairs.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
