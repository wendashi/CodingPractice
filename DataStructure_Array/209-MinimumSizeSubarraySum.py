class Solution():
    def MSSS(self, target:int, nums:list[int]):
        j = 0 #起始
        Sum = 0 
        res = float('inf')
        for i in range(len(nums)):#终止
            Sum += nums[i]
            while Sum >= target:
                res = min(res, i-j+1)
                Sum -= nums[j]
                j += 1
        
        return 0 if res == float('inf') else res
    
target1 = 7
nums1 = [2,3,1,2,4,3]

target2 = 11
nums2 = [1,1,1,1,1,1,1,1]

sol_instance = Solution()
res = sol_instance.MSSS(target2, nums2)
print(res)