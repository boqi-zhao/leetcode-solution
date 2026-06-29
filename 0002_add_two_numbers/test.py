"""
LeetCode 0002. 两数相加 测试用例
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


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        l1 = build_list([2, 4, 3])
        l2 = build_list([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_values(result), [7, 0, 8])

    def test_example2(self):
        """测试示例 2：两个零"""
        l1 = build_list([0])
        l2 = build_list([0])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_values(result), [0])

    def test_example3(self):
        """测试示例 3：进位链较长"""
        l1 = build_list([9, 9, 9, 9, 9, 9, 9])
        l2 = build_list([9, 9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_values(result), [8, 9, 9, 9, 0, 0, 0, 1])

    def test_single_digit_no_carry(self):
        """测试边界情况：个位相加无进位"""
        l1 = build_list([5])
        l2 = build_list([3])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_values(result), [8])

    def test_single_digit_with_carry(self):
        """测试边界情况：个位相加有进位"""
        l1 = build_list([5])
        l2 = build_list([7])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_values(result), [2, 1])

    def test_different_lengths_l1_longer(self):
        """测试边界情况：l1 比 l2 长"""
        l1 = build_list([1, 2, 3])
        l2 = build_list([4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_values(result), [5, 2, 3])

    def test_different_lengths_l2_longer(self):
        """测试边界情况：l2 比 l1 长"""
        l1 = build_list([1])
        l2 = build_list([2, 3, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_values(result), [3, 3, 4])

    def test_carry_at_end(self):
        """测试边界情况：末尾产生进位"""
        l1 = build_list([9, 9])
        l2 = build_list([1])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_values(result), [0, 0, 1])

    def test_all_nines(self):
        """测试边界情况：全 9 相加"""
        l1 = build_list([9, 9, 9])
        l2 = build_list([9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_values(result), [8, 9, 9, 1])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestAddTwoNumbers.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
