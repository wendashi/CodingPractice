# class Solution():
#     def Sum3(self, nums: list[int]):
#         nums.sort()
#         result = []
#         for i in range(len(nums)):
#             if nums[i] > 0 :
#                 return result
            
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue # continue 关键字用于跳过当前循环中的剩余代码，并继续下一次循环的执行

#             left = i + 1
#             right = len(nums) - 1

#             while left < right:

#                 sum3 = nums[i] + nums[left] + nums[right]

#                 if sum3 > 0:
#                     right -= 1
#                 elif sum3 < 0:
#                     left += 1
#                 else:
#                     result.append([nums[i], nums[left], nums[right]])

#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     right -= 1
#                     left += 1
        
#         return result
    
# sol = Solution()
# res = sol.Sum3(nums = [-1,0,1,2,-1,-4])
# print(res)

class Solution():
    def sumof3nums(self, nums: list[int]):
        nums.sort()

        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            
            if i > 0 and nums[i] == nums[i - 1]:#i 与 i 的左边去比，left 在 i 的右边
                continue
        
            left = i + 1
            right = len(nums) - 1

            while left < right:
                print(i, left, right)
                print(nums[i], nums[left], nums[right])
                sumof3 = nums[i] + nums[left] + nums[right] #调节

                if sumof3 < 0:
                    left += 1
                elif sumof3 > 0:
                    right -= 1
                else: 
                    result.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left + 1]: #同上
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 不论如何都要移动，可以移动一个，但移动两个更快
                    left += 1
                    right -= 1
                
        return result

sol = Solution()
res = sol.sumof3nums(nums = [1,-1,-1,0])
print(res)

# 时间复杂度分析：

# 首先，代码对输入列表 nums 进行排序，这需要 O(n log n) 的时间，其中 n 是输入列表的长度。
# 接下来，代码使用三重嵌套循环来查找三元组。外层循环迭代了每个元素一次（n次），然后内部的双指针循环在最坏情况下需要 O(n) 的时间，因此总共的时间复杂度为 O(n^2)。
# 在内部的循环中，有一些额外的去重逻辑，但在最坏情况下，仍然只会增加 O(n) 的时间复杂度。
# 因此，总的时间复杂度为 O(n log n) + O(n^2) = O(n^2)。这是该算法的主要时间复杂度。
# 对于时间复杂度的求和，通常我们只关注增长最快的那一项，因为这项将主导算法的性能。

# 空间复杂度分析：

# 额外的空间复杂度主要由 result 列表用来存储符合条件的三元组。在最坏情况下，可能有 O(n^2) 个这样的三元组，因此空间复杂度为 O(n^2)。
# 除了 result 列表之外，代码只使用了一些额外的变量，这些变量的空间复杂度是常量级的，不会随输入规模增加而改变。
# 因此，总的空间复杂度为 O(n^2)。

# 综上所述，该代码的时间复杂度为 O(n^2)，空间复杂度为 O(n^2)。
