"""
LeetCode 0001. 两数之和 测试用例
"""

import unittest
from solution import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        # 结果可能是 [0,1] 或 [1,0]，都算正确
        self.assertIn(result, [[0, 1], [1, 0]])
        # 验证结果正确性
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_example2(self):
        """测试示例 2"""
        nums = [3, 2, 4]
        target = 6
        result = self.solution.twoSum(nums, target)
        # 结果可能是 [1,2] 或 [2,1]，都算正确
        self.assertIn(result, [[1, 2], [2, 1]])
        # 验证结果正确性
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_example3(self):
        """测试示例 3"""
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        # 结果可能是 [0,1] 或 [1,0]，都算正确
        self.assertIn(result, [[0, 1], [1, 0]])
        # 验证结果正确性
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_minimum_length(self):
        """测试最小长度（2个元素）"""
        nums = [1, 2]
        target = 3
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[0, 1], [1, 0]])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_negative_numbers(self):
        """测试负数"""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[2, 4], [4, 2]])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_mixed_positive_negative(self):
        """测试正负数混合"""
        nums = [-1, 0, 1, 2, 3]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[0, 2], [2, 0]])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_zero_in_array(self):
        """测试数组中包含0"""
        nums = [0, 4, 3, 0]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[0, 3], [3, 0]])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_duplicate_values(self):
        """测试重复值（但不是答案）"""
        nums = [1, 1, 2, 3]
        target = 5
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[2, 3], [3, 2]])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_large_numbers(self):
        """测试大数"""
        nums = [1000000000, 2000000000, 3000000000]
        target = 5000000000
        result = self.solution.twoSum(nums, target)
        self.assertIn(result, [[1, 2], [2, 1]])
        self.assertEqual(nums[result[0]] + nums[result[1]], target)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestTwoSum.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
