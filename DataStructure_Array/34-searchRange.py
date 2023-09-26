import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-21 16:56:42 (1st)

# class Solution():
#     def srange(self, nums: list[int], target: int):
#         def bs(nums: list[int], target: int):
#             l = 0
#             r = len(nums)
#             while l < r:
#                 mid = (l + r) // 2
#                 if nums[mid] == target:
#                     return mid
#                 elif nums[mid] > target:
#                     r = mid
#                 else:
#                     l = mid + 1
            
#             return -1
        
#         index = bs(nums, target)
#         print('index', index)
        
#         if index == -1:
#             return [-1, -1]
        
#         lb, rb = index, index
#         while lb > 0 and nums[lb - 1] == target:
#             lb -= 1
#         while rb < len(nums) - 1 and nums[rb + 1] == target:
#             rb += 1
        
#         return [lb, rb]
    
# sol = Solution()
# res = sol.srange(nums = [1], target = 1)
# print(res)

# 当前时间是: 2023-09-26 13:27:39（2nd）

class Solution():
    def sr(self, nums: list[int], target: int):
        def bs(nums: list[int], target: int):
            l = 0
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid 
                elif nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return [-1, -1]
        
        temp = bs(nums, target)
        print(temp)

        if temp == [-1, -1]:
            return temp
        
        lt = temp
        while lt > 0 and nums[lt - 1] == target:
            lt -= 1

        lr = temp
        while lr < len(nums) - 1 and nums[lr + 1] == target:
            lr += 1
        
        return [lt, lr]

sol = Solution()
res = sol.sr(nums = [1], target = 1)
print(res)

        