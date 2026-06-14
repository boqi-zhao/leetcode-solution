"""
LeetCode 0003. 无重复字符的最长子串 测试用例
"""

import unittest
from solution import Solution


class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        s = "abcabcbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

    def test_example2(self):
        """测试示例 2"""
        s = "bbbbb"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)

    def test_example3(self):
        """测试示例 3"""
        s = "pwwkew"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

    def test_empty_string(self):
        """测试空字符串"""
        s = ""
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 0)

    def test_single_character(self):
        """测试单个字符"""
        s = "a"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)

    def test_all_unique_characters(self):
        """测试全部字符不重复"""
        s = "abcdef"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 6)

    def test_symbols_and_spaces(self):
        """测试包含符号和空格"""
        s = "abc def"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 7)

    def test_alternating_characters(self):
        """测试交替重复字符"""
        s = "abba"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 2)

    def test_long_unique_suffix(self):
        """测试末尾存在较长无重复子串"""
        s = "dvdf"
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestLengthOfLongestSubstring.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
