# class Solution():
#     def sumii(self, nums1:list[int], nums2:list[int], nums3:list[int], nums4:list[int]):
#         hashtable = {}
#         for num1 in nums1:
#             for num2 in nums2:
#                 if num1 + num2 in hashtable:
#                     hashtable[num1 + num2] += 1
#                 else:
#                     hashtable[num1 + num2] = 1

#         count = 0
#         for num3 in nums3:
#             for num4 in nums4:
#                 if - num3 - num4 in hashtable:
#                     count += hashtable[- num3 - num4]
        
#         return count
    

# sol = Solution()
# res = sol.sumii(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0])
# print(res)

# class Solution():
#     def foursumii(self, nums1:list[int], nums2:list[int], nums3:list[int], nums4:list[int]):
#         hash = {}
        
#         for i in nums1:
#             for j in nums2:
#                 if i + j not in hash:
#                     hash[i+j] = 1
#                 else:
#                     hash[i+j] += 1 

#         count = 0

#         for i in nums3:
#             for j in nums4:
#                 if -i-j in hash:
#                     count += hash[-i-j]
        
#         return count

# sol = Solution()
# res = sol.foursumii(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2])
# print(res)

# 时间复杂度分析：

# 首先，代码包含两个嵌套的循环，第一个循环遍历nums1，第二个循环遍历nums2，所以两个循环的时间复杂度分别是O(len(nums1))和O(len(nums2))
# 在第一个循环和第二个循环内部，有一些常数时间的操作，如哈希表的查找和更新。
# 接下来，代码包含两个嵌套的循环，第一个循环遍历nums3，第二个循环遍历nums4，所以两个循环的时间复杂度分别是O(len(nums3))和O(len(nums4))。
# 在第三个循环和第四个循环内部，也有一些常数时间的操作，如哈希表的查找。
# 综上所述，该算法的时间复杂度是O(len(nums1) * len(nums2) + len(nums3) * len(nums4))=O(n^2 + n^2)=O(2n^2)=O(n^2)
# 空间复杂度分析：

# 代码使用了一个哈希表hash来存储nums1和nums2中元素的和以及它们的出现次数。哈希表的大小取决于nums1和nums2中可能的不同和的数量。
# 考虑最差的情况，nums1和nums2中元素如果都不相同，可能出现的和的次数就 = O(len(nums1) * len(nums2))，所以哈希表的空间复杂度可以表示为O(len(nums1) * len(nums2))。
# 除了哈希表，代码还使用了一些常数级的额外空间来存储循环变量和计数器。
# 综上所述，该算法的空间复杂度是O(len(nums1) * len(nums2))=O(n^2)。


# 2023.9.17（6th）

# class Solution():
#     def foursum(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]):
#         hash = {}

#         for i in nums1:
#             for j in nums2:
#                 if i + j in hash:
#                     hash[i + j] += 1
#                 else:
#                     hash[i + j] = 1
        
#         res = 0
#         for i in nums3:
#             for j in nums4:
#                 if -i-j in hash:
#                     res += hash[-i-j]
        

#         return res
    
# sol = Solution()
# res = sol.foursum(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2])
# print(res)


#2023.9.19(7th)

class Solution():
    def foursum(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]):
        hash = {}

        for i in nums1:
            for j in nums2:
                if i + j in hash:
                    hash[i + j] += 1
                else:
                    hash[i + j] = 1

        count = 0
        for i in nums3:
            for j in nums4:
                if -i-j in hash:
                    count += hash[-i - j]
        
        return count

sol = Solution()
res = sol.foursum(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2])
print(res)