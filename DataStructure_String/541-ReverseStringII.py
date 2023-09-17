# class Solution():
#     def rever(self, s: str, k: int):
#         res = ''
#         n = len(s)
#         flip = -1
#         for i in range(0, n, k):
#             a = s[i: i+k ]
#             res += a[::flip]
#             flip = -flip

#         return res
    
# sol = Solution()
# res = sol.rever(s = "abcdefg", k = 2)
# print(res)

#2023.9.16（5th）

# class Solution():
#     def reverse2(self, s:str, k:int):
#         flip = -1
#         n = len(s)
#         res = ''
#         for i in range(0, n, k):
#             print(i)
#             x = s[i:i+k]
#             res += x[::flip]
#             flip = -flip
        
#         return res

# sol = Solution()
# result = sol.reverse2(s = "abcdefg", k = 2)
# print(result)

# # 时间复杂度 O(n), 空间复杂度 O(n)

# 2023.9.17(6th)

class Solution():
    def reverstring(self, s: str, k: int):
        res = ''
        flip = -1
        for i in range(0, len(s), k):
            j = s[i : i + k]
            res += j[::flip]
            flip = -flip

        return res

sol = Solution()
res = sol.reverstring(s = "abcdefg", k = 2)
print(res)


