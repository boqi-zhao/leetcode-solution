# leetcode-solution

LeetCode 题目解答集合

## 项目结构

每道题目一个独立文件夹，文件夹内包含：
- `solution.py` - 包含 `Solution` 类的实现
- `test.py` - 包含测试用例

```
leetcode-solution/
├── 0026_remove_duplicates_from_sorted_array/
│   ├── solution.py    # Solution 类实现
│   └── test.py        # 测试用例
├── 0027_remove_element/
│   ├── solution.py
│   └── test.py
└── ...
```

## 运行测试

### 运行单个题目的测试

从项目根目录直接运行：

```bash
python 0026_remove_duplicates_from_sorted_array/test.py
```

或者进入题目文件夹运行：

```bash
cd 0026_remove_duplicates_from_sorted_array
python test.py
```

## 工作流程

### 添加新题目

1. **提供题目名称**（例如：`26. 删除有序数组中的重复项`）
2. **AI 自动生成**：
   - 创建题目文件夹（如 `0026_remove_duplicates_from_sorted_array/`）
   - 生成 `solution.py` - 包含 `Solution` 类模板（方法签名和文档）
   - 生成 `test.py` - 包含完整的测试用例
3. **实现代码**：在 `solution.py` 中实现 `Solution` 类的方法
4. **验证实现**：运行 `python 题目文件夹/test.py` 验证代码是否正确
5. **完成**：所有测试通过后，题目完成

### 示例

**输入**：
```
26. 删除有序数组中的重复项
```

**AI 生成**：
- `0026_remove_duplicates_from_sorted_array/solution.py` - Solution 模板
- `0026_remove_duplicates_from_sorted_array/test.py` - 测试用例

**验证**：
```bash
python 0026_remove_duplicates_from_sorted_array/test.py
```

## 已完成的题目

- [x] 0026. Remove Duplicates from Sorted Array (删除有序数组中的重复项)
