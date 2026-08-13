# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。

# 示例 2：
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。

# 示例 3：
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。

# 2023.9.17（6th）  

# 时间复杂度分析：

# 首先，代码对输入列表 nums 进行排序，这需要 O(n log n) 的时间，其中 n 是输入列表的长度。
# 接下来，代码使用三重嵌套循环来查找三元组。外层循环迭代了每个元素一次（n次），然后内部的双指针循环在最坏情况下需要 O(n) 的时间，因此总共的时间复杂度为 O(n^2)。
# 在内部的循环中，有一些额外的去重逻辑，但在最坏情况下，仍然只会增加 O(n) 的时间复杂度。
# 因此，总的时间复杂度为 O(n log n) + O(n^2) = O(n^2)。这是该算法的主要时间复杂度。
# 对于时间复杂度的求和，通常我们只关注增长最快的那一项，因为这项将主导算法的性能。

# 空间复杂度分析：

# 由于 result 列表只存储最终的结果，而不会随着输入规模的增加而线性增长，所以空间复杂度是 O(1)


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 20:42:41 (7th)

# class Solution():
#     def threesum(self, nums: list[int]):
#         # 先排序，让“和太大就右指针左移、和太小就左指针右移”成立
#         nums.sort()
#         res = []

#         for i in range(len(nums)):
#             # 排完序后，当前最小数都已经大于 0 ，后面三个数之和不可能再等于 0
#             if nums[i] > 0:
#                 return res
            
#             # 在“第一层”去重，避免同样的起点重复算
#             if i > 0 and nums[i - 1] == nums[i]:
#                 continue
            
#             # 双指针
#             l = i + 1
#             r = len(nums) - 1

#             while l < r:
#                 sum = nums[i] + nums[l] + nums[r]

#                 # 和太大就右指针左移、和太小就左指针右移
#                 if sum > 0 :
#                     r -= 1
#                 elif sum < 0:
#                     l += 1
#                 else:
#                     res.append([nums[i], nums[l], nums[r]])

#                     # 规避左右指针的重复值
#                     while l < r and nums[l + 1] == nums[l]:
#                         l += 1
#                     while l < r and nums[r - 1] == nums[r]:
#                         r -= 1
#                     l += 1
#                     r -= 1
            
#         return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        # 第一个数-i -> 另外两个数-双指针[如果小，左指针就右移，如果大，右指针就左移]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break 

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res
                


sol = Solution()
res = sol.threeSum(nums = [-1,0,1,2,-1,-4])
print(res)