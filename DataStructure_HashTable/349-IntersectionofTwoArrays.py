# class Solution():
#     def getintersection(self, nums1:list[int], nums2:list[int]):
#         hash1 = {}
#         res = []

#         for i in nums1:
#             hash1[i] = 1
#             print(i, hash1[i])
        
#         for i in nums2:
#             if i in hash1.keys() and hash1[i] == 1:
#                 res.append(i)
#                 hash1[i] = 0

#         return res

# nums1 = [1,2,2,1]
# nums2 = [2,2]

# nums3 = [4,9,5]
# nums4 = [9,4,9,8,4]

# sol = Solution()
# res = sol.getintersection(nums3, nums4)

# print(res)

#2023.9.17 (6th)

# way1
# class Solution():
#     def intersec(self, nums1: list[int], nums2: list[int]):
#         res = []
#         nums1s = set(nums1)
#         nums2s = set(nums2)
#         for i in nums1s:
#             if i in nums2s:
#                 res.append(i)

#         return res


# sol = Solution()
# res = sol.intersec(nums1 = [1,2,2,1], nums2 = [2,2])
# print(res)

# way2
# class Solution():
#     def intersec(self, nums1: list[int], nums2: list[int]):
#         hash = {}
#         for i in nums1:
#             hash[i] = 1
        
#         res = []
#         for i in nums2:
#             if i in hash.keys() and hash[i] == 1:
#                 res.append(i)
#                 hash[i] -= 1
                
#         return res

# sol = Solution()
# res = sol.intersec(nums1 = [1,2,2,1], nums2 = [2,2])
# print(res)

import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 16:53:50

class Solution():
    def ita(self, nums1: list[int], nums2: list[int]):
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        for i in set2:
            if i in set1:
                res.append(i) 

        return res

sol = Solution()
res = sol.ita(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
print(res)
