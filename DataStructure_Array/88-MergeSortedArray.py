class Solution():
    def merge(self, nums1:list[int], m:int, nums2:list[int], n:int):
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n :
            print('??')
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
                print(3)
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
                print(4)    
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
                print(1)
            elif nums1[p1] >= nums2[p2]:#else:
                sorted.append(nums2[p2]) 
                p2 += 1        
        nums1[:] = sorted
        print(nums1)

Solution_instance = Solution()

res = Solution_instance.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

print(res)
