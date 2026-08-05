# DataStructure_Array Summary

这个文件按“**核心题型/思路**”来分类，目的是方便复习和默写。
有些题可以同时归到多个类别，这里优先按**最核心的解法**来分。

## 1. 二分查找 Binary Search

特点：
- 适合**有序数组**，或者“答案具有单调性”的题
- 核心是：看 `mid`，然后决定去左边还是右边

题目：
- [704-BinarySearch.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/704-BinarySearch.py)：标准二分查找
- [35-searchInsert.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/35-searchInsert.py)：查找插入位置
- [34-searchRange.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/34-searchRange.py)：查找目标区间，可看作边界二分
- [69-mySqrt.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/69-mySqrt.py)：对答案做二分
- [367-isPerfectSquare.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/367-isPerfectSquare.py)：对答案做二分

复习关键词：
- `while l < r` / `while l <= r`
- `mid = (l + r) // 2`
- 左闭右开 or 左闭右闭要统一

## 2. 快速选择 Quickselect

特点：
- 用 big, equal, small 做3个分区
- 不排序整个数组，只让一个 `pivot` 落到最终位置

题目：
- [215-Kth_Largest_Element_in_an_Array.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/215-Kth_Largest_Element_in_an_Array.py)

复习关键词：
- `target_index = len(nums) - k`
- `while` 控整体范围
- `for` 做当前轮的 partition
- `pivot` 先挪到末尾
- `store_index` 维护 `<= pivot` 区域

## 3. 双指针 Two Pointers

特点：
- 两个指针从不同位置出发，或快慢指针同步推进
- 常用于原地修改数组、去重、合并、平方比较

题目：
- [26-removeDuplicates.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/26-removeDuplicates.py)：快慢指针去重
- [27-RemoveElement.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/27-RemoveElement.py)：快慢指针移除元素
- [283-moveZeroes.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/283-moveZeroes.py)：快慢指针移动 0
- [88-MergeSortedArray.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/88-MergeSortedArray.py)：双指针合并两个有序数组
- [977-SquaresofaSortedArray.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/977-SquaresofaSortedArray.py)：左右指针比较平方大小

复习关键词：
- `slow/fast`
- `left/right`
- 原地覆盖

## 4. 滑动窗口 Sliding Window

特点：
- 本质上也是双指针，但重点是维护一个“连续窗口”
- 常见问法：最长、最短、满足条件的连续子数组

题目：
- [209-MinimumSizeSubarraySum.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/209-MinimumSizeSubarraySum.py)：最短满足和的子数组
- [904-totalFruit.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/904-totalFruit.py)：至多两种元素的最长连续区间

复习关键词：
- 右指针扩张
- 左指针收缩
- `while` 维护窗口合法性

## 5. 矩阵模拟 / 边界控制

特点：
- 不是普通一维数组，而是二维矩阵
- 常用四个边界：`top / bottom / left / right`

题目：
- [54-spiralOrder.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/54-spiralOrder.py)：按螺旋顺序读矩阵
- [59-SpiralMatrixII.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/59-SpiralMatrixII.py)：按螺旋顺序生成矩阵
- [LCR-spiralArray.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/LCR-spiralArray.py)：螺旋遍历数组/矩阵

复习关键词：
- 一圈一圈处理
- 更新四条边界
- 注意奇数阶中心点

## 6. 数学 / 数论

特点：
- 核心不在数组技巧，而在数字本身的性质
- 常见是质因数分解、整除、乘积

题目：
- [0-primeFactors.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/0-primeFactors.py)：质因数分解
- [2521-distinctPrimeFactors.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/2521-distinctPrimeFactors.py)：统计不同质因数
- [66-PlusOne.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/66-PlusOne.py)：数位处理，偏模拟/数学

复习关键词：
- `i * i <= n`
- 不断试除
- 数位进位

## 7. 栈 / 字符串模拟

特点：
- 虽然放在数组文件夹里，但核心思路更像栈

题目：
- [844-backspaceCompare.py](file:///Users/wendashi/Desktop/2026/CodingPractice/DataStructure_Array/844-backspaceCompare.py)：用栈模拟退格

复习关键词：
- 遇到普通字符就入栈
- 遇到 `#` 就弹栈

## 一句话索引

- 想到“有序 + 查位置” -> 二分查找
- 想到“第 k 大 / 第 k 小” -> Quickselect
- 想到“原地删除 / 去重 / 移动元素” -> 双指针
- 想到“最长/最短连续子数组” -> 滑动窗口
- 想到“矩阵一圈一圈走” -> 矩阵模拟
- 想到“质因数 / 整除 / 进位” -> 数学

## 目前最值得优先吃透的几类

如果是为了面试和默写，建议先按这个顺序复习：

1. 二分查找
2. 双指针
3. 滑动窗口
4. Quickselect
5. 矩阵模拟
6. 数学 / 其他
