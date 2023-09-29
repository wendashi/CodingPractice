# class Solution():
#     def foursum(self, nums: list[int], target: int):
#         result = []
#         nums.sort()
#         n = len(nums)

#         for i in range(n):
#             if nums[i] > 0 and target > 0:
#                 break

#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             for j in range(i + 1, n):
#                 if nums[j] > 0 and target > 0:
#                     break

#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue

#                 left = j + 1
#                 right = n - 1

#                 while left < right:
#                     sum4 = nums[i] + nums[j] + nums[left] + nums[right]

#                     if sum4 > target:
#                         right -= 1
#                     elif sum4 < target:
#                         left += 1
#                     else:
#                         result.append([nums[i], nums[j], nums[left], nums[right]])
                        
#                         while left < right and nums[right] == nums[right - 1]:
#                             right -= 1
#                         while left < right and nums[left] == nums[left + 1]:
#                             left += 1
#                         right -= 1
#                         left += 1

#             return result

# nums1 = [1,0,-1,0,-2,2]
# target1 = 0                    

# sol = Solution()
# res = sol.foursum(nums1, target1)
# print(res)
                    

# class Solution():
#     def sumof4(self, nums: list[int], target: int):
#         result = []
#         nums.sort()
#         print(nums)

#         for i in range(len(nums)):
#             if target > 0 and nums[i] > target:
#                 return result
            
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             j = i + 1
#             for j in range(i+1, len(nums)):
#                 print(i, j)
#                 if target > 0 and nums[i] + nums[j] > target:
#                     return result

#                 if j > i + 1  and nums[j] == nums[j - 1]:
#                     continue

#                 left = j + 1
#                 right = len(nums) - 1
#                 while left < right:
#                     sumof4 = nums[i] + nums[j] + nums[left] + nums[right]
#                     if sumof4 > target:
#                         right -= 1

#                     elif sumof4 < target:
#                         left += 1

#                     else:
#                         result.append([nums[i], nums[j], nums[left], nums[right]])

#                         while left < right and nums[left] == nums[left + 1]:
#                             left += 1
#                         while left < right and nums[right] == nums[right - 1]:
#                             right -= 1
#                         left += 1
#                         right -= 1
        
#         return result
        
# sol = Solution()
# res = sol.sumof4(nums = [1,0,-1,0,-2,2], target = 0)
# print(res)


# 2023.9.17 (6th)

# class Solution():
#     def sumoffour(self, nums: list[int], target: int):
#         res = []
#         nums.sort()
#         # print(nums)

#         for i in range(len(nums)):
#             # print('nums[i]', nums[i])
#             if target > 0 and nums[i] > target:
#                 break

#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             for j in range(i + 1, len(nums)):
#                 # print('nums[j]', nums[j])
#                 if target > 0 and nums[i] + nums[j] > target:
#                     break

#                 if j > i+1 and nums[j] == nums[j - 1]:
#                     continue

#                 l = j + 1
#                 r = len(nums) - 1

#                 while l < r :
#                     sum = nums[i] + nums[j] + nums[l] + nums[r]
#                     if sum < target:
#                         l += 1
#                     elif sum > target:
#                         r -= 1
#                     else:
#                         res.append([nums[i], nums[j], nums[l], nums[r]])

#                         while l < r and nums[l] == nums[l + 1]:
#                             l += 1
#                         while l < r and nums[r] == nums[r - 1]:
#                             r -= 1
#                         l += 1
#                         r -= 1
        
#         return res
    
# sol = Solution()
# res = sol.sumoffour(nums = [1,0,-1,0,-2,2], target = 0)
# print(res)
                
import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 21:09:20

class Solution():
    def foursum(self, nums: list[int], target: int):
        nums.sort()
        res = []
        for i in range(len(nums)):
            print('i', nums[i])
            if nums[i] > target and target > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                print('j', nums[j])
                if nums[i] + nums[j] > target and target > 0:
                    break
                
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = len(nums) - 1

                # print(l, r)
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    print(([nums[i], nums[j], nums[l], nums[r]]))
                    print('sum', sum)
                    if sum > target:
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        print('???????')
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        print('res', res)

                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        
        return res

sol = Solution()
res = sol.foursum(nums = [-3,-4,5,5,-5], target = 2)
print(res)