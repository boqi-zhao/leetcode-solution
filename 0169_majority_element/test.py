"""
LeetCode 169. 多数元素 测试用例
"""

import unittest
from solution import Solution


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [3, 2, 3]
        expected = 3
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, expected)

    def test_example2(self):
        """测试示例 2"""
        nums = [2, 2, 1, 1, 1, 2, 2]
        expected = 2
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, expected)

    def test_edge_case1(self):
        """测试边界情况 1：只有一个元素"""
        nums = [1]
        expected = 1
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, expected)

    def test_edge_case2(self):
        """测试边界情况 2：所有元素相同"""
        nums = [2, 2, 2, 2, 2]
        expected = 2
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, expected)

    def test_edge_case3(self):
        """测试边界情况 3：多数元素在数组前半部分"""
        nums = [3, 3, 3, 1, 2]
        expected = 3
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, expected)

    def test_edge_case4(self):
        """测试边界情况 4：多数元素在数组后半部分"""
        nums = [1, 2, 3, 3, 3]
        expected = 3
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, expected)

    def test_edge_case5(self):
        """测试边界情况 5：多数元素在数组中间"""
        nums = [1, 2, 2, 2, 3]
        expected = 2
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, expected)

    def test_edge_case6(self):
        """测试边界情况 6：包含负数"""
        nums = [-1, -1, -1, 2, 3]
        expected = -1
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, expected)

    def test_edge_case7(self):
        """测试边界情况 7：大数组"""
        nums = [1] * 25001 + [2] * 25000
        expected = 1
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMajorityElement.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)

