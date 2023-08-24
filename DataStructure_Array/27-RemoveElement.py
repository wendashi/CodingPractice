class Solution():
    def removeelement(self, nums:list[int], val:int):
        fast, slow = 0, 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow

sol_instance = Solution()

nums1 = [3,2,2,3]
val1 = 3

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
res = sol_instance.removeelement(nums2, val2)
print(res)