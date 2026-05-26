"""
LeetCode 0011. 盛最多水的容器 测试用例
"""

import unittest
from solution import Solution


class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.solution.maxArea(height), 49)

    def test_example2(self):
        """测试示例 2"""
        height = [1, 1]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_minimum_length(self):
        """测试最小长度（2个元素）"""
        height = [1, 2]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_symmetric_heights(self):
        """测试两端等高"""
        height = [4, 3, 2, 1, 4]
        self.assertEqual(self.solution.maxArea(height), 16)

    def test_increasing_heights(self):
        """测试递增高度"""
        height = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxArea(height), 6)

    def test_decreasing_heights(self):
        """测试递减高度"""
        height = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.maxArea(height), 6)

    def test_all_same_height(self):
        """测试所有高度相同"""
        height = [2, 2, 2, 2]
        self.assertEqual(self.solution.maxArea(height), 6)

    def test_one_tall_bar(self):
        """测试中间有高柱"""
        height = [1, 10000, 1, 1, 1]
        self.assertEqual(self.solution.maxArea(height), 4)

    def test_max_height_value(self):
        """测试最大高度值"""
        height = [10000, 10000]
        self.assertEqual(self.solution.maxArea(height), 10000)

    def test_one_side_tall(self):
        """测试一侧极高"""
        height = [10000, 1]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_complex_case(self):
        """测试复杂情况"""
        height = [2, 3, 4, 5, 18, 17, 6]
        self.assertEqual(self.solution.maxArea(height), 17)


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestMaxArea.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
