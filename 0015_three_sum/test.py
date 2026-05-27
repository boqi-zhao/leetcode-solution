"""
LeetCode 0015. 三数之和 测试用例
"""

import unittest
from solution import Solution


def normalize_triplets(triplets):
    """将三元组列表标准化：每个三元组内部排序，整体再排序"""
    return sorted([sorted(t) for t in triplets])


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [-1, 0, 1, 2, -1, -4]
        result = self.solution.threeSum(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(normalize_triplets(result), normalize_triplets(expected))

    def test_example2(self):
        """测试示例 2"""
        nums = [0, 1, 1]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

    def test_example3(self):
        """测试示例 3"""
        nums = [0, 0, 0]
        result = self.solution.threeSum(nums)
        expected = [[0, 0, 0]]
        self.assertEqual(normalize_triplets(result), normalize_triplets(expected))

    def test_edge_case_no_solution(self):
        """测试边界情况 - 无解"""
        nums = [1, 2, 3]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, [])

    def test_edge_case_all_zeros(self):
        """测试边界情况 - 多个零"""
        nums = [0, 0, 0, 0]
        result = self.solution.threeSum(nums)
        expected = [[0, 0, 0]]
        self.assertEqual(normalize_triplets(result), normalize_triplets(expected))

    def test_edge_case_duplicates(self):
        """测试边界情况 - 含重复元素"""
        nums = [-1, -1, 0, 1, 1]
        result = self.solution.threeSum(nums)
        expected = [[-1, 0, 1]]
        self.assertEqual(normalize_triplets(result), normalize_triplets(expected))

    def test_edge_case_negative_positive_mix(self):
        """测试边界情况 - 正负数混合"""
        nums = [-2, 0, 1, 1, 2]
        result = self.solution.threeSum(nums)
        expected = [[-2, 0, 2], [-2, 1, 1]]
        self.assertEqual(normalize_triplets(result), normalize_triplets(expected))

    def test_edge_case_large_duplicates(self):
        """测试边界情况 - 大量重复值"""
        nums = [-1, -1, -1, 2, 2, 2, 0]
        result = self.solution.threeSum(nums)
        expected = [[-1, -1, 2]]
        self.assertEqual(normalize_triplets(result), normalize_triplets(expected))


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestThreeSum.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
