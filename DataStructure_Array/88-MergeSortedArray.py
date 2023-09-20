# class Solution():
#     def merge(self, nums1:list[int], m:int, nums2:list[int], n:int):
#         sorted = []
#         p1, p2 = 0, 0
#         while p1 < m or p2 < n :
#             print('??')
#             if p1 == m:
#                 sorted.append(nums2[p2])
#                 p2 += 1
#                 print(3)
#             elif p2 == n:
#                 sorted.append(nums1[p1])
#                 p1 += 1
#                 print(4)    
#             elif nums1[p1] < nums2[p2]:
#                 sorted.append(nums1[p1])
#                 p1 += 1
#                 print(1)
#             elif nums1[p1] >= nums2[p2]:#else:
#                 sorted.append(nums2[p2]) 
#                 p2 += 1        
#         nums1[:] = sorted
#         print(nums1)

# Solution_instance = Solution()

# res = Solution_instance.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

# print(res)

#2023.9.20(7th)

class Solution():
    def merge(self, nums1: list[int], m: int, nums2: list[int], n :int):
        temp = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p2 == n:
                temp.append(nums1[p1])
                p1 +=1               
            elif p1 == m:
                temp.append(nums2[p2])
                p2 += 1    
            elif nums1[p1] > nums2[p2]:
                temp.append(nums2[p2])
                p2 += 1   
            else:
                temp.append(nums1[p1])
                p1 += 1
        
        nums1[:] = temp[:]

        return nums1
    
sol = Solution()
res = sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
print(res)
