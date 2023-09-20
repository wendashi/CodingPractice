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
class Solution():
    def mmsss(self, target: int, nums: list[int]):
        l = 0
        sum = 0
        res = float('inf')
        for r in range(len(nums)):
            sum += nums[r] 
            while sum >= target:
                res = min(res, r-l+1)
                sum -= nums[l]
                l += 1

        return res if res != float('inf') else 0
    
sol = Solution()
res = sol.mmsss(target = 7, nums = [2,3,1,2,4,3])
print(res)