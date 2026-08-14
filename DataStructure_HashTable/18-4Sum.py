# https://leetcode.cn/problems/4sum/description/
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
                
import datetime
from typing import List
# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 21:09:20

# class Solution():
#     def foursum(self, nums: list[int], target: int):
#         nums.sort()
#         res = []
#         for i in range(len(nums)):
#             print('i', nums[i])
#             if nums[i] > target and target > 0:
#                 break
            
#             # 避免同样的第一个数重复开头
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             for j in range(i + 1, len(nums)):
#                 print('j', nums[j])
#                 if nums[i] + nums[j] > target and target > 0:
#                     break

#                 # 避免同样的第二个数重复开头
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue

#                 l = j + 1
#                 r = len(nums) - 1

#                 # print(l, r)
#                 while l < r:
#                     sum = nums[i] + nums[j] + nums[l] + nums[r]
#                     # print(([nums[i], nums[j], nums[l], nums[r]]))
#                     # print('sum', sum)
#                     if sum > target:
#                         r -= 1
#                     elif sum < target:
#                         l += 1
#                     else:
#                         # print('???????')
#                         res.append([nums[i], nums[j], nums[l], nums[r]])
#                         # print('res', res)

#                         while l < r and nums[l] == nums[l + 1]:
#                             l += 1
#                         while l < r and nums[r] == nums[r - 1]:
#                             r -= 1
#                         l += 1
#                         r -= 1
        
#         return res

class Solution:
    def fourSum(self, nums: List[int], target: int):
        # 双指针
        nums.sort()
        res = []
        for a in range(len(nums)):
            if nums[a] > target and target >= 0:
                break

            if a > 0 and nums[a - 1] == nums[a]:
                continue

            for b in range(a + 1, len(nums)):
                if nums[b] + nums[a] > target and target >= 0:
                    break
                
                if b > a + 1 and nums[b - 1] == nums[b]:
                    continue

                left = b + 1
                right = len(nums) - 1
                while left < right:
                    print(a, b, left, right)
                    sum_of_4 = nums[a] + nums[b] + nums[left] + nums[right]
                    if sum_of_4 > target:
                        right -= 1
                    elif sum_of_4 < target:
                        left += 1
                    else:
                        res.append([nums[a], nums[b], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res

sol = Solution()
res = sol.fourSum(nums = [-489,-475,-469,-468,-467,-462,-456,-443,-439,-425,-425,-410,-401,-342,-341,-331,-323,-307,-299,-262,-254,-245,-244,-238,-229,-227,-225,-224,-221,-197,-173,-171,-160,-142,-142,-136,-134,-125,-114,-100,-86,-81,-66,-47,-37,-34,4,7,11,34,60,76,99,104,113,117,124,139,141,143,144,146,157,157,178,183,185,189,192,194,221,223,226,232,247,249,274,281,284,293,298,319,327,338,340,368,375,377,379,388,390,392,446,469,480,490], target = 2738)
print(res)