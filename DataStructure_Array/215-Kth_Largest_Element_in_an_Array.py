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

from typing import List
import random

class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            # len(nums) = len(big) + len(equal) + len(small)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(big) + len(equal) < k: # k > len(nums) - len(small):
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(big) - len(equal))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot
        
        return quick_select(nums, k)

eg_nums = [3,2,1,5,6,4]
eg_k = 2

sol = Solution()
output = sol.findKthLargest(eg_nums, eg_k)
print('output:', output)

        
