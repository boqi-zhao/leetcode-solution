"""
LeetCode 0438. 找到字符串中所有字母异位词 测试用例
"""

import unittest
from solution import Solution


class TestFindAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        s = "cbaebabacd"
        p = "abc"
        self.assertEqual(sorted(self.solution.findAnagrams(s, p)), [0, 6])

    def test_example2(self):
        """测试示例 2"""
        s = "abab"
        p = "ab"
        self.assertEqual(sorted(self.solution.findAnagrams(s, p)), [0, 1, 2])

    def test_s_shorter_than_p(self):
        """测试 s 长度小于 p"""
        s = "a"
        p = "ab"
        self.assertEqual(self.solution.findAnagrams(s, p), [])

    def test_no_match(self):
        """测试不存在异位词"""
        s = "aaaa"
        p = "ab"
        self.assertEqual(self.solution.findAnagrams(s, p), [])

    def test_exact_match(self):
        """测试 s 与 p 完全相同"""
        s = "abc"
        p = "abc"
        self.assertEqual(self.solution.findAnagrams(s, p), [0])

    def test_single_character(self):
        """测试单字符匹配"""
        s = "aaa"
        p = "a"
        self.assertEqual(sorted(self.solution.findAnagrams(s, p)), [0, 1, 2])

    def test_same_length_no_match(self):
        """测试等长但字符不匹配"""
        s = "abc"
        p = "xyz"
        self.assertEqual(self.solution.findAnagrams(s, p), [])

    def test_repeated_pattern(self):
        """测试重复模式中的多个异位词"""
        s = "ababab"
        p = "aba"
        self.assertEqual(sorted(self.solution.findAnagrams(s, p)), [0, 2])


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestFindAnagrams.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
