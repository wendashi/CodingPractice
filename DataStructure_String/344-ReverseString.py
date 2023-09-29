# class Solution():
#     def rever(self, s: list[str]):
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s[:] = [s[i] for i in range(len(s)-1, -1, -1)]
#         # return s[:]
        

# sol = Solution()
# res = sol.rever(s = ["h","e","l","l","o"])
# print(res)

## 2023.9.8 two pointers

# class Solution():
#     def reverstring(self, s: list[str]):
#         l = 0
#         r = len(s) - 1
#         while l < r:
#             # tempr = s[r]
#             # templ = s[l]
#             # s[l] = tempr
#             # s[r] = templ
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
            

#         return s[:]
    

# sol = Solution()
# res = sol.reverstring(s = ["h","e","l","l","o"])
# print(res)

# 2023.9.16(6th)

# class Solution():
#     def reversestring(self, s: list[str]):
#         # return s[::-1] 
#         l = 0
#         r = len(s) - 1
#         while l < r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
        
#         return s[:]



# sol = Solution()
# res = sol.reversestring(s = ["h","e","l","l","o"])
# print(res)
# #time: O(n), space: O(1)


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 15:46:18

class Solution():
    def rever(self, s: str):
        s[:] = s[::-1]
    
sol = Solution