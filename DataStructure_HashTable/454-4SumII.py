class Solution():
    def sumii(self, nums1:list[int], nums2:list[int], nums3:list[int], nums4:list[int]):
        hashtable = {}
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 in hashtable:
                    hashtable[num1 + num2] += 1
                else:
                    hashtable[num1 + num2] = 1

        count = 0
        for num3 in nums3:
            for num4 in nums4:
                if - num3 - num4 in hashtable:
                    count += hashtable[- num3 - num4]
        
        return count
    

sol = Solution()
res = sol.sumii(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0])
print(res)