# class Solution():
#     def reversestring(self, s: list[str]):
#         # return s[::-1] 
#         l = 0
#         r = len(s) - 1
#         while l < r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
        
#         return s


import datetime

# 获取当前的日期和时间
current_time = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印当前时间
print("当前时间是:", formatted_time)

# 当前时间是: 2023-09-29 15:46:18
# 2026-08-13 00:10:26 344-7th

class Solution():
    def rever(self, s: str):
        # s[:] = s[::-1]

        left = 0
        right = len(s) - 1

        while left < right:
           temp = s[left]
           s[left] = s[right]
           s[right] = temp
           left += 1
           right -= 1
        
        return s
    
sol = Solution