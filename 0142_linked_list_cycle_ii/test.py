"""
LeetCode 0142. 环形链表 II 测试用例
"""

import unittest
from solution import Solution, ListNode


def build_cycled_list(values, pos):
    """根据列表和 pos 构建带环或不带环的单链表，返回 (head, nodes)"""
    if not values:
        return None, []
    nodes = [ListNode(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0], nodes


class TestDetectCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        head, nodes = build_cycled_list([3, 2, 0, -4], 1)
        result = self.solution.detectCycle(head)
        self.assertIs(result, nodes[1])

    def test_example2(self):
        """测试示例 2"""
        head, nodes = build_cycled_list([1, 2], 0)
        result = self.solution.detectCycle(head)
        self.assertIs(result, nodes[0])

    def test_example3(self):
        """测试示例 3"""
        head, _ = build_cycled_list([1], -1)
        result = self.solution.detectCycle(head)
        self.assertIsNone(result)

    def test_empty_list(self):
        """测试边界情况：空链表"""
        head, _ = build_cycled_list([], -1)
        result = self.solution.detectCycle(head)
        self.assertIsNone(result)

    def test_two_nodes_no_cycle(self):
        """测试边界情况：两个节点无环"""
        head, _ = build_cycled_list([1, 2], -1)
        result = self.solution.detectCycle(head)
        self.assertIsNone(result)

    def test_single_node_with_cycle(self):
        """测试边界情况：单节点自环"""
        head, nodes = build_cycled_list([1], 0)
        result = self.solution.detectCycle(head)
        self.assertIs(result, nodes[0])

    def test_cycle_at_tail(self):
        """测试边界情况：尾节点指向自身"""
        head, nodes = build_cycled_list([1, 2, 3], 2)
        result = self.solution.detectCycle(head)
        self.assertIs(result, nodes[2])

    def test_extreme_values(self):
        """测试边界情况：极端节点值且无环"""
        head, _ = build_cycled_list([-100000, 100000], -1)
        result = self.solution.detectCycle(head)
        self.assertIsNone(result)

    def test_long_list_with_cycle(self):
        """测试边界情况：较长链表带环"""
        values = list(range(100))
        head, nodes = build_cycled_list(values, 50)
        result = self.solution.detectCycle(head)
        self.assertIs(result, nodes[50])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestDetectCycle.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
