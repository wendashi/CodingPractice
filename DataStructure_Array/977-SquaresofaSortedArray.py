# class Solution():
#     def SquareSortedArray(self, nums:list[int]):
#         l = 0
#         r = len(nums)-1
#         result = []
#         while l < r+1:
#             l_2 = nums[l] ** 2
#             r_2 = nums[r] ** 2
#             print(l_2, r_2)
#             if l_2 < r_2:
#                 result.append(r_2)
#                 r -= 1
#             else:
#                 result.append(l_2)
#                 l += 1
            
#         return result[::-1]
    
# sol_instance = Solution()
# nums1 = [-4,-1,0,3,10]
# nums2 = [-7,-3,2,3,11]
# res = sol_instance.SquareSortedArray(nums2)
# print(res)

# 2023.9.20(9th)

class Solution():
    def ssa(self, nums: list[int]):
        l = 0 
        r = len(nums) - 1
        res = []
        while l < r + 1:
            l2 = nums[l] ** 2
            r2 = nums[r] ** 2
            if l2 > r2:
                res.append(l2)
                l += 1
            else:
                res.append(r2)
                r -= 1
        
        return res[::-1]

sol = Solution()
res = sol.ssa(nums = [-4,-1,0,3,10])
print(res)
