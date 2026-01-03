"""
LeetCode 27. Remove Element 测试用例
"""

import unittest
from solution import Solution


class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [3, 2, 2, 3]
        val = 3
        expected_length = 2
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        # 检查前 result 个元素不包含 val
        self.assertNotIn(val, nums[:result])

    def test_example2(self):
        """测试示例 2"""
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_length = 5
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        # 检查前 result 个元素不包含 val
        self.assertNotIn(val, nums[:result])

    def test_empty_array(self):
        """测试空数组"""
        nums = []
        val = 1
        expected_length = 0
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)

    def test_no_target_value(self):
        """测试数组中不包含目标值"""
        nums = [1, 2, 3, 4, 5]
        val = 6
        expected_length = 5
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], [1, 2, 3, 4, 5])

    def test_all_same_value(self):
        """测试所有元素都是目标值"""
        nums = [3, 3, 3, 3]
        val = 3
        expected_length = 0
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        self.assertNotIn(val, nums[:result])

    def test_single_element_match(self):
        """测试单个元素且匹配"""
        nums = [1]
        val = 1
        expected_length = 0
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)

    def test_single_element_no_match(self):
        """测试单个元素但不匹配"""
        nums = [1]
        val = 2
        expected_length = 1
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        self.assertEqual(nums[:result], [1])

    def test_val_at_beginning(self):
        """测试目标值在开头"""
        nums = [1, 2, 3, 4, 5]
        val = 1
        expected_length = 4
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        self.assertNotIn(val, nums[:result])

    def test_val_at_end(self):
        """测试目标值在末尾"""
        nums = [1, 2, 3, 4, 5]
        val = 5
        expected_length = 4
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        self.assertNotIn(val, nums[:result])

    def test_val_in_middle(self):
        """测试目标值在中间"""
        nums = [1, 2, 3, 4, 5]
        val = 3
        expected_length = 4
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        self.assertNotIn(val, nums[:result])

    def test_multiple_occurrences(self):
        """测试多个目标值"""
        nums = [1, 2, 2, 2, 3, 4, 2, 5]
        val = 2
        expected_length = 4
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        self.assertNotIn(val, nums[:result])

    def test_zero_value(self):
        """测试目标值为 0"""
        nums = [0, 1, 0, 3, 12]
        val = 0
        expected_length = 3
        
        result = self.solution.removeElement(nums, val)
        
        self.assertEqual(result, expected_length)
        self.assertNotIn(val, nums[:result])


if __name__ == '__main__':
    unittest.main()

