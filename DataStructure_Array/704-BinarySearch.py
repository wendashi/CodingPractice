# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。

# 你必须编写一个具有 O(log n) 时间复杂度的算法。
# n / 2^k = 1 -> k = log2(n)

# 示例 1:

# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:

# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1

# class Solution():
#     def bs(self, nums: list[int], target: int):
#         l = 0
#         r = len(nums) # 因为 // 2 是向下取整，所以 l = mid + 1 
#         # 区间是 [l, r)
#         while l < r:
#             mid = (l + r)// 2
#             if nums[mid] > target:
#                 r = mid
#             elif nums[mid] < target:
#                 l = mid + 1 # mid 已经确定不可能是答案，所以要把它排除掉。
#             else:
#                 return mid
#         return -1

# sol = Solution()
# res = sol.bs(nums = [-1,0,3,5,9,12], target = 9)
# print(res)


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-26 11:14:31 (10th)

class Solution():
    def bs(self, nums: list[int], target: int):
        l = 0
        r = len(nums) #[l,r)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        return -1

sol = Solution()
res = sol.bs(nums = [-1,0,3,5,9,12], target = 12)
print(res)
            
            
        
