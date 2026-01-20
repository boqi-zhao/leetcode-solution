"""
LeetCode 0049. 字母异位词分组 测试用例
"""

import unittest
from solution import Solution


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = self.solution.groupAnagrams(strs)
        # 对结果进行标准化处理：每个子列表排序，然后整个结果排序
        normalized_result = sorted([sorted(group) for group in result])
        expected = sorted([sorted(group) for group in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]])
        self.assertEqual(normalized_result, expected)

    def test_example2(self):
        """测试示例 2 - 空字符串"""
        strs = [""]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [[""]])

    def test_example3(self):
        """测试示例 3 - 单个字符"""
        strs = ["a"]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [["a"]])

    def test_edge_case_empty_array(self):
        """测试边界情况 - 空数组"""
        strs = []
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [])

    def test_edge_case_single_group(self):
        """测试边界情况 - 所有字符串都是异位词"""
        strs = ["abc", "bca", "cab"]
        result = self.solution.groupAnagrams(strs)
        normalized_result = sorted([sorted(group) for group in result])
        expected = sorted([sorted(["abc", "bca", "cab"])])
        self.assertEqual(normalized_result, expected)

    def test_edge_case_no_anagrams(self):
        """测试边界情况 - 没有异位词，每个字符串独立一组"""
        strs = ["abc", "def", "ghi"]
        result = self.solution.groupAnagrams(strs)
        normalized_result = sorted([sorted(group) for group in result])
        expected = sorted([sorted(["abc"]), sorted(["def"]), sorted(["ghi"])])
        self.assertEqual(normalized_result, expected)

    def test_edge_case_multiple_groups(self):
        """测试边界情况 - 多个不同的异位词组"""
        strs = ["abc", "bca", "cab", "def", "fed", "xyz"]
        result = self.solution.groupAnagrams(strs)
        normalized_result = sorted([sorted(group) for group in result])
        expected = sorted([
            sorted(["abc", "bca", "cab"]),
            sorted(["def", "fed"]),
            sorted(["xyz"])
        ])
        self.assertEqual(normalized_result, expected)

    def test_edge_case_long_strings(self):
        """测试边界情况 - 较长的字符串"""
        strs = ["listen", "silent", "enlist"]
        result = self.solution.groupAnagrams(strs)
        normalized_result = sorted([sorted(group) for group in result])
        expected = sorted([sorted(["listen", "silent", "enlist"])])
        self.assertEqual(normalized_result, expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestGroupAnagrams.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
