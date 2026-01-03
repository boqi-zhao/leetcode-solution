"""
LeetCode 88. Merge Sorted Array 测试用例
"""

import unittest
from solution import Solution


class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        expected = [1, 2, 2, 3, 5, 6]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_example2(self):
        """测试示例 2"""
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        expected = [1]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_example3(self):
        """测试示例 3"""
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expected = [1]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_nums1_empty(self):
        """测试 nums1 为空的情况"""
        nums1 = [0, 0, 0]
        m = 0
        nums2 = [1, 2, 3]
        n = 3
        expected = [1, 2, 3]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_nums2_empty(self):
        """测试 nums2 为空的情况"""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = []
        n = 0
        expected = [1, 2, 3, 0, 0, 0]
        
        self.solution.merge(nums1, m, nums2, n)
        
        # 只检查前 m 个元素
        self.assertEqual(nums1[:m], expected[:m])

    def test_all_nums2_greater(self):
        """测试 nums2 所有元素都大于 nums1"""
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [4, 5, 6]
        n = 3
        expected = [1, 2, 3, 4, 5, 6]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_all_nums2_smaller(self):
        """测试 nums2 所有元素都小于 nums1"""
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        expected = [1, 2, 3, 4, 5, 6]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_interleaved(self):
        """测试交错合并"""
        nums1 = [1, 3, 5, 0, 0, 0]
        m = 3
        nums2 = [2, 4, 6]
        n = 3
        expected = [1, 2, 3, 4, 5, 6]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_duplicate_values(self):
        """测试包含重复值"""
        nums1 = [1, 2, 2, 0, 0, 0]
        m = 3
        nums2 = [2, 3, 3]
        n = 3
        expected = [1, 2, 2, 2, 3, 3]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_single_element_each(self):
        """测试每个数组只有一个元素"""
        nums1 = [2, 0]
        m = 1
        nums2 = [1]
        n = 1
        expected = [1, 2]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_negative_numbers(self):
        """测试包含负数"""
        nums1 = [-1, 0, 0, 0]
        m = 1
        nums2 = [-2, -1, 2]
        n = 3
        expected = [-2, -1, -1, 2]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_large_numbers(self):
        """测试大数字"""
        nums1 = [1, 3, 5, 0, 0]
        m = 3
        nums2 = [2, 4]
        n = 2
        expected = [1, 2, 3, 4, 5]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_nums1_larger(self):
        """测试 nums1 比 nums2 大很多"""
        nums1 = [1, 2, 3, 4, 5, 0, 0]
        m = 5
        nums2 = [6, 7]
        n = 2
        expected = [1, 2, 3, 4, 5, 6, 7]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)

    def test_nums2_larger(self):
        """测试 nums2 比 nums1 大很多"""
        nums1 = [1, 2, 0, 0, 0, 0, 0]
        m = 2
        nums2 = [3, 4, 5, 6, 7]
        n = 5
        expected = [1, 2, 3, 4, 5, 6, 7]
        
        self.solution.merge(nums1, m, nums2, n)
        
        self.assertEqual(nums1, expected)


if __name__ == '__main__':
    import sys
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMergeSortedArray.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)

