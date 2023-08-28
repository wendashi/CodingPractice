class Solution():
    def getintersection(self, nums1:list[int], nums2:list[int]):
        hash1 = {}
        res = []

        for i in nums1:
            hash1[i] = 1
            print(i, hash1[i])
        
        for i in nums2:
            if i in hash1.keys() and hash1[i] == 1:
                res.append(i)
                hash1[i] = 0

        return res

nums1 = [1,2,2,1]
nums2 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]

sol = Solution()
res = sol.getintersection(nums3, nums4)

print(res)