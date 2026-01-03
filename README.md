# leetcode-solution

LeetCode 题目解答集合

## 项目结构

每道题目一个独立文件夹，文件夹内包含：
- `solution.py` - 包含 `Solution` 类的实现
- `test.py` - 包含完整的测试用例（unittest）
- `debug.py` - 调试脚本，可以单独运行和调试单个测试用例

```
leetcode-solution/
├── 0026_remove_duplicates_from_sorted_array/
│   ├── solution.py    # Solution 类实现
│   ├── test.py        # 测试用例（unittest）
│   └── debug.py       # 调试脚本（支持断点调试）
├── 0027_remove_element/
│   ├── solution.py
│   ├── test.py
│   └── debug.py
├── 0088_merge_sorted_array/
│   ├── solution.py
│   ├── test.py
│   └── debug.py
└── ...
```

## 运行测试

### 方式 1: 运行所有测试用例（推荐用于最终验证）

从项目根目录直接运行：

```bash
python 0026_remove_duplicates_from_sorted_array/test.py
```

或者运行指定的测试用例：

```bash
python 0026_remove_duplicates_from_sorted_array/test.py TestRemoveDuplicates.test_example1
```

### 方式 2: 调试单个测试用例（推荐用于开发调试）

**在 IDE 中调试**：
1. 打开 `debug.py` 文件
2. 在 `solution.py` 或 `debug.py` 中打断点
3. 直接运行 `debug.py`（点击 IDE 的运行按钮）
4. 可以单步调试，查看变量值

**命令行运行**：
```bash
python 0026_remove_duplicates_from_sorted_array/debug.py
```

**自定义测试用例**：
编辑 `debug.py`，修改 `test_custom()` 函数，添加你自己的测试数据，然后运行调试。

## 工作流程

### 添加新题目

1. **提供题目名称**（例如：`26. 删除有序数组中的重复项`）
2. **AI 自动生成**：
   - 创建题目文件夹（如 `0026_remove_duplicates_from_sorted_array/`）
   - 生成 `solution.py` - 包含 `Solution` 类模板（方法签名和文档）
   - 生成 `test.py` - 包含完整的测试用例（unittest）
   - 生成 `debug.py` - 调试脚本（支持断点调试）
3. **实现代码**：在 `solution.py` 中实现 `Solution` 类的方法
4. **调试开发**：使用 `debug.py` 在 IDE 中打断点调试，逐步验证逻辑
5. **验证实现**：运行 `python 题目文件夹/test.py` 验证所有测试用例
6. **完成**：所有测试通过后，题目完成

### 示例

**输入**：
```
26. 删除有序数组中的重复项
```

**AI 生成**：
- `0026_remove_duplicates_from_sorted_array/solution.py` - Solution 模板
- `0026_remove_duplicates_from_sorted_array/test.py` - 测试用例
- `0026_remove_duplicates_from_sorted_array/debug.py` - 调试脚本

**开发调试**：
```bash
# 在 IDE 中打开 debug.py，打断点，运行调试
python 0026_remove_duplicates_from_sorted_array/debug.py
```

**最终验证**：
```bash
python 0026_remove_duplicates_from_sorted_array/test.py
```

## 题目列表

- [x] 0026. Remove Duplicates from Sorted Array (删除有序数组中的重复项)
- [ ] 0027. Remove Element (移除元素)
- [ ] 0088. Merge Sorted Array (合并两个有序数组)
