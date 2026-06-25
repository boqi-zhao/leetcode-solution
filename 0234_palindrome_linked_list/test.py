"""
LeetCode 0234. 回文链表 测试用例
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


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        head = build_list([1, 2, 2, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_example2(self):
        """测试示例 2"""
        head = build_list([1, 2])
        self.assertFalse(self.solution.isPalindrome(head))

    def test_single_node(self):
        """测试边界情况：单个节点"""
        head = build_list([5])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_odd_length_palindrome(self):
        """测试边界情况：奇数长度回文链表"""
        head = build_list([1, 2, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_all_same_values(self):
        """测试边界情况：所有节点值相同"""
        head = build_list([1, 1, 1, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_not_palindrome_odd_length(self):
        """测试边界情况：奇数长度非回文链表"""
        head = build_list([1, 2, 3])
        self.assertFalse(self.solution.isPalindrome(head))

    def test_longer_palindrome(self):
        """测试边界情况：较长回文链表"""
        head = build_list([1, 2, 3, 2, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_extreme_values(self):
        """测试边界情况：极端节点值"""
        head = build_list([0, 9, 0])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_zero_values(self):
        """测试边界情况：包含 0 的回文链表"""
        head = build_list([0, 0])
        self.assertTrue(self.solution.isPalindrome(head))


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestIsPalindrome.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
