"""
LeetCode 0049. 字母异位词分组 (Group Anagrams)

题目描述：
给你一个字符串数组 strs，请你将 字母异位词（anagrams）组合在一起。可以按任意顺序返回结果列表。

"字母异位词" 是指两个字符串包含的字母完全相同，只是顺序不同。

示例 1：
输入：strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出：[["bat"], ["nat","tan"], ["ate","eat","tea"]]
解释：
- "nat" 和 "tan" 是互为字母异位词；
- "ate"、"eat"、"tea" 是一组；
- "bat" 没有和它组成异位词的字符串，就自己一组。

示例 2：
输入：strs = [""]
输出：[[""]]

示例 3：
输入：strs = ["a"]
输出：[["a"]]

提示：
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] 均只包含小写英文字母 'a'-'z'
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        pass
