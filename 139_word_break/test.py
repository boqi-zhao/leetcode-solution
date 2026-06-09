"""
LeetCode 139. 单词拆分 测试用例
"""

import unittest
from solution import Solution


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        s = "leetcode"
        wordDict = ["leet", "code"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def test_example2(self):
        """测试示例 2"""
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def test_example3(self):
        """测试示例 3"""
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertFalse(result)

    def test_edge_case_single_char(self):
        """测试边界情况 - 单字符完全匹配"""
        s = "a"
        wordDict = ["a"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def test_edge_case_single_char_no_match(self):
        """测试边界情况 - 单字符无法匹配"""
        s = "a"
        wordDict = ["b"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertFalse(result)

    def test_edge_case_exact_one_word(self):
        """测试边界情况 - 整个字符串恰好是一个单词"""
        s = "hello"
        wordDict = ["hello", "world"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def test_edge_case_reuse_word(self):
        """测试边界情况 - 重复使用同一单词"""
        s = "aaaa"
        wordDict = ["aa"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def test_edge_case_prefix_trap(self):
        """测试边界情况 - 前缀陷阱（贪心会失败）"""
        s = "cars"
        wordDict = ["car", "ca", "rs"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def test_edge_case_multiple_words_split(self):
        """测试边界情况 - 多种单词组合可拼接"""
        s = "abcd"
        wordDict = ["a", "abc", "b", "cd"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)

    def test_edge_case_impossible(self):
        """测试边界情况 - 完全无法拼接"""
        s = "abcd"
        wordDict = ["e", "f"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertFalse(result)

    def test_edge_case_overlapping_words(self):
        """测试边界情况 - 多种拆分方式"""
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        result = self.solution.wordBreak(s, wordDict)
        self.assertTrue(result)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestWordBreak.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
