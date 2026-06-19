"""
LeetCode 0076. 最小覆盖子串 测试用例
"""

import unittest
from solution import Solution


class TestMinWindow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        s = "ADOBECODEBANC"
        t = "ABC"
        result = self.solution.minWindow(s, t)
        self.assertEqual(result, "BANC")

    def test_example2(self):
        """测试示例 2"""
        s = "a"
        t = "a"
        result = self.solution.minWindow(s, t)
        self.assertEqual(result, "a")

    def test_example3(self):
        """测试示例 3"""
        s = "a"
        t = "aa"
        result = self.solution.minWindow(s, t)
        self.assertEqual(result, "")

    def test_edge_case_entire_string(self):
        """测试边界情况 - 整个字符串即为答案"""
        s = "aab"
        t = "aab"
        result = self.solution.minWindow(s, t)
        self.assertEqual(result, "aab")

    def test_edge_case_duplicate_chars_in_t(self):
        """测试边界情况 - t 含重复字符"""
        s = "bbaac"
        t = "aba"
        result = self.solution.minWindow(s, t)
        self.assertEqual(result, "baa")

    def test_edge_case_no_valid_window(self):
        """测试边界情况 - s 中缺少 t 的字符"""
        s = "abc"
        t = "def"
        result = self.solution.minWindow(s, t)
        self.assertEqual(result, "")

    def test_edge_case_insufficient_count(self):
        """测试边界情况 - 字符存在但数量不足"""
        s = "ab"
        t = "aa"
        result = self.solution.minWindow(s, t)
        self.assertEqual(result, "")

    def test_edge_case_single_char_match(self):
        """测试边界情况 - 单字符多次出现取最短"""
        s = "bbbbb"
        t = "b"
        result = self.solution.minWindow(s, t)
        self.assertEqual(result, "b")

    def test_edge_case_t_at_end(self):
        """测试边界情况 - 最小窗口在末尾"""
        s = "bba"
        t = "ab"
        result = self.solution.minWindow(s, t)
        self.assertEqual(result, "ba")


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMinWindow.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
