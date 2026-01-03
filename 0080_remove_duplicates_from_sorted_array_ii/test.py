"""
LeetCode 80. Remove Duplicates from Sorted Array II 测试用例
"""

import unittest
from solution import Solution


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 1, 1, 2, 2, 3]
        expected_length = 5
        expected_nums = [1, 1, 2, 2, 3]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_example2(self):
        """测试示例 2"""
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected_length = 7
        expected_nums = [0, 0, 1, 1, 2, 3, 3]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_empty_array(self):
        """测试空数组"""
        nums = []
        expected_length = 0
        expected_nums = []
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_single_element(self):
        """测试单个元素"""
        nums = [1]
        expected_length = 1
        expected_nums = [1]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_two_elements_same(self):
        """测试两个相同元素"""
        nums = [1, 1]
        expected_length = 2
        expected_nums = [1, 1]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_two_elements_different(self):
        """测试两个不同元素"""
        nums = [1, 2]
        expected_length = 2
        expected_nums = [1, 2]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_all_same_more_than_two(self):
        """测试所有元素相同且超过两个"""
        nums = [2, 2, 2, 2, 2]
        expected_length = 2
        expected_nums = [2, 2]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_no_duplicates(self):
        """测试没有重复元素"""
        nums = [1, 2, 3, 4, 5]
        expected_length = 5
        expected_nums = [1, 2, 3, 4, 5]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_exactly_two_duplicates(self):
        """测试每个元素恰好出现两次"""
        nums = [1, 1, 2, 2, 3, 3]
        expected_length = 6
        expected_nums = [1, 1, 2, 2, 3, 3]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_mixed_duplicates(self):
        """测试混合重复情况"""
        nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 4]
        expected_length = 7
        expected_nums = [1, 1, 2, 2, 3, 3, 4]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_negative_numbers(self):
        """测试负数"""
        nums = [-1, -1, -1, 0, 0, 1, 1, 1]
        expected_length = 6
        expected_nums = [-1, -1, 0, 0, 1, 1]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_single_duplicate_group(self):
        """测试只有一个重复组超过两次"""
        nums = [1, 1, 1, 1, 1]
        expected_length = 2
        expected_nums = [1, 1]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)


if __name__ == '__main__':
    import sys
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestRemoveDuplicates.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)

