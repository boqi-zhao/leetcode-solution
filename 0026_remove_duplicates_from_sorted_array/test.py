"""
LeetCode 26. Remove Duplicates from Sorted Array 测试用例
"""

import unittest
from solution import Solution


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 1, 2]
        expected_length = 2
        expected_nums = [1, 2]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_example2(self):
        """测试示例 2"""
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_length = 5
        expected_nums = [0, 1, 2, 3, 4]
        
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

    def test_no_duplicates(self):
        """测试无重复元素"""
        nums = [1, 2, 3, 4, 5]
        expected_length = 5
        expected_nums = [1, 2, 3, 4, 5]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_all_duplicates(self):
        """测试所有元素都相同"""
        nums = [1, 1, 1, 1, 1]
        expected_length = 1
        expected_nums = [1]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_negative_numbers(self):
        """测试负数"""
        nums = [-1, -1, 0, 0, 1, 1]
        expected_length = 3
        expected_nums = [-1, 0, 1]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_two_elements_same(self):
        """测试两个相同元素"""
        nums = [1, 1]
        expected_length = 1
        expected_nums = [1]
        
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

    def test_long_array(self):
        """测试长数组"""
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
        expected_length = 10
        expected_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)

    def test_zeros(self):
        """测试包含零"""
        nums = [0, 0, 0, 1, 1, 2, 2]
        expected_length = 3
        expected_nums = [0, 1, 2]
        
        result = self.solution.removeDuplicates(nums)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], expected_nums)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestRemoveDuplicates.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)

