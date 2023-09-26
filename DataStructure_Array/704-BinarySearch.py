# class Solution():
#     def bs(self, nums:list[int], target:int):
#         l = 0
#         r = len(nums)

#         while l < r:
#             mid = (l+r)//2
#             if nums[mid] > target:
#                 r = mid
#             elif nums[mid] < target:
#                 l = mid + 1
#             else:
#                 return mid
        
#         return -1
    

# solution_instance = Solution()

# nums1 = [-1,0,3,5,9,12]

# target1 = 9

# res = solution_instance.bs(nums1, target1)

# print(res)

# 2023.9.20(9th)

# class Solution():
#     def bs(self, nums: list[int], target: int):
#         l = 0
#         r = len(nums) # 因为 // 2 是向下取整，所以
#         while l < r:
#             mid = (l + r)// 2
#             if nums[mid] > target:
#                 r = mid
#             elif nums[mid] < target:
#                 l = mid + 1 
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
        r = len(nums)
        while l < r: # l 最多遍历到 r-1 的位置
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        
        return -1

sol = Solution()
res = sol.bs(nums = [-1,0,3,5,9,12], target = 2)
print(res)
            
            
        
