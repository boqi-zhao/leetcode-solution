"""
LeetCode 0018. 四数之和 测试用例
"""

import unittest
from solution import Solution


def normalize_quadruplets(quadruplets):
    """将四元组列表标准化：每个四元组内部排序，整体再排序"""
    return sorted([sorted(q) for q in quadruplets])


class TestFourSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        result = self.solution.fourSum(nums, target)
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertEqual(normalize_quadruplets(result), normalize_quadruplets(expected))

    def test_example2(self):
        """测试示例 2"""
        nums = [2, 2, 2, 2, 2]
        target = 8
        result = self.solution.fourSum(nums, target)
        expected = [[2, 2, 2, 2]]
        self.assertEqual(normalize_quadruplets(result), normalize_quadruplets(expected))

    def test_edge_case_no_solution(self):
        """测试边界情况 - 无解"""
        nums = [1, 2, 3, 4]
        target = 100
        result = self.solution.fourSum(nums, target)
        self.assertEqual(result, [])

    def test_edge_case_less_than_four_elements(self):
        """测试边界情况 - 元素不足四个"""
        nums = [1, 2, 3]
        target = 6
        result = self.solution.fourSum(nums, target)
        self.assertEqual(result, [])

    def test_edge_case_single_element(self):
        """测试边界情况 - 单个元素"""
        nums = [1]
        target = 1
        result = self.solution.fourSum(nums, target)
        self.assertEqual(result, [])

    def test_edge_case_negative_target(self):
        """测试边界情况 - 负目标值"""
        nums = [-2, -1, 0, 1, 2]
        target = -5
        result = self.solution.fourSum(nums, target)
        self.assertEqual(result, [])

    def test_edge_case_all_zeros(self):
        """测试边界情况 - 全零"""
        nums = [0, 0, 0, 0]
        target = 0
        result = self.solution.fourSum(nums, target)
        expected = [[0, 0, 0, 0]]
        self.assertEqual(normalize_quadruplets(result), normalize_quadruplets(expected))

    def test_edge_case_duplicates(self):
        """测试边界情况 - 含重复元素"""
        nums = [1, 0, -1, 0, -2, 2, -1, -2]
        target = 0
        result = self.solution.fourSum(nums, target)
        expected = [
            [-2, -1, 1, 2],
            [-2, 0, 0, 2],
            [-1, -1, 0, 2],
            [-1, 0, 0, 1],
        ]
        self.assertEqual(normalize_quadruplets(result), normalize_quadruplets(expected))

    def test_edge_case_exact_four_elements(self):
        """测试边界情况 - 恰好四个元素"""
        nums = [2, 2, 2, 2]
        target = 8
        result = self.solution.fourSum(nums, target)
        expected = [[2, 2, 2, 2]]
        self.assertEqual(normalize_quadruplets(result), normalize_quadruplets(expected))


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestFourSum.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
