# class Solution():
#     def MSSS(self, target:int, nums:list[int]):
#         j = 0 #起始
#         Sum = 0 
#         res = float('inf')
#         for i in range(len(nums)):#终止
#             Sum += nums[i]
#             while Sum >= target:
#                 res = min(res, i-j+1)
#                 Sum -= nums[j]
#                 j += 1
        
#         return 0 if res == float('inf') else res
    
# target1 = 7
# nums1 = [2,3,1,2,4,3]

# target2 = 11
# nums2 = [1,1,1,1,1,1,1,1]

# sol_instance = Solution()
# res = sol_instance.MSSS(target2, nums2)
# print(res)

# 2023.9.20(6th)
# class Solution():
#     def mmsss(self, target: int, nums: list[int]):
#         l = 0
#         sum = 0
#         res = float('inf')
#         for r in range(len(nums)):
#             sum += nums[r] 
#             while sum >= target:
#                 res = min(res, r-l+1)
#                 sum -= nums[l]
#                 l += 1

#         return res if res != float('inf') else 0
    
# sol = Solution()
# res = sol.mmsss(target = 7, nums = [2,3,1,2,4,3])
# print(res)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-21 14:47:52(7th)

# class Solution():
#     def mmsss(self, target: int, nums: list[int]):
#         res = float('inf')
#         l = 0
#         sum = 0
#         for r in range(len(nums)):
#             sum += nums[r]
#             print('sum:',sum)
#             while sum >= target:
#                 sum -= nums[l]
#                 res = min(res, r-l+1)
#                 l += 1
#                 print('res:',res)
        
#         return 0 if res == float('inf') else res
    
# sol = Solution()
# res = sol.mmsss(target = 11, nums = [1,1,1,1,1,1,1,1])
# print(res)

# res = float('inf')
# print('real？',res is float('inf'))  # 这会输出 False，因为它们不是同一个对象

# 当前时间是: 2023-09-21 15:02:52

# 当前时间是: 2023-09-22 15:22:37(8th)

class Solution():
    def minsss(self, target: int, nums: list[int]):
        i = 0
        sum = 0
        res = float('inf')
        for j in range(len(nums)):
            sum += nums[j]
            print(sum, i, j)
            while sum >= target:
                res = min(res, j - i + 1)
                sum -= nums[i]
                i += 1
        
        return 0 if res == float('inf') else res

sol = Solution()
res = sol.minsss(target = 7, nums = [2,3,1,2,4,3])
print(res)