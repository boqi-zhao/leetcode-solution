# LeetCode 题目代码生成规则

当你需要为新的 LeetCode 题目生成代码时，请按照以下规则创建三个文件：

## 文件结构

每个题目需要创建独立的文件夹，命名格式：`题目编号_题目英文名（下划线分隔）`

文件夹内包含三个文件：
1. `solution.py` - 解决方案实现
2. `test.py` - 测试用例（unittest）
3. `debug.py` - 调试脚本

## 1. solution.py 格式

```python
"""
LeetCode [题目编号]. [题目中文名] ([题目英文名])

题目描述：
[完整的题目描述，包括所有要求、约束和说明]

示例 1：
输入：[示例输入]
输出：[示例输出]
解释：[示例解释]

示例 2：
输入：[示例输入]
输出：[示例输出]
解释：[示例解释]

提示：
- [提示1]
- [提示2]
- [提示3]
"""


class Solution(object):
    def methodName(self, param1, param2):
        """
        :type param1: List[int]
        :type param2: int
        :rtype: int
        """
        # 实现代码
        pass
```

**要求**：
- 文件开头包含完整的题目描述（中文）
- 包含所有示例和提示
- Solution 类的方法要有完整的类型注解（:type 和 :rtype）
- 方法签名要与 LeetCode 官方格式一致
- **重要**：方法体内只保留 `pass`，不要实现具体代码，让用户自己实现解决方案

## 2. test.py 格式

```python
"""
LeetCode [题目编号]. [题目中文名] 测试用例
"""

import unittest
from solution import Solution


class TestClassName(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """测试示例 1"""
        # 测试代码
        pass

    def test_example2(self):
        """测试示例 2"""
        # 测试代码
        pass

    def test_edge_case1(self):
        """测试边界情况1"""
        # 测试代码
        pass

    # ... 更多测试用例


if __name__ == '__main__':
    # 支持命令行参数选择运行特定测试用例
    # 例如: python test.py TestClassName.test_example1
    # 或者: python test.py -k test_example1
    unittest.main(verbosity=2)
```

**要求**：
- 使用 unittest 框架
- 测试类命名：`Test` + 方法名（首字母大写，驼峰命名）
- 必须包含 `setUp` 方法创建 Solution 实例
- 每个测试方法都要有中文注释说明测试内容
- 至少包含所有示例的测试用例
- 包含边界情况测试（空数组、单个元素、极端值等）
- 测试断言要清晰明确

## 3. debug.py 格式

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
调试脚本 - 可以单独运行和调试单个测试用例
使用方法：
1. 直接在 IDE 中运行此文件（可以打断点）
2. 或者命令行运行：python debug.py
3. 修改下面的 test_case 变量来选择要调试的测试用例
"""

from solution import Solution


def test_example1():
    """测试示例 1"""
    solution = Solution()
    # 输入数据
    param1 = [...]
    param2 = ...
    expected = ...
    
    # 在这里打断点调试
    result = solution.methodName(param1, param2)
    
    print(f"输入: param1 = {[...]}, param2 = {param2}")
    print(f"输出: result = {result}")
    print(f"期望: {expected}")
    print(f"结果: {'✅ 通过' if result == expected else '❌ 失败'}")


def test_example2():
    """测试示例 2"""
    solution = Solution()
    # ... 类似结构
    pass


def test_custom():
    """自定义测试 - 在这里添加你自己的测试用例"""
    solution = Solution()
    # ... 自定义测试数据
    pass


# 选择要运行的测试用例（修改这里来选择不同的测试）
if __name__ == '__main__':
    # 取消注释你想要运行的测试用例
    
    test_example1()      # 运行示例 1
    # test_example2()    # 运行示例 2
    # test_custom()      # 运行自定义测试
```

**要求**：
- 文件开头包含 shebang 和编码声明
- 包含使用说明注释
- 每个测试函数都要有中文注释
- 包含详细的打印输出，显示输入、输出、期望值和结果
- 在 `if __name__ == '__main__'` 中通过注释/取消注释来选择运行的测试
- 支持在 IDE 中打断点调试

## 代码风格要求

1. **注释**：所有注释使用中文
2. **命名**：
   - 类名：驼峰命名（如 `Solution`, `TestRemoveDuplicates`）
   - 方法名：驼峰命名（如 `removeDuplicates`, `test_example1`）
   - 变量名：小写下划线（如 `nums`, `expected_length`）
3. **类型注解**：使用 LeetCode 标准格式（`:type` 和 `:rtype`）
4. **测试覆盖**：确保覆盖所有示例和常见边界情况

## 生成流程

当用户提供题目信息时：
1. 创建题目文件夹（格式：`题目编号_题目英文名`）
2. 生成 `solution.py`（包含完整题目描述和 Solution 类模板，方法体内只保留 `pass`）
3. 生成 `test.py`（包含所有示例测试和边界情况测试）
4. 生成 `debug.py`（包含调试脚本，支持断点调试）

**重要原则**：
- **不要实现 solution.py 中的具体代码**，只保留方法签名和 `pass`
- 可以临时实现代码来验证测试用例的正确性，但验证完成后必须删除实现，只保留 `pass`
- 让用户自己实现解决方案，这是练习的核心目的
- 测试用例和调试脚本要完整且正确，确保用户实现后可以验证

## 注意事项

- **核心原则**：不要实现 `solution.py` 中的代码，只保留方法签名和 `pass`，让用户自己实现
- 可以临时实现代码来验证测试用例的正确性，但验证完成后必须删除实现代码
- 确保所有文件都可以独立运行（solution.py 有 pass 即可，不会报错）
- 测试用例要全面，包括边界情况，且必须经过验证确保正确
- 调试脚本要方便在 IDE 中使用
- 代码要符合 Python 编码规范
- 所有输出和注释使用中文

