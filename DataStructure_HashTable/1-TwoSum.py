# class Solution():
#     def twoSum(self, nums: list, target: int):
#         hashtable = {}
#         for i, num in enumerate(nums):
#             if target - num in hashtable:
#                 return [hashtable[target - num], i]
            
#             hashtable[nums[i]] = i
        
#         return []
    
# nums1 = [2,7,11,15]
# target1 = 9

# sol = Solution()
# res = sol.twoSum(nums1, target1)

# print(res)

#2023.9.17 (6th)
# class Solution():
#     def twosum(self, nums: list[int], target: int):
#         hash = {}

#         for i, num in enumerate(nums):
#             if target - i in hash.keys():
#                 return [hash[i] , hash[target - i]]
            
#             hash[num] = i
        
# sol = Solution()
# res = sol.twosum(nums = [2,7,11,15], target = 9)
# print(res)

#2023.9.19 (7th)
# class Solution():
#     def twoSum(self, nums: list[int], target: int):
#         hash = {}
#         for i, num in enumerate(nums):
#             if target - num in hash:
#                 return [hash[target - num], i]
#             else:
#                 hash[num] = i
        
#         return None

# sol = Solution()
# res = sol.twoSum(nums = [2,7,11,15], target = 9)
# print(res)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 20:05:33（8th）    

class Solution():
    def twosum(self, nums: list[int], target: int):
        hash = {}
        for i, num in enumerate(nums):
            hash[num] = i

        for j in range(len(nums)):
            if target - nums[j] in hash.keys() and j != hash[target - nums[j]]:
                return [j, hash[target - nums[j]]]
        
sol = Solution()
res = sol.twosum(nums = [3,3], target = 6)
print(res)