# class Solution():
#     def removeelement(self, nums:list[int], val:int):
#         fast, slow = 0, 0
#         size = len(nums)
#         while fast < size:
#             if nums[fast] != val:
#                 nums[slow] = nums[fast]
#                 slow += 1
#             fast += 1
        
#         return slow

# sol_instance = Solution()

# nums1 = [3,2,2,3]
# val1 = 3

# nums2 = [0,1,2,2,3,0,4,2]
# val2 = 2
# res = sol_instance.removeelement(nums2, val2)
# print(res)

# 2023.9.20(9th)

# class Solution():
#     def remove(self, nums: list[int], val: int):
#         slow, fast = 0, 0

#         while fast < len(nums): #没有减1。如果减1，那长度为1就没法进入循环了
#             # print('fast:',fast)
#             # print('slow:',slow)
#             if nums[fast] != val:
#                 nums[slow] = nums[fast]
#                 # print('nums[slow]',nums[slow])
#                 slow += 1
#             fast += 1
        
#         return slow

# sol = Solution()
# res = sol.remove(nums = [3,2,2,3], val = 3)
# print(res)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# # 当前时间是: 2023-09-21 14:01:50（10th）

# class Solution():
#     def removeelement(self, nums: list[int], val: int):
#         slow , fast = 0, 0
#         size = len(nums)
#         while fast < size:
#             if nums[fast] != val:
#                 nums[slow] = nums[fast]
#                 slow += 1
#             fast += 1
        
#         return slow

# sol = Solution()
# res = sol.removeelement(nums = [3,2,2,3], val = 3)
# print(res)

# 当前时间是: 2023-09-26 14:05:55

class Solution():
    def remove(self, nums: list[int], val: int):
        s, f = 0 , 0
        while f < len(nums):
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1
            f += 1
        
        return s

sol = Solution()
res = sol.remove(nums = [3,2,2,3], val = 3)
print(res)

# 当前时间是: 2023-09-26 14:14:54