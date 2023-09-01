class Solution():
    def twoSum(self, nums: list, target: int):
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            
            hashtable[nums[i]] = i
        
        return []
    
nums1 = [2,7,11,15]
target1 = 9

sol = Solution()
res = sol.twoSum(nums1, target1)

print(res)