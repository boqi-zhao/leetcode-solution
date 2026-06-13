"""
LeetCode 32. 最长有效括号 测试用例
"""

import unittest
from solution import Solution


class TestLongestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        s = "(()"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 2)

    def test_example2(self):
        """测试示例 2"""
        s = ")()())"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 4)

    def test_example3(self):
        """测试示例 3"""
        s = ""
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 0)

    def test_edge_case_single_left_paren(self):
        """测试边界情况 - 单个左括号"""
        s = "("
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 0)

    def test_edge_case_single_right_paren(self):
        """测试边界情况 - 单个右括号"""
        s = ")"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 0)

    def test_edge_case_valid_pair(self):
        """测试边界情况 - 完整有效括号对"""
        s = "()"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 2)

    def test_edge_case_nested_valid(self):
        """测试边界情况 - 嵌套有效括号"""
        s = "(())"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 4)

    def test_edge_case_all_left_parens(self):
        """测试边界情况 - 全是左括号"""
        s = "((("
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 0)

    def test_edge_case_all_right_parens(self):
        """测试边界情况 - 全是右括号"""
        s = ")))"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 0)

    def test_edge_case_fully_valid(self):
        """测试边界情况 - 整个字符串有效"""
        s = "()(())"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 6)

    def test_edge_case_deeply_nested(self):
        """测试边界情况 - 深度嵌套且完全有效"""
        s = "((()))"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 6)

    def test_edge_case_reversed_parens(self):
        """测试边界情况 - 右括号在前"""
        s = ")("
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 0)

    def test_edge_case_trailing_invalid(self):
        """测试边界情况 - 末尾多余右括号"""
        s = "())"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 2)

    def test_edge_case_valid_prefix_only(self):
        """测试边界情况 - 仅前缀有效"""
        s = "()(()"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 2)

    def test_edge_case_leading_invalid(self):
        """测试边界情况 - 开头无效右括号"""
        s = ")()()("
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 4)

    def test_edge_case_continuous_valid(self):
        """测试边界情况 - 连续有效括号"""
        s = "(()())"
        result = self.solution.longestValidParentheses(s)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestLongestValidParentheses.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
