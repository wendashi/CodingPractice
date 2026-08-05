# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 10

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 方法：快速选择 Quickselect
# Quickselect 和快速排序类似：
# 随机选择一个基准值 pivot。
# 分区，使得：小于等于 pivot 的元素在左边；
# 大于 pivot 的元素在右边。

# 分区完成后，pivot 位于它最终排序位置 p。
# 比较 p 和目标下标 n-k：p == n-k：找到答案；
# p < n-k：只搜索右边；
# p > n-k：只搜索左边。

# 每次只需要继续处理一侧，因此平均时间复杂度为 O(n)。

from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 把“第 k 大”转换成“升序排列时的数组下标”
        # partition 结束后，pivot 的下标就是它在完整升序数组中的最终下标
        # 因为 partition 后：左边全部 <= pivot | pivot | 右边全部 > pivot
        target_index = len(nums) - k
        left_index, right_index = 0, len(nums) - 1

        # 如果 pivot 的最终位置正好是 target ，直接返回
        # 如果 pivot 位置太小，就去右半边找，更新 left
        # 如果 pivot 位置太大，就去左半边找，更新 right
        while left_index <= right_index: # quickselect 整体流程的循环
            # 随机一个“数组下标”
            pivot_index = random.randint(left_index, right_index)
            pivot_value = nums[pivot_index]

            # 先把 pivot 的值挪到数组末尾
            nums[pivot_index], nums[right_index] = nums[right_index],  nums[pivot_index]
            
            # 先扫 left ~ right-1, 确保 [left, store_index) 中的元素都 <= pivot_value 
            store_index = left_index
            for scan_index in range(left_index, right_index): # partition 分区扫描
                if nums[scan_index] <= pivot_value:
                    nums[scan_index], nums[store_index] = nums[store_index], nums[scan_index]
                    store_index += 1

            # 把暂存的 pivot (nums[right_index]) 放到分界点
            nums[store_index], nums[right_index] = nums[right_index], nums[store_index]

            if store_index == target_index:
                return nums[store_index]
            elif store_index < target_index:
                left_index = store_index + 1
            else:
                right_index = store_index - 1


eg_nums = [3,2,1,5,6,4]
eg_k = 2

sol = Solution()
output = sol.findKthLargest(eg_nums, eg_k)
print('output:', output)

        