import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-22 12:28:59

# class Solution():
#     def movezero(self, nums: list[int]):
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j += 1

#         return nums[:]

# sol = Solution()
# res = sol.movezero([0,1,0,3,12])
# print(res)

# 当前时间是: 2023-09-26 14:15:50

class Solution():
    def move0(self, nums: list[int]):
        s, f = 0, 0
        while f < len(nums):
            if nums[f] != 0:
                nums[s], nums[f] = nums[f], nums[s]
                s += 1
            f += 1
        
        return nums

sol = Solution()
res = sol.move0( nums = [0,1,0,3,12])
print(res)